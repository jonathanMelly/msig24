# Logique et conditions

La logique et les conditions sont des concepts fondamentaux en programmation. Ils permettent aux programmes de prendre
des décisions basées sur des informations spécifiques.

## Première approche

Imaginez que vous êtes un chef cuisinier dans un restaurant. Vous
avez besoin de savoir si vous avez suffisamment d'ingrédients pour préparer un plat particulier. Si vous avez tous les
ingrédients, vous pouvez commencer à cuisiner. Sinon, vous devez commander plus d'ingrédients.

En programmation, nous utilisons des conditions pour faire des choix similaires. Une condition est une expression qui
peut être vraie ou fausse. 

Nous pouvons utiliser des **opérateurs de comparaison** tels que 
- `==` : est égal à
- `!=` : est différent de
- `<`  : est plus petit que
- `>`  : est plus grand que
- `<=` : est plus petit ou égal à
et `>=`: est plus grand ou égal à 

pour comparer des valeurs et déterminer si une condition est vraie ou fausse.

Il est aussi important de connaître les opérateurs unaires :

- `+` : comme en mathématiques, indique un nombre positif
- `-` : comme en mathématiques, indique un nombre négatif
- `!` : indique la négation pour un élément booléen 

### Exemple: Majeur ?

Par exemple, supposons que nous avons une variable `age` qui contient l'âge d'une personne. Nous pouvons utiliser une
condition pour déterminer si cette personne est majeure ou mineure. Voici un exemple de code C# qui illustre cela :

```csharp
using System;

class Program
{
    static void Main()
    {
        // Saisie
        Console.Write("Entrez votre âge : ");
        string input = Console.ReadLine();

        // Conversion de la saisie en nombre
        int age = Convert.ToInt32(input);

        // Condition
        if (age >= 18)
        {
            Console.WriteLine("Vous êtes majeur.");
        }
        else
        {
            Console.WriteLine("Vous êtes mineur.");
        }
    }
}
```

Dans cet exemple, nous demandons à l'utilisateur d'entrer son âge, puis nous utilisons une instruction `if` pour
déterminer s'il est majeur ou mineur. Si l'âge est supérieur ou égal à 18, nous affichons "Vous êtes majeur.". Sinon,
nous affichons "Vous êtes mineur.".

### Exemple : Permis de conduire

Nous pouvons également utiliser des opérateurs logiques tels que `&&` (et), `||` (ou) et `!` (non) pour combiner des
conditions. Par exemple, supposons que nous avons deux variables `hasCar` et `hasLicense` qui indiquent si une personne
possède une voiture et un permis de conduire, respectivement. Nous pouvons utiliser une condition pour déterminer si
cette personne peut conduire. Voici un exemple de code C# qui illustre cela :

```csharp
using System;

class Program
{
    static void Main()
    {
        // Saisie
        Console.Write("Avez-vous une voiture ? (oui/non) : ");
        bool hasCar = Console.ReadLine().ToLower() == "oui";

        Console.Write("Avez-vous un permis de conduire ? (oui/non) : ");
        bool hasLicense = Console.ReadLine().ToLower() == "oui";

        // Condition
        if (hasCar && hasLicense)
        {
            Console.WriteLine("Vous pouvez conduire.");
        }
        else
        {
            Console.WriteLine("Vous ne pouvez pas conduire.");
        }
    }
}
```

Dans cet exemple, nous demandons à l'utilisateur s'il possède une voiture et un permis de conduire, puis nous utilisons
une instruction `if` pour déterminer s'il peut conduire. Si l'utilisateur a une voiture et un permis de conduire, nous
affichons "Vous pouvez conduire.". Sinon, nous affichons "Vous ne pouvez pas conduire.".

En résumé, les conditions sont un moyen puissant de faire des choix dans votre code. Elles vous permettent de créer des
programmes qui peuvent s'adapter à différentes situations et prendre des décisions en fonction des informations
disponibles.

## Logique booléenne

La logique booléenne est une branche de la logique mathématique qui traite des valeurs de vérité, qui sont soit vraies (
true) soit fausses (false). Elle est utilisée en programmation pour représenter des états binaires et pour effectuer des
opérations logiques sur ces états.

Les opérateurs logiques booléens sont utilisés pour combiner des expressions booléennes et produire une nouvelle
expression booléenne. Les opérateurs logiques booléens les plus courants sont :

* `&&` (ET) : retourne true si toutes les expressions sont vraies.
* `||` (OU) : retourne true si au moins une des expressions est vraie.
* `!` (NON) : retourne l'opposé de la valeur de l'expression.

Voici un exemple de code C# qui illustre l'utilisation de ces opérateurs :

```csharp
using System;

class Program
{
    static void Main()
    {
        bool a = true;
        bool b = false;

        // ET
        Console.WriteLine(a && b); // Affiche False

        // OU
        Console.WriteLine(a || b); // Affiche True

        // NON
        Console.WriteLine(!a); // Affiche False
    }
}
```

Dans cet exemple, nous avons deux variables booléennes `a` et `b`. Nous utilisons les opérateurs `&&`, `||` et `!` pour
combiner ces variables et produire de nouvelles expressions booléennes.

Les tables de vérité sont un moyen utile de visualiser les résultats des opérations logiques booléennes. Voici les
tables de vérité pour les opérateurs `&&`, `||` et `!` :

| a | b | a && b |
|---|---|--------|
| T | T | T      |
| T | F | F      |
| F | T | F      |
| F | F | F      |

| a | b | a \|\| b |
|---|---|----------|
| T | T | T        |
| T | F | T        |
| F | T | T        |
| F | F | F        |

| a | !a |
|---|----|
| T | F  |
| F | T  |

Dans ces tables, `T` signifie true et `F` signifie false. Les colonnes `a` et `b` représentent les valeurs des variables
booléennes, et les colonnes `a && b`, `a || b` et `!a` représentent les résultats des opérations logiques booléennes
correspondantes.

En résumé, la logique booléenne est un concept important en programmation qui permet de représenter des états binaires
et d'effectuer des opérations logiques sur ces états. Les opérateurs logiques booléens les plus courants sont `&&`, `||`
et `!`, et les tables de vérité sont un moyen utile de visualiser les résultats de ces opérations.

### Simplifications

Pour simplifier une expression booléenne en algèbre de Boole, vous pouvez utiliser les lois de l'algèbre de Boole et les
propriétés des opérateurs logiques. Voici quelques conseils pour simplifier une expression booléenne :

1. Utilisez les lois de l'algèbre de Boole pour simplifier les expressions. Par exemple, vous pouvez utiliser la loi de
   commutativité pour interchanger les termes d'une expression, ou la loi d'associativité pour regrouper les termes
   d'une expression.
2. Utilisez les propriétés des opérateurs logiques pour simplifier les expressions. Par exemple, vous pouvez utiliser la
   propriété de distributivité pour distribuer un opérateur sur les termes d'une expression, ou la propriété
   d'idempotence pour simplifier les expressions qui contiennent des termes identiques.
3. Utilisez les tables de vérité pour simplifier les expressions. Les tables de vérité vous permettent de visualiser les
   résultats des opérations logiques et de simplifier les expressions en conséquence.
4. Utilisez les techniques de factorisation pour simplifier les expressions. La factorisation consiste à extraire un
   facteur commun des termes d'une expression et à le mettre en évidence.
5. Utilisez les techniques de substitution pour simplifier les expressions. La substitution consiste à remplacer une
   expression par une autre expression équivalente.

Voici un exemple de simplification d'une expression booléenne en utilisant les lois de l'algèbre de Boole et les
propriétés des opérateurs logiques :

Expression initiale : `(a && b) || (!a && !b)`

Utilisation de la loi de distributivité : `(a || !a) && (b || !b)`

Utilisation de la propriété d'idempotence : `(a || !a) && (b || !b)`

Simplification : `true && true`

Résultat final : `true`

#### Algèbre de bool avec exemples

Voici un exemple pour chaque loi de l'algèbre de Boole :

1. Loi de commutativité : `a && b = b && a` et `a || b = b || a`. 
   Exemple : `(2 > 1) && (3 > 2) = (3 > 2) && (2 > 1)`.
2. Loi d'associativité : `(a && b) && c = a && (b && c)` et `(a || b) || c = a || (b || c)`.
   Exemple : `((2 > 1) && (3 > 2)) && (4 > 3) = (2 > 1) && ((3 > 2) && (4 > 3))`.
3. Loi de distributivité : `a && (b || c) = (a && b) || (a && c)` et `a || (b && c) = (a || b) && (a || c)`.
   Exemple : `(2 > 1) && ((3 > 2) || (4 > 3)) = ((2 > 1) && (3 > 2)) || ((2 > 1) && (4 > 3))`.
4. Loi d'identité : `a && true = a` et `a || false = a`. Exemple : `(2 > 1) && true = (2 > 1)`.
5. Loi de complémentarité : `a && !a = false` et `a || !a = true`. Exemple : `(2 > 1) && !(2 > 1) = false`.
6. Loi de double négation : `!!a = a`. Exemple : `!!(2 > 1) = (2 > 1)`.
7. Loi de De Morgan : `!(a && b) = !a || !b` et `!(a || b) = !a && !b`.
   Exemple : `!(2 > 1) && !(3 > 2) = !(2 > 1 || 3 > 2)`.
8. Loi d'absorption : `a && (a || b) = a` et `a || (a && b) = a`. Exemple : `(2 > 1) && ((2 > 1) || (3 > 2)) = (2 > 1)`.
9. Loi de consensus : `(a && b) || (a && !b) || (!a && b) = a || b`.
   Exemple : `(2 > 1) && (3 > 2) || (2 > 1) && !(3 > 2) || !(2 > 1) && (3 > 2) = (2 > 1) || (3 > 2)`.
10. Loi de redondance : `a && (a || b) = a` et `a || (a && b) = a`.
    Exemple : `(2 > 1) && ((2 > 1) || (3 > 2)) = (2 > 1)`.
