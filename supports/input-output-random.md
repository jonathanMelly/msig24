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
lignes, car nous avons utilisé `Write()` pour afficher le premier mot et `WriteLine()` pour afficher le reste du
message.

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

### Formatage

Pour formater l'affichage des nombres dans la console en C#, vous pouvez utiliser des chaînes de format. Voici quelques
exemples pour différents types de formatage :

#### 1. Format numérique standard

Utilisez des [chaînes de format](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings) 
standard comme `N`, `F`, `E`, etc.

```csharp
double nombre = 12345.6789;

// Format numérique standard avec séparateur de milliers
Console.WriteLine(nombre.ToString("N")); // Affiche "12,345.68" (dépend du paramètre culturel)

// Format avec 2 décimales fixes
Console.WriteLine(nombre.ToString("F2")); // Affiche "12345.68"

// Format scientifique
Console.WriteLine(nombre.ToString("E2")); // Affiche "1.23E+004"
```

#### 2. Format personnalisé

Vous pouvez également utiliser des chaînes de format personnalisées pour un meilleur contrôle.

```csharp
double nombre = 12345.6789;

// Format personnalisé avec séparateur de milliers et 2 décimales
Console.WriteLine(nombre.ToString("#,##0.00")); // Affiche "12,345.68"

// Format personnalisé pour afficher uniquement la partie entière
Console.WriteLine(nombre.ToString("0")); // Affiche "12346" (arrondi)

// Format personnalisé pour ajouter des zéros de tête
Console.WriteLine(nombre.ToString("000000")); // Affiche "012346" (arrondi)
```

#### 3. En utilisant la culture

Pour définir une culture spécifique (ex. pour l'affichage en français), vous pouvez spécifier la culture dans la méthode
`ToString`.

```csharp
using System.Globalization;

double nombre = 12345.6789;
CultureInfo cultureFr = new CultureInfo("fr-FR");

// Affiche "12 345,68" avec la culture française
Console.WriteLine(nombre.ToString("N", cultureFr));
```

#### 4. Interpolation de chaînes avec format

Avec l'interpolation de chaînes, vous pouvez appliquer un format directement dans une chaîne.

```csharp
double nombre = 12345.6789;
Console.WriteLine($"{nombre:N2}"); // Affiche "12,345.68"
```

### Alignement

Pour aligner les nombres lors de l'affichage dans la console en C#, vous pouvez utiliser des méthodes de formatage et
des chaînes de format avec des espaces réservés. Voici plusieurs techniques pour obtenir l'alignement souhaité :

### 1. Alignement avec interpolation de chaînes

En utilisant les interpolations de chaînes, vous pouvez spécifier un [alignement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated) en ajoutant un nombre dans les
accolades. Un nombre positif aligne à droite, tandis qu'un nombre négatif aligne à gauche.

```csharp
double nombre = 12345.6789;

// Aligner à droite dans un espace de 15 caractères
Console.WriteLine($"{nombre,15:N2}"); // Affiche "       12,345.68" (15 caractères)

// Aligner à gauche dans un espace de 15 caractères
Console.WriteLine($"{nombre,-15:N2}"); // Affiche "12,345.68       " (15 caractères)
```

### 2. Alignement avec `String.Format`

La méthode `String.Format` permet également de spécifier un alignement en combinant les chaînes de format avec un
espacement spécifique.

```csharp
double nombre = 12345.6789;

// Aligner à droite dans un espace de 15 caractères
Console.WriteLine(String.Format("{0,15:N2}", nombre)); // Affiche "       12,345.68"

// Aligner à gauche dans un espace de 15 caractères
Console.WriteLine(String.Format("{0,-15:N2}", nombre)); // Affiche "12,345.68       "
```

### 3. Alignement dans un tableau de données

Si vous avez plusieurs valeurs à afficher de manière alignée, par exemple dans un tableau, vous pouvez combiner ces
techniques pour obtenir un affichage en colonnes.

```csharp
double[] nombres = { 123.45, 6789.01, 23.4, 567890.123 };
Console.WriteLine("{0,10} | {1,10}", "Nombre", "Formaté");

foreach (var nombre in nombres)
{
    Console.WriteLine("{0,10} | {1,10:N2}", nombre, nombre);
}

// Exemple d'affichage :
//    Nombre |  Formaté
//     123.45 |    123.45
//   6789.01 |   6,789.01
//      23.4 |     23.40
// 567890.12 | 567,890.12
```

### 4. Utiliser `PadLeft` et `PadRight`

Vous pouvez aussi utiliser `PadLeft` et `PadRight` pour des ajustements précis de chaînes si vous préférez manipuler les
chaînes directement.

```csharp
double nombre = 12345.6789;

// Convertir en chaîne et utiliser PadLeft pour l'alignement à droite
Console.WriteLine(nombre.ToString("N2").PadLeft(15));

// Convertir en chaîne et utiliser PadRight pour l'alignement à gauche
Console.WriteLine(nombre.ToString("N2").PadRight(15));
```

Ces méthodes vous permettent de contrôler l'alignement et le format des nombres dans la console, ce qui peut être
particulièrement utile pour l'affichage de tableaux de données ou pour une présentation soignée.