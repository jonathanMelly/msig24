# Persistence

En C#, les méthodes `File.ReadAllText` et `File.ReadAllLines` offrent deux approches pratiques pour lire des données à
partir d'un fichier. Voici comment les utiliser pour sauvegarder et charger des données de manière simple et
contextuelle.

## File.WriteAllText : Sauvegarder des données dans un fichier

Avant de charger des données, il faut d’abord les sauvegarder. `File.WriteAllText` permet de sauvegarder une chaîne de
texte dans un fichier en remplaçant tout le contenu existant.

### Exemple de sauvegarde

Supposons que vous vouliez sauvegarder une liste de noms avec des retours de ligne entre chaque nom.

```csharp
using System.IO;

string chemin = "noms.txt";
string contenu = "Alice\nBob\nCharlie\nDavid";

// Sauvegarder la chaîne dans le fichier
File.WriteAllText(chemin, contenu);

Console.WriteLine("Les noms ont été sauvegardés dans le fichier.");
```

- **Explication** : Le texte `"Alice\nBob\nCharlie\nDavid"` contient des retours de ligne (`\n`) pour que chaque nom
  soit écrit sur une ligne distincte dans le fichier. `File.WriteAllText` sauvegarde ce contenu dans `noms.txt`,
  écrasant tout contenu existant.

## File.ReadAllText : Charger l'intégralité d'un fichier en une seule chaîne

La méthode `File.ReadAllText` lit tout le contenu d’un fichier en une seule chaîne de texte. Elle est utile si vous avez
un petit fichier ou si vous n'avez pas besoin de traiter ligne par ligne.

### Exemple de chargement avec `File.ReadAllText`

```csharp
// Lire tout le contenu du fichier dans une seule chaîne
string contenu = File.ReadAllText(chemin);

Console.WriteLine("Contenu du fichier :");
Console.WriteLine(contenu);
```

- **Explication** : `File.ReadAllText` lit tout le texte dans `noms.txt` et l'affiche. Les retours de ligne présents
  dans le fichier sont également chargés dans la chaîne.

#### Utilisation de `Split` avec `ReadAllText`

Si vous avez besoin d’un tableau où chaque ligne est un élément, vous pouvez utiliser `Split` pour diviser la chaîne en
utilisant les retours de ligne.

```csharp
string[] noms = contenu.Split(new[] { '\n' }, StringSplitOptions.RemoveEmptyEntries);

Console.WriteLine("Noms chargés depuis le fichier :");
foreach (string nom in noms)
{
    Console.WriteLine(nom);
}
```

- **Explication** : `contenu.Split(new[] { '\n' }, StringSplitOptions.RemoveEmptyEntries)` divise la chaîne en un
  tableau, où chaque nom est un élément distinct. `StringSplitOptions.RemoveEmptyEntries` évite d'inclure des lignes
  vides.

## File.ReadAllLines : Charger un fichier ligne par ligne

La méthode `File.ReadAllLines` lit le fichier ligne par ligne et renvoie chaque ligne sous forme de tableau de chaînes.
Elle est particulièrement utile si vous devez traiter chaque ligne individuellement.

### Exemple de chargement avec `File.ReadAllLines`

```csharp
// Lire toutes les lignes du fichier dans un tableau de chaînes
string[] lignes = File.ReadAllLines(chemin);

Console.WriteLine("Noms chargés depuis le fichier (ligne par ligne) :");
foreach (string ligne in lignes)
{
    Console.WriteLine(ligne);
}
```

- **Explication** : `File.ReadAllLines` charge chaque ligne du fichier dans un tableau. Chaque élément du tableau
  correspond à une ligne du fichier, sans inclure les retours de ligne. Cela permet de traiter chaque ligne
  indépendamment.

### Comparaison entre `File.ReadAllText` et `File.ReadAllLines`

| Méthode             | Résultat                                  | Quand l’utiliser                                                                   |
|---------------------|-------------------------------------------|------------------------------------------------------------------------------------|
| `File.ReadAllText`  | Chaîne unique contenant tout le contenu   | Pour lire tout le fichier d’un seul coup, sans traitement ligne par ligne          |
| `File.ReadAllLines` | Tableau de chaînes, une ligne par élément | Pour traiter chaque ligne individuellement, sans avoir à faire de découpage manuel |

### Exemple complet : Sauvegarde et chargement

Voici un exemple complet avec `File.WriteAllText` pour la sauvegarde et les deux méthodes de lecture pour le chargement.

```csharp
using System;
using System.IO;

string chemin = "noms.txt";

// Sauvegarder une liste de noms avec des retours de ligne
string[] noms = { "Alice", "Bob", "Charlie", "David" };
File.WriteAllText(chemin, string.Join(Environment.NewLine, noms));

Console.WriteLine("Les noms ont été sauvegardés dans le fichier.");

// Charger le fichier avec ReadAllText
string contenu = File.ReadAllText(chemin);
Console.WriteLine("\nChargement avec ReadAllText :");
Console.WriteLine(contenu);

// Charger le fichier avec ReadAllLines
string[] lignes = File.ReadAllLines(chemin);
Console.WriteLine("\nChargement avec ReadAllLines (ligne par ligne) :");
foreach (string ligne in lignes)
{
    Console.WriteLine(ligne);
}
```

### Résumé

- **Sauvegarder** : `File.WriteAllText` sauvegarde tout le contenu d’un fichier, en remplaçant le contenu existant.
- **Charger en une chaîne** : `File.ReadAllText` lit tout le fichier en une seule chaîne.
- **Charger en un tableau de lignes** : `File.ReadAllLines` lit le fichier ligne par ligne dans un tableau de chaînes.

Ces méthodes sont pratiques pour travailler avec des fichiers de texte simples dans des applications C#.

## Append
Les fonctions `Write` ont pour effet d’écraser le contenu précédent du fichier. Il existe les alternatives nommées
`AppendAllText` et `AppendAllLines` pour ajouter du contenu sans effacer l’existant...