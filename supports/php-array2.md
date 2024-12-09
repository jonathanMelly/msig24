# Tableaux associatifs

## Tableau Simple : Liste de Prénoms

Ce type de tableau est utilisé pour une simple énumération de prénoms.

### Exemple : Tableau de prénoms

```php
$eleves = ["Bob", "Max", "Alice"];

// Affichage des prénoms
foreach ($eleves as $prenom) {
    echo "Prénom : $prenom\n";
}
```

## Conversion en Tableau Associatif Avec Clé `prenom`

On enrichit le tableau en convertissant chaque élément pour qu’il contienne une clé `prenom`.

### Exemple : Conversion en associatif

```php
$eleves = ["Bob", "Max", "Alice"];
$elevesAssoc = [];

// Conversion
foreach ($eleves as $prenom) {
    $elevesAssoc[] = ["prenom" => $prenom];
}

// Affichage
foreach ($elevesAssoc as $eleve) {
    echo "Prénom : {$eleve['prenom']}\n";
}
```

## Version Complète : Tableau Associatif Avec `nom` et `prenom`

On passe à un tableau associatif où chaque entrée contient des clés `nom` et `prenom`.

### Exemple : Tableau enrichi avec nom et prénom

```php
$eleves = [
    ["prenom" => "Bob", "nom" => "Martin"],
    ["prenom" => "Max", "nom" => "Dupont"],
    ["prenom" => "Alice", "nom" => "Durand"],
];

// Affichage des prénoms et noms
foreach ($eleves as $eleve) {
    echo "Prénom : {$eleve['prenom']}, Nom : {$eleve['nom']}\n";
}
```

## Comparaison et Évolution

Voici une vue d'ensemble des différentes structures et leur utilisation.

| **Type**                 | **Structure**                                | **Utilisation**                         |
|--------------------------|----------------------------------------------|-----------------------------------------|
| Tableau simple           | `["Bob", "Max", "Alice"]`                    | Listes simples sans structure complexe. |
| Associatif avec `prenom` | `[["prenom" => "Bob"], ["prenom" => "Max"]]` | Ajout d’une structure minimale.         |
| Associatif complet       | `[["prenom" => "Bob", "nom" => "Martin"]]`   | Gestion d’informations détaillées.      |
