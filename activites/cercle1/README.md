# Calcul de la surface d'un cercle

## Rappel

Pour calculer la surface d'un cercle, on multiplie son rayon au carré par PI.

## Objectif

- Demander à l'utilisateur le rayon
- Calculer la surface
- Afficher le résultat

<details><summary>Proposition de solution</summary>

```csharp
const float PI = 3.14f;
float rayon;
float surface;

Console.Write("Entrez le rayon du cercle : ");
rayon = Convert.ToSingle(Console.ReadLine());

surface = PI * rayon * rayon;

Console.WriteLine($"La surface du cercle est : {surface}");
Console.ReadKey();
```

</details>