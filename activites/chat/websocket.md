# Alternative : websocket

## Étape 1: Installation de Ratchet pour PHP WebSockets

D'abord, nous devons installer Ratchet, une bibliothèque PHP pour WebSockets. Créons un fichier `composer.json` :

```json
{
    "require": {
        "cboden/ratchet": "^0.4.4"
    },
    "autoload": {
        "psr-4": {
            "MyApp\\": "src"
        }
    }
}
```

Ensuite, installez les dépendances avec Composer :

```bash
composer install
```

## Étape 2: Créer le serveur WebSocket

Créons un dossier `src` et un fichier `src/Chat.php` pour notre serveur WebSocket :

```php
<?php
namespace MyApp;
use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;
use PDO;

class Chat implements MessageComponentInterface {
    protected $clients;
    protected $db;

    public function __construct() {
        $this->clients = new \SplObjectStorage;
        
        // Connexion à la base de données
        $host = 'localhost';
        $dbname = 'chat_app';
        $username = 'root';
        $password = '';
        
        try {
            $this->db = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
            $this->db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(\PDOException $e) {
            die('Erreur de connexion à la base de données: ' . $e->getMessage());
        }
    }

    public function onOpen(ConnectionInterface $conn) {
        // Stocker la nouvelle connexion
        $this->clients->attach($conn);
        echo "Nouvelle connexion! ({$conn->resourceId})\n";
    }

    public function onMessage(ConnectionInterface $from, $msg) {
        $data = json_decode($msg, true);
        
        // Vérifier si les données sont valides
        if (isset($data['username']) && isset($data['message'])) {
            $username = htmlspecialchars($data['username']);
            $message = htmlspecialchars($data['message']);
            $timestamp = time();
            
            // Enregistrer le message dans la base de données
            try {
                $stmt = $this->db->prepare("INSERT INTO messages (username, message, timestamp) VALUES (:username, :message, :timestamp)");
                $stmt->bindParam(':username', $username);
                $stmt->bindParam(':message', $message);
                $stmt->bindParam(':timestamp', $timestamp);
                $stmt->execute();
                
                // Préparer le message à diffuser
                $response = json_encode([
                    'username' => $username,
                    'message' => $message,
                    'timestamp' => $timestamp
                ]);
                
                // Diffuser le message à tous les clients connectés
                foreach ($this->clients as $client) {
                    $client->send($response);
                }
                
            } catch(\PDOException $e) {
                echo "Erreur lors de l'enregistrement du message: " . $e->getMessage() . "\n";
            }
        }
    }

    public function onClose(ConnectionInterface $conn) {
        // Supprimer la connexion
        $this->clients->detach($conn);
        echo "Connexion {$conn->resourceId} fermée\n";
    }

    public function onError(ConnectionInterface $conn, \Exception $e) {
        echo "Une erreur est survenue: {$e->getMessage()}\n";
        $conn->close();
    }
}
```

## Étape 3: Créer le script pour démarrer le serveur WebSocket

Créons un fichier `bin/chat-server.php` :

```php
<?php
require dirname(__DIR__) . '/vendor/autoload.php';

use Ratchet\Server\IoServer;
use Ratchet\Http\HttpServer;
use Ratchet\WebSocket\WsServer;
use MyApp\Chat;

$server = IoServer::factory(
    new HttpServer(
        new WsServer(
            new Chat()
        )
    ),
    8080
);

echo "Serveur WebSocket démarré sur le port 8080\n";
$server->run();
```

## Étape 4: Modifier le HTML

Modifions notre fichier HTML pour charger les messages au début et pour afficher un indicateur de statut de connexion :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application de Chat WebSocket</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h2>Chat en direct</h2>
            <div id="connection-status">Non connecté</div>
        </div>
        <div class="chat-messages" id="chat-messages">
            <!-- Les messages s'afficheront ici -->
        </div>
        <div class="chat-input">
            <input type="text" id="username" placeholder="Votre nom" />
            <input type="text" id="message" placeholder="Écrivez votre message..." />
            <button id="send-btn">Envoyer</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

## Étape 5: Mettre à jour le CSS pour le statut de connexion

Ajoutons quelques styles pour l'indicateur de statut :

```css
/* Ajouter à votre fichier style.css existant */

#connection-status {
    font-size: 0.8em;
    padding: 5px 10px;
    border-radius: 10px;
    background-color: #f44336;
    color: white;
    display: inline-block;
    margin-left: 10px;
}

#connection-status.connected {
    background-color: #4CAF50;
}

/* Ajuster la disposition du header */
.chat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.chat-header h2 {
    margin: 0;
}
```

## Étape 6: Remplacer le JavaScript par du code WebSocket

Remplaçons complètement notre fichier `script.js` avec une version WebSocket :

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Sélection des éléments DOM
    const chatMessages = document.getElementById('chat-messages');
    const usernameInput = document.getElementById('username');
    const messageInput = document.getElementById('message');
    const sendButton = document.getElementById('send-btn');
    const connectionStatus = document.getElementById('connection-status');
    
    // Créer une connexion WebSocket
    let socket;
    let reconnectInterval = null;
    
    function connectWebSocket() {
        // Connexion WebSocket (modifiez l'URL selon votre configuration)
        socket = new WebSocket('ws://localhost:8080');
        
        // Gestionnaire d'ouverture de connexion
        socket.onopen = function(e) {
            console.log('Connexion WebSocket établie');
            connectionStatus.textContent = 'Connecté';
            connectionStatus.classList.add('connected');
            
            // Charger les messages existants lors de la connexion
            loadExistingMessages();
            
            // Nettoyer tout intervalle de reconnexion existant
            if (reconnectInterval) {
                clearInterval(reconnectInterval);
                reconnectInterval = null;
            }
        };
        
        // Gestionnaire de message reçu
        socket.onmessage = function(event) {
            const data = JSON.parse(event.data);
            displayMessage(data.username, data.message, data.timestamp);
        };
        
        // Gestionnaire de fermeture de connexion
        socket.onclose = function(event) {
            console.log('Connexion WebSocket fermée:', event);
            connectionStatus.textContent = 'Déconnecté - Tentative de reconnexion...';
            connectionStatus.classList.remove('connected');
            
            // Tenter de se reconnecter toutes les 5 secondes
            if (!reconnectInterval) {
                reconnectInterval = setInterval(connectWebSocket, 5000);
            }
        };
        
        // Gestionnaire d'erreur
        socket.onerror = function(error) {
            console.error('Erreur WebSocket:', error);
            connectionStatus.textContent = 'Erreur de connexion';
            connectionStatus.classList.remove('connected');
        };
    }
    
    // Fonction pour charger les messages existants (uniquement lors de la connexion initiale)
    function loadExistingMessages() {
        fetch('get_messages.php')
            .then(response => response.json())
            .then(data => {
                // Effacer les messages actuels
                chatMessages.innerHTML = '';
                
                // Afficher les messages
                data.forEach(msg => {
                    displayMessage(msg.username, msg.message, msg.timestamp);
                });
                
                // Faire défiler vers le bas
                chatMessages.scrollTop = chatMessages.scrollHeight;
            })
            .catch(error => console.error('Erreur:', error));
    }
    
    // Fonction pour afficher un message
    function displayMessage(username, message, timestamp) {
        const messageDiv = document.createElement('div');
        const currentUser = usernameInput.value.trim();
        
        // Déterminer si le message est envoyé ou reçu
        if (username === currentUser) {
            messageDiv.className = 'message sent';
        } else {
            messageDiv.className = 'message received';
        }
        
        // Formater l'heure
        const date = new Date(timestamp * 1000);
        const formattedTime = date.toLocaleTimeString();
        
        // Construire le contenu du message
        messageDiv.innerHTML = `
            <div class="message-info">${username} - ${formattedTime}</div>
            <div class="message-text">${message}</div>
        `;
        
        chatMessages.appendChild(messageDiv);
        
        // Faire défiler vers le bas
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Fonction pour envoyer un message
    function sendMessage() {
        const username = usernameInput.value.trim();
        const message = messageInput.value.trim();
        
        if (username === '' || message === '') {
            alert('Veuillez entrer votre nom et un message');
            return;
        }
        
        if (socket.readyState === WebSocket.OPEN) {
            // Envoyer le message au serveur WebSocket
            socket.send(JSON.stringify({
                username: username,
                message: message
            }));
            
            // Effacer le champ de message
            messageInput.value = '';
        } else {
            alert('Pas connecté au serveur. Veuillez réessayer.');
        }
    }
    
    // Écouteurs d'événements
    sendButton.addEventListener('click', sendMessage);
    
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    // Établir la connexion WebSocket initiale
    connectWebSocket();
});
```

## Étape 7: Conserver le fichier PHP pour charger les messages existants

Gardons notre fichier `get_messages.php` pour charger les messages existants lors de la connexion initiale :

```php
<?php
// Ce fichier reste identique à la version précédente
require_once 'config.php';

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

try {
    $stmt = $db->prepare("SELECT username, message, timestamp FROM messages ORDER BY timestamp DESC LIMIT 50");
    $stmt->execute();
    
    $messages = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $messages = array_reverse($messages);
    
    echo json_encode($messages);
    
} catch(PDOException $e) {
    echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
}
?>
```

## Étape 8: Démarrer le serveur WebSocket

Pour démarrer le serveur WebSocket, exécutez la commande suivante dans un terminal :

```bash
php bin/chat-server.php
```

Gardez ce terminal ouvert pour maintenir le serveur WebSocket en fonctionnement.

<details>

<summary>Utilisation en production</summary>

1. Configurer le serveur WebSocket comme un service (avec systemd sur Linux par exemple)
2. Utiliser un proxy WebSocket (comme Nginx) pour gérer SSL et les connexions externes
3. Implémenter une authentification plus robuste
4. Considérer l'utilisation de Redis pour la gestion des messages entre plusieurs instances de serveur

Voici un exemple de configuration Nginx pour un proxy WebSocket :

```nginx
server {
    listen 443 ssl;
    server_name votre-domaine.com;

    ssl_certificate /chemin/vers/certificat.crt;
    ssl_certificate_key /chemin/vers/cle-privee.key;

    location /ws/ {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /chemin/vers/votre/application;
        index index.html index.php;
        # ... autres configurations PHP ...
    }
}
```
</details>


## Conclusion

Votre application de chat utilise maintenant les WebSockets pour une communication en temps réel, ce qui offre plusieurs avantages :

1. Latence réduite : les messages sont transmis instantanément
2. Moins de charge serveur : pas de requêtes HTTP constantes
3. Communication bidirectionnelle : le serveur peut envoyer des messages aux clients sans requête
4. Économie de bande passante : les connexions WebSocket sont plus légères que les requêtes HTTP répétées

Cette implémentation WebSocket est beaucoup plus efficace que la version AJAX avec polling, surtout lorsque le nombre d'utilisateurs augmente. Les utilisateurs verront les messages apparaître instantanément sans avoir à attendre le prochain cycle de polling.

N'oubliez pas que pour que ce système fonctionne correctement, le serveur WebSocket doit rester actif en permanence, ce qui nécessite une configuration appropriée sur votre serveur de production.