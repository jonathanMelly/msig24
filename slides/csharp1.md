---
theme: default
title: C#1
class: text-center
drawings:
  persist: true
transition: slide-left
mdc: true
---
# Introduction à C# : Les Bases

---

## Variables

```csharp
// Déclaration de variables
var nombre = 5;
var texte = "Hello, World!";
```

**Explication :**
- Utilisez `var` pour laisser C# déduire le type de la variable.
- Suivez la convention camelCase pour nommer vos variables.

---

## Types de Données

```csharp
// Exemples de types
int entier = 10;
double decimal = 3.14;
bool vraiOuFaux = true;
string message = "Bonjour !";
```

**Principaux Types :**
- **int** : pour les nombres entiers.
- **double** : pour les nombres décimaux.
- **bool** : pour les valeurs vrai/faux.
- **string** : pour le texte.

---

## Opérateurs

```csharp
int a = 10;
int b = 5;
int somme = a + b;        // 15
int produit = a * b;      // 50
int modulo = a % b;       // 0
```

**Explication :**
- Opérateurs arithmétiques : `+`, `-`, `*`, `/`, `%`
- Opérateurs de comparaison : `==`, `!=`, `>`, `<`, `>=`, `<=`

---

## Conditions

```csharp
int age = 20;
if (age >= 18)
{
    Console.WriteLine($"Vous êtes majeur.");
}
else
{
    Console.WriteLine($"Vous êtes mineur.");
}
```

**Syntaxe Conditionnelle :**
- Utilisez `if`, `else` pour gérer la logique conditionnelle.

---

## Entrée Utilisateur

```csharp
Console.Write("Entrez votre nom : ");
string nom = Console.ReadLine();
Console.WriteLine($"Bonjour, {nom} !");
```

**Explication :**
- **`Console.ReadLine()`** pour capturer une entrée utilisateur.
- **`Console.WriteLine()`** pour afficher une sortie, en utilisant l’interpolation de chaînes.

---

## Sorties

```csharp
int age = 25;
Console.WriteLine($"Vous avez {age} ans.");
```

**String Interpolation :**
- Placez `$` avant la chaîne pour intégrer des variables directement.

---

## Conversions

```csharp
string nombreTexte = "42";
int nombre = int.Parse(nombreTexte); // Convertit en int

double decimal = 3.14;
int entier = (int)decimal;           // Cast en int
```

**Conversions Fréquentes :**
- **`int.Parse()`**, **`double.Parse()`** pour convertir des chaînes.
- Utilisez `(int)` pour un cast direct.

---

## Valeurs Aléatoires

```csharp
Random random = new Random();
int nombreAleatoire = random.Next(1, 101); // Entre 1 et 100
Console.WriteLine($"Nombre aléatoire : {nombreAleatoire}");
```

**Explication :**
- Utilisez la classe **`Random`** pour générer des nombres aléatoires.

---

## Récapitulatif

- **Variables** : Déclarez avec `var`.
- **Types** : int, double, bool, string.
- **Opérateurs** : +, -, *, /, %.
- **Conditions** : if, else.
- **Entrée/Sortie** : Console.
- **Conversions** : `int.Parse`, cast `(int)`.
- **Aléatoire** : `Random`.

**Vous êtes prêt à coder en C# !**

---
