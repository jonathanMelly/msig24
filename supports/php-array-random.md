# Listes (tableaux), debug et aléatoire en php

## Déclaration d'un tableau en syntaxe courte

```php
// Liste d'élèves
$eleves = ["Alice", "Bob", "Charlie", "Diana", "Eve"];

// Afficher la structure du tableau avec var_dump
var_dump($eleves);
/*
Résultat :
array(5) {
  [0]=> string(5) "Alice"
  [1]=> string(3) "Bob"
  [2]=> string(7) "Charlie"
  [3]=> string(5) "Diana"
  [4]=> string(3) "Eve"
}
*/
```

> [!TIP]
> la fonction `var_dump` permet d’afficher le contenu étendu d’une variable,
> ce qui est très pratique pour déboguer

## Accéder à des éléments d'un tableau

```php
// Accéder au premier et au troisième élément
echo $eleves[0]; // Affiche "Alice"
echo $eleves[2]; // Affiche "Charlie"

// Vérifier un élément avec var_dump
var_dump($eleves[2]);
/*
Résultat :
string(7) "Charlie"
*/
```

## Ajouter ou modifier des éléments

### Ajouter un élément :

```php
$eleves[] = "Frank"; // Ajoute "Frank" à la fin du tableau
var_dump($eleves);
/*
Résultat :
array(6) {
  [0]=> string(5) "Alice"
  [1]=> string(3) "Bob"
  [2]=> string(7) "Charlie"
  [3]=> string(5) "Diana"
  [4]=> string(3) "Eve"
  [5]=> string(5) "Frank"
}
*/
```

### Modifier un élément :

```php
$eleves[1] = "Benjamin"; // Remplace "Bob" par "Benjamin"
var_dump($eleves);
/*
Résultat :
array(6) {
  [0]=> string(5) "Alice"
  [1]=> string(8) "Benjamin"
  [2]=> string(7) "Charlie"
  [3]=> string(5) "Diana"
  [4]=> string(3) "Eve"
  [5]=> string(5) "Frank"
}
*/
```

## Parcourir un tableau avec une boucle

### Exemple avec `foreach` :

```php
foreach ($eleves as $index => $eleve) {
    echo "Élève $index : $eleve\n";
}
```

## Sélectionner un élève aléatoire avec `random_int`

### Utilisation de `random_int` pour sélectionner un élève :

```php
// Générer un index aléatoire
$indexAleatoire = random_int(0, count($eleves) - 1);

// Accéder à l'élève correspondant
$eleveChoisi = $eleves[$indexAleatoire];

echo "Élève choisi aléatoirement : $eleveChoisi\n";

// Debug avec var_dump
var_dump($indexAleatoire);
var_dump($eleveChoisi);
```

**Explication :**

- `random_int(min, max)` génère un entier aléatoire sécurisé entre `min` et `max`.
- `count($eleves)` retourne le nombre d'éléments dans le tableau.
