---
theme: default
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: true
# some information about the slides
info: |
  ## Découverte de Python
  Comparaison avec C# pour les développeurs
# active slide scale - réduire la taille du contenu pour qu'il tienne sur la slide
scale: 0.85
# enable slide-level transitions
transition: slide-left
# enable vertical slides with "---" separator
layout: default
---

# Découverte de Python
## Syntaxe et comparaison avec C#

---

# Table des matières

- Syntaxe générale et indentation
- Variables et types de données
- Conversion de types
- Conditions
- Boucles
- Types de base: int, float, string, list
- Entrées utilisateur (équivalent à ReadLine)

---

# Syntaxe générale et indentation

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# En Python, l'indentation définit les blocs
def fonction():
    if True:
        print("Indentation avec 4 espaces")
        for i in range(3):
            print(i)  # Encore 4 espaces
    
    # Retour au niveau précédent
    print("Fin de la fonction")
```

</div>
<div>

## C#
```csharp
// En C#, les accolades définissent les blocs
void Fonction()
{
    if (true)
    {
        Console.WriteLine("Blocs avec accolades");
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine(i);
        }
    }
    
    // Les accolades définissent la fin du bloc
    Console.WriteLine("Fin de la fonction");
}
```

</div>
</div>

---

# Variables et types de données

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Typage dynamique - pas besoin de déclarer le type
number = 42          # int
decimal = 3.14       # float
text = "Bonjour"    # str
liste = [1, 2, 3]    # list
dictionnaire = {"clé": "valeur"}  # dict
booleen = True       # bool

# Vérifier le type
print(type(number))  # <class 'int'>

# Python utilise le snake_case
my_number = 10
```

</div>
<div>

## C#
```csharp
// Typage statique - déclaration explicite du type
int number = 42;
double decimal = 3.14;
string text = "Bonjour";
List<int> liste = new List<int> { 1, 2, 3 };
Dictionary<string, string> dict = new Dictionary<string, string>
{
    { "clé", "valeur" }
};
bool booleen = true;

// Vérifier le type
Console.WriteLine(number.GetType());

// C# utilise le camelCase ou PascalCase
int monnumber = 10;
```

</div>
</div>

---

# Conversion de types

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Conversion explicite
number_str = "42"
number_int = int(number_str)  # 42
number_float = float(number_str)  # 42.0

# Conversion de float vers int (tronque la partie décimale)
x = int(3.9)  # 3

# Conversion en chaîne
number = 42
text = str(number)  # "42"

# Les listes peuvent être converties en d'autres collections
ma_liste = [1, 2, 3]
mon_tuple = tuple(ma_liste)  # (1, 2, 3)
mon_set = set(ma_liste)      # {1, 2, 3}
```

</div>
<div>

## C#
```csharp
// Conversion explicite
string numberStr = "42";
int numberInt = int.Parse(numberStr);  // ou Convert.ToInt32(numberStr)
double numberDouble = double.Parse(numberStr);

// Conversion de double vers int (tronque la partie décimale)
int x = (int)3.9;  // 3

// Conversion en chaîne
int number = 42;
string text = number.ToString();  // ou Convert.ToString(number)

// Les collections peuvent être converties
List<int> maListe = new List<int> { 1, 2, 3 };
int[] monTableau = maListe.ToArray();
HashSet<int> monSet = new HashSet<int>(maListe);
```

</div>
</div>

---

# Conditions

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Structure if-elif-else
age = 18

if age < 18:
    print("Mineur")
elif age == 18:
    print("Tout juste majeur")
else:
    print("Majeur")

# Opérateurs de comparaison: ==, !=, <, >, <=, >=
# Opérateurs logiques: and, or, not

# Condition ternaire
statut = "majeur" if age >= 18 else "mineur"

# Vérification d'appartenance
fruits = ["pomme", "banane", "orange"]
if "pomme" in fruits:
    print("La pomme est dans la liste")
```

</div>
<Transform :scale="0.8">
<div>

## C#
```csharp
// Structure if-else if-else
int age = 18;

if (age < 18)
{
    Console.WriteLine("Mineur");
}
else if (age == 18)
{
    Console.WriteLine("Tout juste majeur");
}
else
{
    Console.WriteLine("Majeur");
}

// Opérateurs de comparaison: ==, !=, <, >, <=, >=
// Opérateurs logiques: &&, ||, !

// Condition ternaire
string statut = age >= 18 ? "majeur" : "mineur";

// Vérification d'appartenance
List<string> fruits = new List<string> { "pomme", "banane", "orange" };
if (fruits.Contains("pomme"))
{
    Console.WriteLine("La pomme est dans la liste");
}
```

</div></Transform>
</div>

---

# Boucles (1/2)

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Boucle for avec range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Boucle for avec une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Boucle for avec index et valeur
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

</div>
<div>

## C#
```csharp
// Boucle for classique
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}

// Boucle foreach avec une liste
List<string> fruits = new List<string> { "pomme", "banane", "orange" };
foreach (string fruit in fruits)
{
    Console.WriteLine(fruit);
}

// Boucle for avec index et valeur
for (int i = 0; i < fruits.Count; i++)
{
    Console.WriteLine($"{i}: {fruits[i]}");
}
```

</div>
</div>

---

# Boucles (2/2)

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Boucle while
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# break et continue
for i in range(10):
    if i == 3:
        continue  # Passe à l'itération suivante
    if i == 7:
        break     # Sort de la boucle
    print(i)
    
# Compréhension de liste (spécifique à Python)
carrés = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
pairs = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

</div>
<div>

## C#
```csharp
// Boucle while
int compteur = 0;
while (compteur < 5)
{
    Console.WriteLine(compteur);
    compteur++;
}

// break et continue
for (int i = 0; i < 10; i++)
{
    if (i == 3)
        continue;  // Passe à l'itération suivante
    if (i == 7)
        break;     // Sort de la boucle
    Console.WriteLine(i);
}

// LINQ (équivalent C# des compréhensions)
var carrés = Enumerable.Range(1, 5).Select(x => x * x).ToList();
var pairs = Enumerable.Range(0, 10).Where(x => x % 2 == 0).ToList();
```

</div>
</div>

---

# Types de base: int, float (1/2)


<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Entiers (int) - précision illimitée
a = 42
b = 1000000000000000000000  # Pas de limite de taille

# Opérations de base
somme = a + b
difference = a - b
produit = a * b
quotient = a / b        # Division flottante (toujours)
quotient_entier = a // b  # Division entière
reste = a % b           # Modulo
puissance = a ** 2      # Puissance
```

</div>
<div>

## C#
```csharp
// Entiers - plusieurs types selon la taille
int a = 42;
long b = 1000000000000000000;  // Limité à 64 bits

// Opérations de base
var somme = a + b;
var difference = a - b;
var produit = a * b;
var quotient = (double)a / b;  // Division flottante
var quotientEntier = a / 5;    // Division entière si opérandes entiers
var reste = a % b;             // Modulo
var puissance = Math.Pow(a, 2);  // Puissance
```

</div>
</div>

---

# Types de base: int, float (2/2)

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# numbers à virgule flottante (float)
pi = 3.14159
e = 2.71828

# Fonctions mathématiques (module math)
import math
racine = math.sqrt(16)      # 4.0
sinus = math.sin(math.pi/2) # 1.0
cosinus = math.cos(0)       # 1.0
absolu = abs(-5)            # 5
plafond = math.ceil(3.1)    # 4
plancher = math.floor(3.9)  # 3
arrondi = round(3.5)        # 4

# numbers complexes
z = 1 + 2j
```

</div>
<div>

## C#
```csharp
// numbers à virgule flottante
double pi = 3.14159;
float e = 2.71828f;  // Suffixe f pour float
decimal prix = 19.99m;  // Suffixe m pour decimal

// Fonctions mathématiques (classe Math)
double racine = Math.Sqrt(16);      // 4.0
double sinus = Math.Sin(Math.PI/2); // 1.0
double cosinus = Math.Cos(0);       // 1.0
int absolu = Math.Abs(-5);          // 5
double plafond = Math.Ceiling(3.1); // 4.0
double plancher = Math.Floor(3.9);  // 3.0
int arrondi = (int)Math.Round(3.5); // 4

// numbers complexes
Complex z = new Complex(1, 2);  // Namespace System.Numerics
```

</div>
</div>

---

# Types de base: string

<Transform :scale="0.85">
<div class="grid grid-cols-2 gap-2">
<div>

## Python
```python
# Chaînes de caractères (str)
text = "Hello, World!"
text_simple = 'Avec guillemets simples'
text_multiple = """Chaîne
sur plusieurs
lignes"""

# Formatage
name = "Alice"
age = 30
greet = f"Je suis {name} et j'ai {age} ans."

# Méthodes courantes
longueur = len(text)  # 13
majuscules = text.upper()
minuscules = text.lower()
replaced = text.replace("Hello", "Bonjour")

# Accès aux caractères (indexation)
first = text[0]  # 'H'
last = text[-1]  # '!'
sous_chaîne = text[0:5]  # 'Hello'

# Vérifications
start = text.startswith("Hello")  # True
contains = "World" in text  # True
```

</div>
<div>

## C#
```csharp
// Chaînes de caractères (string)
string text = "Hello, World!";
string textSimple = "Avec guillemets doubles";
string textMultiple = @"Chaîne
sur plusieurs
lignes";

// Formatage
string name = "Alice";
int age = 30;
string greet = $"Je suis {name} et j'ai {age} ans.";

// Méthodes courantes
int longueur = text.Length;  // 13
string majuscules = text.ToUpper();
string minuscules = text.ToLower();
string replaced = text.Replace("Hello", "Bonjour");

// Accès aux caractères
char first = text[0];  // 'H'
char last = text[text.Length - 1];  // '!'
string substring = text.Substring(0, 5); //'Hello'

// Vérifications
bool start = text.StartsWith("Hello");  // true
bool contains = text.Contains("World");  // true
```

</div>
</div></Transform>

---

# Types de base: list

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Listes (list) - collection ordonnée, modifiable
numbers = [1, 2, 3, 4, 5]
mixte = [1, "deux", 3.0, [4, 5]]  # Types différents possibles

# Création
vide = []
liste_range = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Accès et modification
first = numbers[0]  # 1
last = numbers[-1]  # 5
numbers[0] = 10  # Modification

# Slicing (tranches)
sous_liste = numbers[1:4]  # [2, 3, 4]

# Méthodes courantes
numbers.append(6)  # Ajoute à la fin
numbers.insert(0, 0)  # Insère au début
numbers.remove(3)  # Supprime la première occurrence de 3
last = numbers.pop()  # Supprime et retourne le last
longueur = len(numbers)  # Taille de la liste
```

</div>
<div>

## C#
```csharp
// Listes (List<T>) - collection ordonnée, modifiable, typée
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
// C# impose un type unique pour chaque liste

// Création
List<int> vide = new List<int>();
List<int> listeRange = Enumerable.Range(1, 5).ToList();

// Accès et modification
int first = numbers[0];  // 1
int last = numbers[numbers.Count - 1];  // 5
numbers[0] = 10;  // Modification

// Sous-listes
List<int> sousListe = numbers.GetRange(1, 3);  // [2, 3, 4]

// Méthodes courantes
numbers.Add(6);  // Ajoute à la fin
numbers.Insert(0, 0);  // Insère au début
numbers.Remove(3);  // Supprime la première occurrence de 3
last = numbers[numbers.Count - 1];  // Pas d'équivalent direct à pop()
numbers.RemoveAt(numbers.Count - 1);  // Supprime le last
int longueur = numbers.Count;  // Taille de la liste
```

</div>
</div>

---

# Entrées utilisateur (équivalent à ReadLine) (1/2)

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Lecture d'une entrée utilisateur
name = input("Entrez votre name: ")
print(f"Bonjour, {name}!")

# Lecture et conversion
try:
    age = int(input("Entrez votre âge: "))
    print(f"Dans 10 ans, vous aurez {age + 10} ans.")
except ValueError:
    print("Erreur: Veuillez entrer un number entier.")
```

</div>
<div>

## C#
```csharp
// Lecture d'une entrée utilisateur
Console.Write("Entrez votre name: ");
string name = Console.ReadLine();
Console.WriteLine($"Bonjour, {name}!");

// Lecture et conversion
Console.Write("Entrez votre âge: ");
try
{
    int age = int.Parse(Console.ReadLine());
    Console.WriteLine($"Dans 10 ans, vous aurez {age + 10} ans.");
}
catch (FormatException)
{
    Console.WriteLine("Erreur: Veuillez entrer un number entier.");
}
```

</div>
</div>

---

# Entrées utilisateur (équivalent à ReadLine) (2/2)

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Lecture de plusieurs valeurs sur une même ligne
# "1 2 3" -> ["1", "2", "3"]
valeurs = input("Entrez des valeurs séparées par des espaces: ").split()

# Conversion des valeurs en entiers
numbers = [int(val) for val in valeurs]
print(f"La somme est: {sum(numbers)}")

# Autre exemple avec map
numbers = list(map(int, input("Entrez des numbers: ").split()))

# Lecture de fichier (alternative à l'entrée utilisateur)
with open("donnees.txt", "r") as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        print(ligne.strip())
```

</div>
<div>

## C#
```csharp
// Lecture de plusieurs valeurs sur une même ligne
Console.Write("Entrez des valeurs séparées par des espaces: ");
string[] valeurs = Console.ReadLine().Split(' ');

// Conversion des valeurs en entiers
List<int> numbers = valeurs.Select(int.Parse).ToList();
Console.WriteLine($"La somme est: {numbers.Sum()}");

// Autre exemple avec Array.ConvertAll
int[] numbers2 = Array.ConvertAll(
    Console.ReadLine().Split(), int.Parse);

// Lecture de fichier (alternative à l'entrée utilisateur)
string[] lignes = File.ReadAllLines("donnees.txt");
foreach (string ligne in lignes)
{
    Console.WriteLine(ligne);
}
```

</div>
</div>

---

# Résumé des differences clés

<div class="grid grid-cols-2 gap-4">
<div>

## Python
```python
# Caractéristiques principales
- Indentation pour les blocs de code
- Typage dynamique (pas de déclaration de type)
- Syntaxe simple et lisible
- Les listes peuvent contenir différents types
- `snake_case` pour les names de variables
- Division entière avec //
- Compréhensions de liste
- Bibliothèque standard riche
```

</div>
<div>

## C#
```csharp
// Caractéristiques principales
// Accolades pour les blocs de code
// Typage statique (déclaration explicite)
// Syntaxe plus verbeuse
// Collections fortement typées
// camelCase ou PascalCase pour les variables
// Division entière implicite entre entiers
// LINQ pour les collections
// Écosystème .NET
```

</div>
</div>

---

# Tableau comparatif

| Fonctionnalité       | Python                       | C#                        |
|----------------------|------------------------------|-----------------------------|
| Extension de fichier | .py                          | .cs                         |
| Blocs de code        | Indentation                  | Accolades {}                |
| Typage               | Dynamique                    | Statique                    |
| Syntaxe              | Simple                       | Plus verbeuse               |
| Lectures utilisateur | `input()`                    | `Console.ReadLine()`        |
| Affichage            | `print()`                    | `Console.WriteLine()`       |
| Collections          | `list`, `tuple`, `dict`, etc.| `List<T>`, `Dictionary<K,V>`|
| Style de nommage     | `snake_case`                 | `camelCase`, `PascalCase`   |

---

# Ressources d'apprentissage

- Documentation officielle Python: [docs.python.org](https://docs.python.org)
- Documentation officielle C#: [docs.microsoft.com/dotnet/csharp](https://learn.microsoft.com/dotnet/csharp)
- Python pour les développeurs .NET: [Microsoft Learn](https://learn.microsoft.com/visualstudio/python)
- Tutoriels interactifs: [Python Tutor](https://pythontutor.com/)
- Environnements en ligne: [Replit](https://replit.com/), [Google Colab](https://colab.research.google.com/) (Python)

---

# Exercices pratiques

1. Créez une fonction qui calcule la factorielle d'un number
2. Implémentez un programme qui inverse une chaîne de caractères
3. Écrivez un algorithme pour trier une liste de nombres
4. Développez une classe `Personne` avec des propriétés et méthodes
5. Lisez un fichier text et comptez les occurrences de chaque mot

---

# Merci !

## Questions ?

```python
print("À bientôt !")
```

```csharp
Console.WriteLine("À bientôt !");
```