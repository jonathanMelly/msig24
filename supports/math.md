# Utilitaires mathématiques

La bibliothèque `Math` en C# propose une large gamme de fonctions mathématiques utiles pour effectuer des calculs
numériques courants. Voici un aperçu des fonctions les plus importantes avec des exemples pratiques pour comprendre leur
utilisation.

### 1. **Math.Min** et **Math.Max**

Ces fonctions permettent de trouver respectivement la valeur minimale et la valeur maximale entre deux nombres.

```csharp
int minValue = Math.Min(5, 10); // Renvoie 5
int maxValue = Math.Max(5, 10); // Renvoie 10
```

### 2. **Math.Round**

`Math.Round` arrondit un nombre décimal au plus proche entier ou au nombre de décimales spécifié.

```csharp
double value = 4.567;
double roundedValue = Math.Round(value); // Renvoie 5
double roundedToTwoDecimals = Math.Round(value, 2); // Renvoie 4.57
```

### 3. **Math.PI**

La constante `Math.PI` représente la valeur de π (pi), utile pour les calculs trigonométriques.

```csharp
double circleCircumference = 2 * Math.PI * radius;
```

### 4. **Math.Pow**

`Math.Pow` permet de calculer la puissance d’un nombre. Elle prend deux arguments : le nombre de base et l'exposant.

```csharp
double power = Math.Pow(2, 3); // Renvoie 8, car 2^3 = 8
```

### 5. **Math.Sqrt**

Cette fonction retourne la racine carrée d'un nombre.

```csharp
double squareRoot = Math.Sqrt(16); // Renvoie 4
```

### 6. **Math.Abs**

`Math.Abs` calcule la valeur absolue d’un nombre, c’est-à-dire sa valeur sans tenir compte du signe.

```csharp
int absValue = Math.Abs(-10); // Renvoie 10
```

### 7. **Math.Ceiling** et **Math.Floor**

- `Math.Ceiling` arrondit un nombre à l’entier supérieur.
- `Math.Floor` arrondit un nombre à l’entier inférieur.

```csharp
double ceilingValue = Math.Ceiling(4.2); // Renvoie 5
double floorValue = Math.Floor(4.8); // Renvoie 4
```

### 8. **Math.Truncate**

Cette fonction tronque la partie décimale d'un nombre, ne gardant que la partie entière sans arrondir.

```csharp
double truncatedValue = Math.Truncate(4.8); // Renvoie 4
```

### 9. **Math.Sign**

`Math.Sign` renvoie 1 si le nombre est positif, -1 si le nombre est négatif, et 0 si le nombre est nul.

```csharp
int sign = Math.Sign(-15); // Renvoie -1
```

### 10. **Math.Sin, Math.Cos, Math.Tan**

Ces fonctions calculent respectivement le sinus, le cosinus et la tangente d'un angle donné en radians.

```csharp
double radians = Math.PI / 4; // 45 degrés en radians
double sine = Math.Sin(radians); // Calcul du sinus
double cosine = Math.Cos(radians); // Calcul du cosinus
double tangent = Math.Tan(radians); // Calcul de la tangente
```

### 11. **Convertir des degrés en radians et inversement**

En C#, les fonctions trigonométriques utilisent des radians. Pour convertir un angle en degrés en radians ou
inversement, on peut utiliser les formules suivantes :

```csharp
double degrees = 45;
double radians = degrees * (Math.PI / 180); // Convertir degrés en radians
double degreesAgain = radians * (180 / Math.PI); // Convertir radians en degrés
```

### Exemple d’utilisation complète

Voici un exemple qui utilise plusieurs de ces fonctions pour calculer l’hypoténuse d’un triangle rectangle :

```csharp
double sideA = 3;
double sideB = 4;
double hypotenuse = Math.Sqrt(Math.Pow(sideA, 2) + Math.Pow(sideB, 2)); // Utilise Pow et Sqrt
Console.WriteLine($"L'hypoténuse est : {hypotenuse}"); // Renvoie 5
```

En maîtrisant ces fonctions de la bibliothèque `Math`, vous pouvez réaliser de nombreux calculs mathématiques essentiels
dans vos programmes C#.