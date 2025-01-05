# PHP `Todo List` ✅

Dans cet exercice, vous allez créer une application web simple pour gérer une **ToDo List**. L'application permettra
d'ajouter, afficher, marquer comme complétée et supprimer des tâches.

## Prérequis

- PHP (7.x ou 8.x)
- Serveur local (ex. XAMPP, WAMP, Laragon)
- Navigateur web
- Base de données (MariaDB, MySQL, SQLite)

## Étapes

### Création de la base de données

Créez une table `tasks` avec les colonnes suivantes :

- `id` : Identifiant unique (clé primaire)
- `task` : Description de la tâche
- `is_done` : État de la tâche (`0` pour non terminée, `1` pour terminée)

<details>
<summary>Idée de solution</summary>

```sql
-- Pour SQLite ou MySQL
CREATE TABLE tasks
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    task    TEXT    NOT NULL,
    is_done BOOLEAN NOT NULL DEFAULT 0
);
```

</details>

### Connexion à la base de données avec PDO

Créez un fichier `db.php` pour la gestion de la connexion.

<details>
<summary>Idée de solution</summary>

```php
<?php
// db.php
$dsn = "mysql:host=localhost;dbname=todo;charset=utf8mb4";
$username = ""; // MySQL: votre utilisateur
$password = ""; // MySQL: votre mot de passe

try {
    $pdo = new PDO($dsn, $username, $password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    die("Erreur de connexion à la base de données : " . $e->getMessage());
}
?>
```

</details>

> [!TIP]
> La fonction `require` permet d’importer une partie de code PHP, ainsi la connexion à la base de données est décrite
> sur un seul fichier et on peut facilement la mettre à jour...

### Interface HTML pour la gestion des tâches

Créez un fichier `index.php` avec un formulaire pour ajouter des tâches et afficher la liste existante.

<details>
<summary>Idée de solution</summary>

```php
<?php
require 'db.php';

// Ajouter une tâche
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $task = $_POST['task'];

    $stmt = $pdo->prepare("INSERT INTO tasks (task) VALUES (:task)");
    $stmt->execute(['task' => $task]);

    header('Location: index.php');
    exit;
}

// Récupérer toutes les tâches
$stmt = $pdo->query("SELECT * FROM tasks");
$tasks = $stmt->fetchAll();
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo List</title>
</head>
<body>
    <h1>ToDo List</h1>

    <form method="POST">
        <input type="text" name="task" placeholder="Nouvelle tâche" required>
        <button type="submit">Ajouter</button>
    </form>

    <h2>Liste des tâches</h2>
    <ul>
        <?php foreach ($tasks as $task): ?>
            <li>
                <form method="POST" action="update.php" style="display:inline;">
                    <input type="hidden" name="id" value="<?= $task['id'] ?>">
                    <button type="submit" name="toggle" style="background:none;border:none;color:inherit;">
                        <?= $task['is_done'] ? '✅' : '⬜' ?>
                    </button>
                </form>
                <?= htmlspecialchars($task['task']) ?>
                <a href="delete.php?id=<?= $task['id'] ?>">Supprimer</a>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

</details>

### Marquer une tâche comme terminée / non terminée

Créez un fichier `update.php` pour gérer l’état d’une tâche.

<details>
<summary>Idée de solution</summary>

```php
<?php
require 'db.php';

if (isset($_POST['id'])) {
    $stmt = $pdo->prepare("UPDATE tasks SET is_done = NOT is_done WHERE id = :id");
    $stmt->execute(['id' => $_POST['id']]);
}

header('Location: index.php');
exit;
?>
```

</details>

### Suppression d’une tâche

Créez un fichier `delete.php` pour gérer la suppression des tâches.

<details>
<summary>Idée de solution</summary>

```php
<?php
require 'db.php';

if (isset($_GET['id'])) {
    $stmt = $pdo->prepare("DELETE FROM tasks WHERE id = :id");
    $stmt->execute(['id' => $_GET['id']]);
}

header('Location: index.php');
exit;
?>
```

</details>

## Résultat attendu

- Une interface web permettant de :
    - Ajouter des tâches.
    - Voir la liste des tâches avec une case ✅ ou ⬜ pour marquer leur état.
    - Supprimer une tâche.

## Améliorations possibles

- Ajouter une validation pour éviter les doublons.
- Mettre en place des filtres (par exemple, afficher uniquement les tâches terminées ou non terminées).
- Ajouter du style avec CSS pour une meilleure expérience utilisateur.

## Exemple d’amélioration CSS

### Ajout de CSS dans un fichier séparé

Créez un fichier `styles.css` pour gérer les styles.

```css
/* styles.css */

/* Style général de la page */
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    width: 400px;
}

/* Titre principal */
h1 {
    font-size: 24px;
    color: #333;
    text-align: center;
}

/* Formulaire pour ajouter une tâche */
form {
    display: flex;
    margin-bottom: 20px;
}

form input[type="text"] {
    flex: 1;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-right: 10px;
}

form button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    font-size: 16px;
    border-radius: 4px;
    cursor: pointer;
}

form button:hover {
    background-color: #218838;
}

/* Liste des tâches */
ul {
    list-style: none;
    padding: 0;
}

li {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 15px;
    border-bottom: 1px solid #ddd;
}

li:last-child {
    border-bottom: none;
}

/* Bouton d'état (complété ou non) */
li button {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 18px;
}

/* Lien pour supprimer une tâche */
li a {
    color: #dc3545;
    text-decoration: none;
    font-size: 14px;
}

li a:hover {
    text-decoration: underline;
}

/* Tâches complétées */
li.completed {
    text-decoration: line-through;
    color: #999;
}
```

### Liaison du fichier CSS avec la page HTML

Ajoutez une balise `<link>` dans la section `<head>` de votre fichier `index.php` :

```php
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <h1>ToDo List</h1>
    <!-- Le reste de votre code HTML -->
</div>
</body>
</html>
```

### Mise à jour du fichier PHP pour inclure des classes CSS dynamiques

Ajoutez une classe `completed` pour les tâches marquées comme terminées.

```php
<ul>
    <?php foreach ($tasks as $task): ?>
        <li class="<?= $task['is_done'] ? 'completed' : '' ?>">
            <form method="POST" action="update.php" style="display:inline;">
                <input type="hidden" name="id" value="<?= $task['id'] ?>">
                <button type="submit" name="toggle">
                    <?= $task['is_done'] ? '✅' : '⬜' ?>
                </button>
            </form>
            <?= htmlspecialchars($task['task']) ?>
            <a href="delete.php?id=<?= $task['id'] ?>">Supprimer</a>
        </li>
    <?php endforeach; ?>
</ul>
```

### Explications des éléments CSS

1. **Structure générale**

- **`body`** : Centrer le contenu verticalement et horizontalement grâce à `flexbox`.
- **`.container`** : Ajout d'une boîte blanche avec des ombres et un arrondi pour un effet "carte".

2. **Formulaire**

- **`form input[type="text"]`** : Largeur flexible pour s'adapter à l'espace disponible.
- **`form button`** : Couleur verte pour le bouton avec un effet de survol plus foncé.

3. **Liste des tâches**

- **`li`** : Affichage en ligne des éléments avec une bordure entre les tâches.
- **`.completed`** : Ligne barrée et couleur grise pour les tâches terminées.

4. **Interactions**

- **`li button:hover`** et **`li a:hover`** : Ajout d'effets pour indiquer les interactions possibles (survol).

### Améliorations possibles

- Ajouter un thème sombre (dark mode).
- Créer un affichage responsive pour les appareils mobiles.
- Ajouter des animations pour les transitions (par exemple, lorsqu'une tâche est supprimée).

## DarkMode et Animations

### Ajouter le Dark Mode avec un bouton de basculement

Ajoutez un bouton de basculement au-dessus du formulaire dans `index.php` :

```php
<div class="container">
    <h1>ToDo List</h1>
    <button id="toggle-dark-mode">🌙 Mode sombre</button>
    <form method="POST">
        <input type="text" name="task" placeholder="Nouvelle tâche" required>
        <button type="submit">Ajouter</button>
    </form>
    <!-- Liste des tâches -->
</div>
```

### Mise à jour du CSS

Ajoutez les styles pour le Dark Mode dans `styles.css` :

```css
/* Dark mode par défaut */
body.dark-mode {
    background-color: #121212;
    color: #ffffff;
}

body.dark-mode .container {
    background-color: #1e1e1e;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.6);
}

body.dark-mode form input[type="text"] {
    background-color: #2c2c2c;
    color: #ffffff;
    border: 1px solid #444;
}

body.dark-mode form button {
    background-color: #3a7f48;
}

body.dark-mode ul li {
    border-bottom: 1px solid #444;
}

body.dark-mode li.completed {
    color: #666;
}

body.dark-mode li a {
    color: #ff6666;
}
```

### Ajout de JavaScript pour gérer le Dark Mode

Créez un fichier `script.js` et ajoutez le code suivant pour gérer le mode sombre :

```javascript
// script.js
document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.getElementById("toggle-dark-mode");

    // Vérifier si l'utilisateur a activé le mode sombre précédemment
    if (localStorage.getItem("dark-mode") === "true") {
        document.body.classList.add("dark-mode");
        toggleButton.textContent = "☀️ Mode clair";
    }

    toggleButton.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");

        // Sauvegarder la préférence dans le stockage local
        const isDarkMode = document.body.classList.contains("dark-mode");
        localStorage.setItem("dark-mode", isDarkMode);

        toggleButton.textContent = isDarkMode ? "☀️ Mode clair" : "🌙 Mode sombre";
    });
});
```

Ajoutez ce script dans votre fichier `index.php` :

```html

<script src="script.js"></script>
```

### Ajouter des animations pour les transitions

Ajoutez des **animations CSS** pour les tâches lorsqu'elles sont ajoutées ou supprimées.

Dans `styles.css` :

```css
/* Animation pour l'ajout d'une tâche */
@keyframes slideIn {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

/* Animation pour la suppression d'une tâche */
@keyframes fadeOut {
    from {
        opacity: 1;
        transform: scale(1);
    }
    to {
        opacity: 0;
        transform: scale(0.9);
    }
}

/* Appliquer l'animation */
li {
    animation: slideIn 0.3s ease-out;
}

/* Animation lors de la suppression */
li.removed {
    animation: fadeOut 0.3s ease-in forwards;
}
```

### Mise à jour de la suppression des tâches (avec JavaScript)

Ajoutez une classe `removed` avant la suppression dans `delete.php` :

```php
<?php
require 'db.php';

if (isset($_GET['id'])) {
    $id = $_GET['id'];
    echo "<script>
        document.querySelector('li[data-id=\"$id\"]').classList.add('removed');
        setTimeout(() => {
            window.location.href = 'delete.php?id=$id';
        }, 300); // Délai pour l'animation
    </script>";
}
?>
```

## Validation

Pour tester correctement votre application ToDo List, voici une liste de tests fonctionnels que vous pouvez effectuer
pour valider les fonctionnalités **Dark Mode** et **Animations**.

### 1. **Test du Dark Mode**

#### Étapes :

1. Chargez la page `index.php` dans votre navigateur.
2. Cliquez sur le bouton **"🌙 Mode sombre"**.
3. Vérifiez que :

- L'arrière-plan devient sombre.
- Les textes et les éléments s’adaptent au mode sombre (voir les styles CSS).

4. Rechargez la page :

- Vérifiez que le mode sombre est conservé (stockage local).

#### Cas de test supplémentaires :

- Si le mode sombre est activé, cliquez sur **"☀️ Mode clair"** et vérifiez que les styles reviennent au mode clair.
- Supprimez les données du stockage local (via la console du navigateur) et rechargez la page. Vérifiez que le mode par
  défaut est le mode clair.

### 2. **Test d'ajout de tâches avec animation**

#### Étapes :

1. Saisissez une tâche dans le formulaire et cliquez sur le bouton **Ajouter**.
2. Vérifiez que :

- La tâche apparaît avec une animation **glissement de gauche**.
- La tâche est bien enregistrée dans la base de données (via un `SELECT` dans la base).

#### Cas de test supplémentaires :

- Essayez d’ajouter une tâche vide (doit être bloqué par le champ `required` dans le formulaire HTML).
- Ajoutez plusieurs tâches d'affilée et vérifiez que chaque tâche utilise l’animation.

---

### 3. **Test de suppression avec animation**

#### Étapes :

1. Supprimez une tâche existante en cliquant sur le lien **Supprimer**.
2. Vérifiez que :

- La tâche disparaît avec une animation **rétrécissement et disparition**.
- La tâche est bien supprimée de la base de données.

#### Cas de test supplémentaires :

- Tentez de supprimer une tâche qui n'existe pas (par exemple en modifiant l'URL). Vérifiez qu'il n'y a pas d'erreur.
- Supprimez plusieurs tâches et vérifiez que l'animation est appliquée à chacune.

---

### 4. **Test de persistance des données**

#### Étapes :

1. Ajoutez plusieurs tâches.
2. Rechargez la page.
3. Vérifiez que toutes les tâches ajoutées sont toujours visibles.

#### Cas de test supplémentaires :

- Passez en mode sombre, ajoutez une tâche, rechargez la page, et vérifiez que le mode sombre est toujours activé.
- Supprimez une tâche en mode sombre, et vérifiez que les styles restent cohérents.


### 5. **Test des tâches terminées**

#### Étapes :

1. Cliquez sur le bouton **✅** ou **⬜** pour marquer une tâche comme terminée ou non terminée.
2. Vérifiez que :

- L’état de la tâche change instantanément dans l’interface (avec ou sans rechargement selon votre implémentation).
- Les styles sont mis à jour (ligne barrée pour les tâches terminées).
- L’état est correctement enregistré dans la base de données.

#### Cas de test supplémentaires :

- Changez l’état d’une tâche plusieurs fois et vérifiez que cela fonctionne à chaque fois.
- Rechargez la page et vérifiez que l’état est correctement affiché.


### 6. **Test des animations globales**

#### Étapes :

1. Ajoutez une tâche.
2. Supprimez une tâche.
3. Changez l’état d’une tâche.
4. Vérifiez que :

- Les animations fonctionnent pour chaque action.
- Les transitions sont fluides et sans erreur.


## Automatisation des tests avec Selenium (Facultatif)

Pour automatiser ces tests, vous pouvez utiliser **Selenium** avec PHP ou un autre langage (comme Python). Voici un
exemple pour tester l'ajout de tâches :

### Exemple en Python avec Selenium

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configurer le driver
driver = webdriver.Chrome()

try:
    # Ouvrir l'application
    driver.get("http://localhost/todo_list/index.php")

    # Ajouter une tâche
    task_input = driver.find_element(By.NAME, "task")
    task_input.send_keys("Test Selenium")
    task_input.send_keys(Keys.RETURN)

    # Vérifier que la tâche est ajoutée
    tasks = driver.find_elements(By.TAG_NAME, "li")
    assert any("Test Selenium" in task.text for task in tasks), "La tâche n'a pas été ajoutée !"

    print("Test réussi : Ajout de tâche")
finally:
    driver.quit()
```

## Résultats attendus

- Tous les cas de test doivent être validés avec succès.
- Les animations doivent être fluides.
- Le Dark Mode doit être fonctionnel et persistant.
- Les actions (ajout, suppression, modification) doivent bien interagir avec la base de données.

## Livrables
Vidéo de max 1 minute qui montre les fonctionnalités

