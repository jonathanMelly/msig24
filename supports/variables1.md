# Gestion mémoire en C#

## Variables

Une variable est un espace mémoire qui stocke une valeur. En C#, nous devons déclarer une variable avant de pouvoir
l'utiliser. Pour déclarer une variable, nous devons spécifier son type et lui donner un nom. Voici un exemple :

```csharp
int nombre;
```

Dans cet exemple, nous avons déclaré une variable de type `int` appelée `nombre`. Nous pouvons maintenant utiliser cette
variable pour stocker une valeur entière.

## Types

En C#, il existe plusieurs types de données que nous pouvons utiliser pour stocker des valeurs dans des variables. Voici
quelques exemples de types de données :

* `int` : type entier qui peut stocker des valeurs entières entre -2,147,483,648 et 2,147,483,647.
* `float` : type à virgule flottante qui peut stocker des valeurs décimales entre -3,4 \* 10^38 et 3,4 \* 10^38.
* `bool` : type booléen qui peut stocker les valeurs `true` ou `false`.
* `string` : type chaîne de caractères qui peut stocker des séquences de caractères.

Voici un exemple de déclaration de variables avec différents types :

```csharp
int nombreEntier = 42;
float nombreDecimal = 3.14f;
bool estVrai = true;
string message = "Bonjour, monde !";
```

Dans cet exemple, nous avons déclaré quatre variables avec différents types. Nous avons également affecté une valeur à
chaque variable.

## Valeurs par défaut

Lorsque nous déclarons une variable en C#, elle est initialisée avec une valeur par défaut. La valeur par défaut dépend
du type de la variable. Voici les valeurs par défaut pour les types de base en C# :

* `int` : 0
* `float` : 0.0f
* `bool` : false
* `string` : null

Notez que pour les types référence (comme `string`), la valeur par défaut est `null`. Cela signifie que la variable ne
pointe vers aucun objet.

Il est important de noter que les valeurs par défaut ne sont pas toujours appropriées pour nos programmes. Par exemple,
si nous voulons stocker un nombre entier qui représente l'âge d'une personne, nous ne voulons probablement pas que la
valeur par défaut soit 0. Dans ce cas, nous devons initialiser la variable avec une valeur appropriée.

Voici un exemple de déclaration de variables avec des valeurs par défaut :

```csharp
int nombreEntier; // valeur par défaut : 0
float nombreDecimal; // valeur par défaut : 0.0f
bool estVrai; // valeur par défaut : false
string message; // valeur par défaut : null
```

Dans cet exemple, nous avons déclaré quatre variables avec des types différents. Notez que nous n'avons pas affecté de
valeur à ces variables, donc elles ont été initialisées avec leurs valeurs par défaut.

## Exemples

Voici quelques exemples pour illustrer l'utilisation des variables et des types en C# :

Dans cet exemple, nous avons déclaré une constante `PI` de type `float` avec la valeur 3,14. Nous avons également
déclaré deux variables `rayon` et `surface` de type `float`. Nous demandons à l'utilisateur d'entrer le rayon du cercle,
puis nous calculons la surface du cercle en utilisant la formule `PI * rayon * rayon`. Nous affichons ensuite la surface
du cercle dans la console.

