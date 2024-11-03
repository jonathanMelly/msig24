# Hello, World! en C#

Bienvenue dans le monde de la programmation ! Voici quelques termes clés que vous rencontrerez souvent :

## Vocabulaire

1. **IDE (Integrated Development Environment)** : Un IDE est un environnement de développement intégré qui fournit des
   outils pour écrire, tester et déboguer du code. Il peut inclure un éditeur de texte, un compilateur, un débogueur et
   d'autres fonctionnalités utiles. En C#, Visual Studio est un exemple courant d'IDE.

2. **Débogage** : Le débogage est le processus de recherche et de correction des erreurs dans votre code. Les erreurs
   peuvent être des bugs logiques, des erreurs de syntaxe ou des problèmes de performance. Les IDE modernes ont des
   outils de débogage intégrés qui vous permettent de suivre l'exécution de votre code étape par étape et de voir
   comment les variables changent au fil du temps.

3. **Gestion de la mémoire** : La gestion de la mémoire est le processus de contrôle de l'allocation et de la libération
   de la mémoire utilisée par votre programme. Dans certains langages, comme C#, la gestion de la mémoire est
   automatique grâce au ramasse-miettes (garbage collector).

4. **Répétition** : La répétition est une technique de programmation qui consiste à exécuter une séquence d'instructions
   plusieurs fois. Les boucles sont souvent utilisées pour implémenter la répétition. En C#, il existe plusieurs types
   de boucles, notamment `for`, `while` et `do-while`.

5. **Condition** : Une condition est une expression qui peut être vraie ou fausse. Les conditions sont souvent utilisées
   pour prendre des décisions dans votre code. Par exemple, vous pouvez utiliser une instruction `if` pour exécuter une
   certaine action si une condition est vraie.

6. **Affichage** : L'affichage est le processus de présentation des données à l'utilisateur. En C#, vous pouvez utiliser
   la méthode `Console.WriteLine()` pour afficher du texte dans la console.

7. **Saisie** : La saisie est le processus de collecte des données de l'utilisateur. En C#, vous pouvez utiliser la
   méthode `Console.ReadLine()` pour lire une ligne de texte entrée par l'utilisateur.

8. **Calcul mathématique** : Les calculs mathématiques sont une partie importante de la programmation. En C#, vous
   pouvez effectuer des opérations arithmétiques telles que l'addition, la soustraction, la multiplication et la
   division en utilisant les opérateurs `+`, `-`, `*` et `/`. Vous pouvez également utiliser des fonctions mathématiques
   telles que `Math.Pow()` pour calculer des puissances et `Math.Sqrt()` pour calculer des racines carrées.

## Exemple

```csharp
using System;

class Program
{
    static void Main()
    {
        // Saisie
        Console.Write("Entrez un nombre : ");
        string input = Console.ReadLine();

        // Conversion de la saisie en nombre
        double number = Convert.ToDouble(input);

        // Calcul mathématique
        double squareRoot = Math.Sqrt(number);

        // Affichage
        Console.WriteLine("La racine carrée de " + number + " est " + squareRoot);

        // Répétition
        for (int i = 0; i < 10; i++)
        {
            // Condition
            if (i % 2 == 0)
            {
                Console.WriteLine(i + " est pair");
            }
            else
            {
                Console.WriteLine(i + " est impair");
            }
        }
    }
}
```

Ce code demande à l'utilisateur d'entrer un nombre, calcule sa racine carrée, puis affiche le résultat. Il utilise
ensuite une boucle `for` pour itérer de 0 à 9, et utilise une instruction `if` pour déterminer si chaque nombre est pair
ou impair.

## Types de données

En C#, il existe plusieurs types de données principaux qui sont utilisés pour stocker des valeurs dans les variables.
Les types de données les plus couramment utilisés en C# sont les suivants :

1. **Types numériques** : Les types numériques sont utilisés pour stocker des nombres entiers ou décimaux. Les types
   numériques les plus couramment utilisés en C# sont :
    * `int` : type entier signé de 32 bits.
    * `long` : type entier signé de 64 bits.
    * `float` : type flottant de 32 bits.
    * `double` : type flottant de 64 bits.
2. **Type booléen** : Le type booléen est utilisé pour stocker des valeurs de vérité, qui sont soit vraies (true) soit
   fausses (false). Le type booléen en C# est `bool`.
3. **Type char** : Le type char est utilisé pour stocker des caractères individuels. Le type char en C# est `char`.
4. **Type string** : Le type string est utilisé pour stocker des chaînes de caractères. Le type string en C#
   est `string`.
5. **Type DateTime** : Le type DateTime est utilisé pour stocker des dates et des heures. Le type DateTime en C#
   est `DateTime`.

Il est important de noter que chaque type de données a une plage de valeurs qu'il peut stocker. Par exemple, le
type `int` peut stocker des nombres entiers compris entre -2,147,483,648 et 2,147,483,647. Si vous essayez de stocker
une valeur en dehors de cette plage, vous obtiendrez une erreur de compilation.

En résumé, les types de données principaux en C# sont les types numériques, le type booléen, le type char, le type
string et le type DateTime. Chaque type de données a une plage de valeurs qu'il peut stocker, et il est important de
choisir le bon type de données pour chaque variable en fonction de ses besoins.

## Expressions

Une expression en C# est une construction syntaxique qui produit une valeur lorsqu'elle est évaluée. Les expressions
peuvent être constituées de littéraux, de variables, d'opérateurs, de méthodes et de fonctions.

Voici quelques exemples d'expressions en C# :

* `5 + 3` : Cette expression produit la valeur entière 8.
* `"Hello, World!"` : Cette expression produit une chaîne de caractères contenant le message "Hello, World!".
* `x * y` : Cette expression produit le résultat de la multiplication des valeurs des variables `x` et `y`.
* `Math.Sqrt(4)` : Cette expression produit la racine carrée de 4, qui est 2.
* `Console.ReadLine()` : Cette expression produit une chaîne de caractères contenant la ligne de texte entrée par
  l'utilisateur.

Les expressions peuvent être utilisées dans différents contextes en C#, tels que les instructions d'assignation, les
instructions de condition, les instructions de boucle et les appels de méthode. Par exemple, voici un exemple
d'utilisation d'une expression dans une instruction d'assignation :

```csharp
int x = 5;
int y = 3;
int z = x * y; // z est maintenant égal à 15
```

Dans cet exemple, l'expression `x * y` est utilisée pour calculer le produit des valeurs des variables `x` et `y`, et le
résultat est assigné à la variable `z`.

En résumé, une expression en C# est une construction syntaxique qui produit une valeur lorsqu'elle est évaluée. Les
expressions peuvent être constituées de littéraux, de variables, d'opérateurs, de méthodes et de fonctions, et elles
peuvent être utilisées dans différents contextes en C#.