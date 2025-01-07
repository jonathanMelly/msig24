# Bibliothèque

Reprendre [l’exercice Mangaka](README.md) en contextualisant sur des livres.

## Aide pour débuter

### Classe Book
Commencer par créer une classe Book :

```csharp
// Créons d'abord une classe Livre simple
public class Book
{
    public string Title { get; set; }
    public string Author { get; set; }
    public bool IsBorrowed { get; set; }

    public Livre(string title, string author)
    {
        Title = title;
        Author = author;
        IsBorrowed = false;
    }
}

```

Puis composer la bibliothèque :

### Bibliothèque
```csharp
List<Book> library = new();
// Ajout de quelques livres
library.Add(new Book("Les Misérables", "Victor Hugo"));
library.Add(new Book("Le Petit Prince", "Antoine de Saint-Exupéry"));
library.Add(new Book("1984", "George Orwell"));
```

Et enfin, afficher les livres

```csharp
// Afficher tous les livres
Console.WriteLine("Liste des livres dans la bibliothèque :");
foreach (var book in library)
{
    Console.WriteLine($"- {book.Title} par {book.Author}");
}
```

## Reste à faire
- [ ] Reprendre les fonctionnalités de recherches et d’emprunt
- [ ] Passer en mode UI avec WinForms
