# Sérialisation en PHP (sauvegarde et restauration d’informations structurées...)

## Objectif

- Gérer une liste d'élèves sous forme structurée (nom et prénom).
- Sauvegarder les données dans un fichier JSON pour persister l'état.
- Recharger les données sauvegardées lors d'une nouvelle exécution.

## Exemple Complet : Gestion, Sauvegarde et Chargement

### Étape 1 : Gestion des Données

Un tableau associatif contient les élèves sous la forme :

```php
[
    ["prenom" => "Bob", "nom" => "Martin"],
    ["prenom" => "Max", "nom" => "Dupont"],
    ["prenom" => "Alice", "nom" => "Durand"]
]
```

### Étape 2 : Sauvegarde et Rechargement avec Fichier JSON

Code complet :

```php
<?php
// Chemin du fichier pour persistance
$fichier = 'eleves.json';

// Étape 1 : Charger les données existantes
if (file_exists($fichier)) {
    $eleves = json_decode(file_get_contents($fichier), true); // Recharger depuis JSON
    echo "Données chargées depuis $fichier.\n";
} else {
    $eleves = []; // Initialisation si le fichier n'existe pas
}

// Étape 2 : Ajouter un nouvel élève
$eleves[] = ["prenom" => "Lucie", "nom" => "Bernard"]; // Ajouter un nouvel élève
$eleves[] = ["prenom" => "Paul", "nom" => "Lemoine"];  // Ajouter un autre élève

// Afficher la liste des élèves
echo "Liste des élèves :\n";
foreach ($eleves as $eleve) {
    echo "Prénom : {$eleve['prenom']}, Nom : {$eleve['nom']}\n";
}

// Étape 3 : Sauvegarder les données dans un fichier JSON
file_put_contents($fichier, json_encode($eleves));
echo "Données sauvegardées dans $fichier.\n";
```

## 3. Fonctionnalités Étendues

### Fonction de Chargement des Données

Pour encapsuler la logique de chargement :

```php
function chargerDonnees($fichier) {
    if (file_exists($fichier)) {
        return json_decode(file_get_contents($fichier), true);
    }
    return [];
}
```

### Fonction de Sauvegarde des Données

Pour encapsuler la logique de sauvegarde :

```php
function sauvegarderDonnees($fichier, $eleves) {
    file_put_contents($fichier, json_encode($eleves));
}
```

### Exemple d’Utilisation

```php
<?php
$fichier = 'eleves.json';

// Charger les données
$eleves = chargerDonnees($fichier);

// Ajouter un élève
$eleves[] = ["prenom" => "Emma", "nom" => "Durand"];

// Sauvegarder les données
sauvegarderDonnees($fichier, $eleves);

// Afficher les élèves
foreach ($eleves as $eleve) {
    echo "Prénom : {$eleve['prenom']}, Nom : {$eleve['nom']}\n";
}
```

## Points Clés

1. **Persistance** :
    - Utiliser **JSON** pour enregistrer les tableaux associatifs dans un format lisible et réutilisable.
    - Méthodes :
        - `json_encode` : Convertir un tableau PHP en chaîne JSON.
        - `json_decode` : Convertir une chaîne JSON en tableau PHP.

2. **Stockage sur Fichier** :
    - Utiliser `file_put_contents` pour écrire dans un fichier.
    - Utiliser `file_get_contents` pour lire un fichier.

3. **Organisation du Code** :
    - Encapsuler la logique de chargement et de sauvegarde dans des fonctions permet une meilleure réutilisation.
