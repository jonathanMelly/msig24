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
* `double`: type à virgule flottante sur 64bits
* `decimal`: type à virgule fixe
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

## Portée

En C#, la portée d'une variable est définie par le bloc de code dans lequel elle est déclarée. La portée d'une variable
détermine où cette variable peut être utilisée dans le code. Voici les différents types de portée en C# avec des
exemples pour illustrer chaque type.

### 1. **Portée des variables locales**

Les variables locales sont déclarées dans un bloc de code (entre deux accolades). Elles
ne sont accessibles que dans ce bloc.

```csharp

int x = 10; // variable locale

if (x > 5)
{
    int y = 20; // variable locale à l'intérieur du bloc if
    Console.WriteLine(x); // Accessible car x est déclarée dans le bloc parent
    Console.WriteLine(y); // Accessible dans ce bloc
}

// Console.WriteLine(y); // Erreur : y n'est pas accessible en dehors du bloc if

```

Dans cet exemple, `x` est déclarée dans le bloc et est accessible partout à partir de sa déclaration. Par contre,
`y` est déclarée dans le bloc `if` et n'est accessible que dans ce bloc.

Ici, `compteur` est une variable d'instance qui est accessible dans toutes les méthodes de la classe `ExempleClasse`.

### 2. **Portée des variables dans des boucles**

Les variables déclarées dans des boucles (comme `for`, `while`, etc.) ne sont accessibles que dans le bloc de la boucle.

```csharp

for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i); // i est accessible dans la boucle
}

// Console.WriteLine(i); // Erreur : i n'est pas accessible en dehors de la boucle

```

Dans cet exemple, `i` est une variable locale à la boucle `for` et ne peut pas être utilisée en dehors de celle-ci.

### 3. **Portée des variables avec des blocs imbriqués**

Chaque bloc crée une nouvelle portée. Une variable déclarée dans un bloc n'est accessible que dans ce bloc et dans les
blocs qui lui sont imbriqués.

```csharp

int x = 100; // portée dans la méthode

{
    int y = 200; // portée dans ce bloc
    Console.WriteLine(x); // Accessible car x est déclarée dans un bloc parent
    Console.WriteLine(y); // Accessible dans ce bloc
}

// Console.WriteLine(y); // Erreur : y n'est pas accessible ici

```

Dans cet exemple, `x` est accessible dans toute la méthode, mais `y` n'est accessible que dans le bloc où elle a été
déclarée.

### Règle importante

Les variables déclarées dans un bloc imbriqué ne peuvent pas masquer les variables de même nom dans un bloc parent.
Cependant, dans des cas exceptionnels, il est possible d'utiliser des variables de même nom si elles sont dans des blocs
différents, mais cela est déconseillé pour éviter la confusion.

**En général, la portée d'une variable en C# est déterminée par les accolades `{}` dans lesquelles elle est déclarée.**

