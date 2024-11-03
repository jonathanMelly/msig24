# Entrée, sorties et nombres aléatoires

## Introduction

Nous allons apprendre à utiliser les entrées et sorties dans la console ainsi que
l'utilisation de la classe Random en C#. Ces concepts sont très importants pour la programmation, car ils permettent de
communiquer avec l'utilisateur et de générer des nombres aléatoires.

## Entrées et sorties dans la console

### Sortie dans la console

Pour afficher du texte dans la console, nous pouvons utiliser la méthode `Console.WriteLine()`. Cette méthode prend en
paramètre une chaîne de caractères et l'affiche dans la console. Voici un exemple :

```csharp
Console.WriteLine("Bonjour, monde !");
```

Cette ligne de code affiche le message "Bonjour, monde !" dans la console.

### Entrée dans la console

Pour lire une entrée de l'utilisateur dans la console, nous pouvons utiliser la méthode `Console.ReadLine()`. Cette
méthode lit une ligne de texte entrée par l'utilisateur et la retourne sous forme de chaîne de caractères. Voici un
exemple :

```csharp
Console.Write("Entrez votre nom : ");
string nom = Console.ReadLine();
Console.WriteLine("Bonjour, " + nom + " !");
```

Dans cet exemple, nous demandons à l'utilisateur d'entrer son nom, puis nous affichons un message de bienvenue en
utilisant la valeur entrée par l'utilisateur.

## Utilisation de Random

La classe Random est utilisée pour générer des nombres aléatoires. Pour utiliser cette classe, nous devons d'abord créer
une instance de la classe Random. Voici un exemple :

```csharp
Random rnd = new Random();
```

Une fois que nous avons créé une instance de la classe Random, nous pouvons utiliser la méthode `Next()` pour générer un
nombre aléatoire. Cette méthode prend en paramètre un entier qui représente la limite supérieure du nombre aléatoire.
Voici un exemple :

```csharp
int nombreAleatoire = rnd.Next(10);
Console.WriteLine("Le nombre aléatoire est : " + nombreAleatoire);
```

Dans cet exemple, nous générons un nombre aléatoire entre 0 et 9 (inclus) et l'affichons dans la console.

## Nuances 🔎

Maintenant que les bases sont décrites, regardons certains aspects avec plus de détail

### Write() et WriteLine()

Pour afficher du texte dans la console, nous pouvons utiliser les méthodes `Write()` et `WriteLine()`. La différence
entre ces deux méthodes est que `Write()` affiche le texte sans aller à la ligne, tandis que `WriteLine()` affiche le
texte et va à la ligne. Voici un exemple :

```csharp
Console.Write("Bonjour, ");
Console.WriteLine("monde !");
```

Cette ligne de code affiche le message "Bonjour, monde !" dans la console. Notez que le message est affiché sur deux
lignes, car nous avons utilisé `Write()` pour afficher le premier mot et `WriteLine()` pour afficher le reste du message.

> On peut aussi transformer le `Write` en `WriteLine` en ajoutant le caractère `\n` (retour de chariot) à la fin :

```csharp
Console.Write("Bonjour\nMonde\n");

//Équivalent
Console.WriteLine("Bonjour");
Console.WriteLine("Monde");
```

### Chaîne de formatage avec $""

Pour afficher du texte dans la console avec des variables, nous pouvons utiliser la chaîne de formatage avec `$""`.
Cette notation permet d'insérer des variables directement dans la chaîne de caractères de manière
plus performante qu'avec l'opérateur `+`... Voici un exemple :

```csharp
string prenom = "John";
string nom = "Doe";
Console.WriteLine($"Bonjour, {prenom} {nom} !");
```

Cette ligne de code affiche le message "Bonjour, John Doe !" dans la console. Notez que nous avons utilisé la
notation `$""` pour insérer les variables `prenom` et `nom` directement dans la chaîne de caractères.

### Conversion de ReadLine() en int

Pour lire une entrée de l'utilisateur dans la console et la convertir en entier, nous pouvons utiliser la
méthode `Convert.ToInt32()`. Cette méthode prend en paramètre une chaîne de caractères et la convertit en entier. Voici
un exemple :

```csharp
Console.Write("Entrez un nombre : ");
string input = Console.ReadLine();
int nombre = Convert.ToInt32(input);
Console.WriteLine("Vous avez entré le nombre : " + nombre);
```

Dans cet exemple, nous demandons à l'utilisateur d'entrer un nombre, puis nous lisons l'entrée de l'utilisateur
avec `ReadLine()`. Nous convertissons ensuite l'entrée en entier avec `Convert.ToInt32()` et nous affichons le résultat
dans la console.