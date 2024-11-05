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

Pour gérer les erreurs de conversion  [voir ci-après](#contrôle-de-conversion)

### Formatage

Pour formater l'affichage des nombres dans la console en C#, vous pouvez utiliser des chaînes de format. Voici quelques
exemples pour différents types de formatage :

#### 1. Format numérique standard

Utilisez
des [chaînes de format](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings)
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

En utilisant les interpolations de chaînes, vous pouvez spécifier
un [alignement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated) en ajoutant un
nombre dans les
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

## Contrôle de conversion

La méthode `TryParse` en C# est utilisée pour convertir une chaîne de caractères en une valeur numérique ou un autre
type, tout en gérant les erreurs de conversion sans générer d'exception. Elle est particulièrement utile lorsqu'il est
possible que l'entrée soit invalide (par exemple, un utilisateur pourrait entrer un texte non convertible en nombre). Si
la conversion réussit, elle renvoie `true` et stocke le résultat dans une variable fournie ; sinon, elle renvoie
`false`.

### Structure générale

```csharp
bool TryParse(string input, out T result)
```

- **`input`** : La chaîne de caractères à convertir.
- **`out result`** : La variable de sortie où le résultat de la conversion est stocké si celle-ci est réussie.
- **Retourne** : Un booléen (`true` ou `false`) indiquant si la conversion a réussi.

### Exemple d'utilisation avec `int.TryParse`

Supposons que vous souhaitiez convertir une chaîne en entier (`int`) :

```csharp
string entree = "123";
int nombre;

if (int.TryParse(entree, out nombre))
{
    Console.WriteLine("Conversion réussie : " + nombre); // Affiche "Conversion réussie : 123"
}
else
{
    Console.WriteLine("Conversion échouée");
}
```

### Exemple avec une entrée invalide

Si l'entrée contient un texte non convertible en entier, `TryParse` renvoie `false` sans lever d'exception :

```csharp
string entreeInvalide = "abc";
int nombre;

if (int.TryParse(entreeInvalide, out nombre))
{
    Console.WriteLine("Conversion réussie : " + nombre);
}
else
{
    Console.WriteLine("Conversion échouée"); // Affiche "Conversion échouée"
}
```

### Variantes de `TryParse`

`TryParse` est disponible pour de nombreux types numériques et de date, comme `double`, `decimal`, `DateTime`, et bien
d'autres. Voici quelques exemples d'utilisation :

#### `double.TryParse`

```csharp
string entree = "12.34";
double nombre;

if (double.TryParse(entree, out nombre))
{
    Console.WriteLine("Conversion réussie : " + nombre); // Affiche "Conversion réussie : 12.34"
}
else
{
    Console.WriteLine("Conversion échouée");
}
```

#### `DateTime.TryParse`

```csharp
string dateEntree = "2024-11-05";
DateTime date;

if (DateTime.TryParse(dateEntree, out date))
{
    Console.WriteLine("Conversion réussie : " + date.ToShortDateString()); // Affiche "Conversion réussie : 05/11/2024"
}
else
{
    Console.WriteLine("Conversion échouée");
}
```

### Avantages de `TryParse`

- **Prévention des exceptions** : Contrairement à `Parse`, `TryParse` ne lève pas d'exception en cas d'échec de
  conversion, rendant le code plus robuste.
- **Vérification de validité** : Permet de vérifier facilement si une entrée est convertible, idéal pour les données
  saisies par l'utilisateur.
- **Simplicité** : Facilite la gestion des conversions en échec sans nécessiter de gestion d'erreur avec `try-catch`.

En résumé, `TryParse` est une méthode pratique et sécurisée pour convertir des chaînes de caractères tout en gérant
facilement les erreurs de conversion.

### Alternative

On peut aussi utiliser `try-catch` avec `Parse` pour gérer les erreurs de conversion, mais cela
est généralement moins performant et moins recommandé pour des conversions répétées ou lorsque les échecs sont
probables, car lever une exception est plus coûteux que simplement vérifier un `true` ou `false` avec `TryParse`.

### Utilisation de `Parse` avec `try-catch`

La méthode `Parse` en C# tente de convertir une chaîne en un type spécifique. Si la conversion échoue (par exemple, si
la chaîne contient des caractères non valides pour ce type), elle lèvera une exception `FormatException`. Vous pouvez
utiliser `try-catch` pour gérer cette exception et effectuer un traitement en cas d'erreur.

### Exemple avec `int.Parse` et `try-catch`

Voici un exemple de conversion d'une chaîne en entier avec `int.Parse`, en capturant les erreurs avec `try-catch` :

```csharp
string entree = "123";
int nombre;

try
{
    nombre = int.Parse(entree);
    Console.WriteLine("Conversion réussie : " + nombre); // Affiche "Conversion réussie : 123"
}
catch (FormatException)
{
    Console.WriteLine("Erreur : La chaîne n'est pas dans un format correct pour un entier.");
}
catch (OverflowException)
{
    Console.WriteLine("Erreur : La valeur est trop grande ou trop petite pour un entier.");
}
```

### Exemple avec une entrée invalide

Si l'entrée contient des caractères non numériques ou si le nombre est trop grand pour le type entier (`int`), `Parse`
lève une exception. Voici un exemple avec une entrée invalide :

```csharp
string entreeInvalide = "abc";
int nombre;

try
{
    nombre = int.Parse(entreeInvalide);
    Console.WriteLine("Conversion réussie : " + nombre);
}
catch (FormatException)
{
    Console.WriteLine("Erreur : La chaîne n'est pas dans un format correct pour un entier."); // Affiche ce message
}
catch (OverflowException)
{
    Console.WriteLine("Erreur : La valeur est trop grande ou trop petite pour un entier.");
}
```

### Variantes avec d'autres types et exceptions

Vous pouvez utiliser le même principe avec d'autres types de données comme `double`, `decimal`, ou `DateTime`. La
méthode `Parse` pour ces types lève également une `FormatException` si la chaîne n'est pas convertible, et
éventuellement une `OverflowException` si le nombre est hors limites du type.

#### Exemple avec `double.Parse`

```csharp
string entree = "12.34";
double nombre;

try
{
    nombre = double.Parse(entree);
    Console.WriteLine("Conversion réussie : " + nombre); // Affiche "Conversion réussie : 12.34"
}
catch (FormatException)
{
    Console.WriteLine("Erreur : La chaîne n'est pas dans un format correct pour un nombre décimal.");
}
catch (OverflowException)
{
    Console.WriteLine("Erreur : La valeur est trop grande ou trop petite pour un nombre décimal.");
}
```

#### Exemple avec `DateTime.Parse`

```csharp
string dateEntree = "2024-11-05";
DateTime date;

try
{
    date = DateTime.Parse(dateEntree);
    Console.WriteLine("Conversion réussie : " + date.ToShortDateString()); // Affiche "Conversion réussie : 05/11/2024"
}
catch (FormatException)
{
    Console.WriteLine("Erreur : La chaîne n'est pas dans un format correct pour une date.");
}
```

### Différences entre `Parse` et `TryParse`

- **Gestion des erreurs** : `Parse` utilise des exceptions (`try-catch`) pour gérer les erreurs de format, tandis que
  `TryParse` utilise un retour booléen (`true` ou `false`).
- **Performance** : `TryParse` est plus performant car il n’utilise pas d’exceptions en cas d’échec, alors que `Parse`
  lève une exception, ce qui peut ralentir le programme s'il y a de nombreux échecs de conversion.
- **Complexité** : `TryParse` est généralement plus simple et plus sécurisé pour valider les entrées utilisateur et
  éviter les erreurs.

En résumé, si vous attendez que les échecs de conversion soient rares ou voulez une approche de gestion d’erreur unifiée
dans un bloc `try-catch`, `Parse` avec `try-catch` peut être acceptable. Cependant, **`TryParse` reste généralement
préférable pour gérer des entrées utilisateur imprévisibles**.

## Couleur

En C#, vous pouvez changer la couleur du texte et le fond dans la console en utilisant les propriétés
`Console.ForegroundColor` et `Console.BackgroundColor`. Il est souvent pratique de sauvegarder la couleur d'origine
avant de la changer pour pouvoir la restaurer ensuite.

Voici comment procéder :

### Exemple : Changer la couleur de texte et de fond, puis restaurer les couleurs d'origine

```csharp
// Sauvegarder les couleurs actuelles
ConsoleColor couleurTexteOriginale = Console.ForegroundColor;
ConsoleColor couleurFondOriginale = Console.BackgroundColor;

// Définir de nouvelles couleurs
Console.ForegroundColor = ConsoleColor.Yellow;
Console.BackgroundColor = ConsoleColor.Blue;

// Afficher le texte avec les nouvelles couleurs
Console.WriteLine("Texte en jaune sur fond bleu.");

// Rétablir les couleurs d'origine
Console.ForegroundColor = couleurTexteOriginale;
Console.BackgroundColor = couleurFondOriginale;

// Afficher un texte avec les couleurs originales pour vérification
Console.WriteLine("Texte avec les couleurs d'origine.");
```

### Explication du code

1. **Sauvegarder les couleurs actuelles** : `Console.ForegroundColor` et `Console.BackgroundColor` stockent les couleurs
   actuelles. En les assignant à des variables (ici `couleurTexteOriginale` et `couleurFondOriginale`), vous pouvez les
   réutiliser après avoir temporairement changé les couleurs.

2. **Changer les couleurs** : Vous pouvez ensuite définir de nouvelles couleurs. Dans cet exemple, le texte devient
   jaune (`ConsoleColor.Yellow`) et le fond devient bleu (`ConsoleColor.Blue`).

3. **Afficher le texte** : Le texte affiché entre les modifications de couleur utilise les nouvelles couleurs
   spécifiées.

4. **Restaurer les couleurs d'origine** : En réaffectant les valeurs sauvegardées, vous rétablissez les couleurs
   initiales de la console, ce qui permet de garder une apparence cohérente après l'affichage coloré.

### Exemple de couleurs disponibles

Voici quelques options de couleur disponibles dans `ConsoleColor` :

- `ConsoleColor.Black`
- `ConsoleColor.DarkBlue`
- `ConsoleColor.DarkGreen`
- `ConsoleColor.DarkCyan`
- `ConsoleColor.DarkRed`
- `ConsoleColor.DarkMagenta`
- `ConsoleColor.DarkYellow`
- `ConsoleColor.Gray`
- `ConsoleColor.DarkGray`
- `ConsoleColor.Blue`
- `ConsoleColor.Green`
- `ConsoleColor.Cyan`
- `ConsoleColor.Red`
- `ConsoleColor.Magenta`
- `ConsoleColor.Yellow`
- `ConsoleColor.White`

### Astuce pour avancés : Encapsuler dans une fonction

Pour rendre cela plus pratique et éviter de toujours sauvegarder et restaurer manuellement, vous pouvez encapsuler
l'affichage coloré dans une fonction :

```csharp
void AfficherTexteCouleur(string texte, ConsoleColor couleurTexte, ConsoleColor couleurFond)
{
    // Sauvegarder les couleurs actuelles
    ConsoleColor couleurTexteOriginale = Console.ForegroundColor;
    ConsoleColor couleurFondOriginale = Console.BackgroundColor;

    // Appliquer les nouvelles couleurs
    Console.ForegroundColor = couleurTexte;
    Console.BackgroundColor = couleurFond;

    // Afficher le texte
    Console.WriteLine(texte);

    // Rétablir les couleurs d'origine
    Console.ForegroundColor = couleurTexteOriginale;
    Console.BackgroundColor = couleurFondOriginale;
}

// Exemple d'utilisation
AfficherTexteCouleur("Attention !", ConsoleColor.Red, ConsoleColor.White);
AfficherTexteCouleur("Information", ConsoleColor.Green, ConsoleColor.Black);
```

Cela vous permet d'appeler `AfficherTexteCouleur` avec le texte et les couleurs souhaitées, tout en assurant que les
couleurs d'origine seront automatiquement restaurées.