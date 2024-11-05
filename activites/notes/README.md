# Notes

## Version 1

Écrire un programme permettant de calculer la moyenne de trois notes comprises entre 1 et 6. Le programme doit
demander à l'utilisateur de saisir les trois notes, vérifier que chaque note est bien un nombre compris dans cet
intervalle, puis calculer et afficher la moyenne de ces trois notes.

**Exemple de fonctionnement attendu :**

- Saisir la note n°1 : `5`
- Saisir la note n°2 : `4`
- Saisir la note n°3 : `3`
- Résultat attendu : La moyenne des notes est `4.00`.

### Contraintes
- Chaque note doit être un nombre compris entre 1 et 6.

## Version 2
- Contrôler que la note saisie soit au demi point
<details><summary>Aide</summary>

Une note arrondie au demi-point, multipliée par deux, donne toujours un nombre entier...
Pour vérifier si un nombre est entier, on peut comparer avec sa valeur entière :

```csharp
double grade = 5.5;
int gradeInt = (int) grade; //Réduit la note à sa valeur entière
bool matches = grade == gradeInt; //Ici false car 5.5 est différent de 5
```

</details>

## Version 3
- Arrondir la moyenne au demi-point

<details><summary>Aide</summary>
Pour arrondir un nombre au demi-point (0.5), vous pouvez multiplier le nombre par 2, l'arrondir à l'entier le plus 
proche, puis le diviser par 2. Voici comment faire cela en C# :

```csharp
double nombre = 3.76;

// Arrondir au demi-point le plus proche
double arrondi = Math.Round(nombre * 2) / 2;

Console.WriteLine(arrondi); // Affiche "3.5"
```

### Explication
1. Multiplier le nombre par 2.
2. Utiliser `Math.Round` pour arrondir le résultat à l'entier le plus proche.
3. Diviser par 2 pour revenir à l'échelle initiale avec un arrondi au demi-point.

</details>

## Version 4
- Contrôler la saisie (pas de texte)

[Voir ici pour l’aide](../../supports/input-output-random.md#contrôle-de-conversion)

## Version 5
- Nombre de notes variables

Tant que l’utilisateur rentre des notes, on les ajoute.

> Il faut donc définir une manière pour que l’utilisateur puisse indiquer que c’est la dernière...


## Version 6
- Sauver les notes et la moyenne dans un fichier

[Aide](../../supports/file.md)

## Aide générale
<details>
<summary>Proposition de solution intermédiaire</summary>

```csharp
using System;

public class Program
{
    public static void Main()
    {
        Console.Write("Combien de notes souhaitez-vous saisir ? ");
        int nombreNotes;
        
        // Validation de la saisie du nombre de notes
        while (!int.TryParse(Console.ReadLine(), out nombreNotes) || nombreNotes <= 0)
        {
            Console.WriteLine("Entrée invalide. Veuillez saisir un nombre entier positif.");
            Console.Write("Combien de notes souhaitez-vous saisir ? ");
        }

        double sommeNotes = 0;
        int compteur = 0;

        while (compteur < nombreNotes)
        {
            Console.Write($"Saisir la note n°{compteur + 1} (entre 1 et 6) : ");
            double note;

            // Validation de la saisie de la note
            while (!double.TryParse(Console.ReadLine(), out note) || note < 1 || note > 6)
            {
                Console.WriteLine("Entrée invalide. Veuillez saisir une note entre 1 et 6.");
                Console.Write($"Saisir la note n°{compteur + 1} (entre 1 et 6) : ");
            }

            // Ajout de la note à la somme totale et incrément du compteur
            sommeNotes += note;
            compteur++;
        }

        // Calcul de la moyenne
        double moyenne = sommeNotes / nombreNotes;

        // Affichage de la moyenne
        Console.WriteLine($"La moyenne des notes est {moyenne:F2}");
    }
}
```

</details>