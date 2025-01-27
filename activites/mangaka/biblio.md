# Bibliothèque

Reprendre [l’exercice Mangaka](README.md) en contextualisant sur des livres.

## Aide pour débuter

### Classe Book
Commencer par créer une classe Book :

```csharp
// Créons d'abord une classe Livre simple
public class Book
{
    public string Title;
    public string Author;
    public bool IsBorrowed = false;
}

```

Puis composer la bibliothèque :

### Bibliothèque
```csharp
//Liste des livres
List<Book> library = new();

// Ajout d’un livre
Book b1 = new Book();
b1.Title = "Les Misérables";
b1.Author = "Victor Hugo";

library.Add(b1);
```

Et enfin, afficher les livres

```csharp
// Afficher tous les livres
Console.WriteLine("Liste des livres dans la bibliothèque :");
foreach (Book book in library)
{
    Console.WriteLine($"- {book.Title} par {book.Author}");
}
```

## Reste à faire
- [ ] Reprendre les fonctionnalités de recherches et d’emprunt
- [ ] Passer en mode UI avec WinForms
