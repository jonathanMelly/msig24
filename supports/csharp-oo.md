# C# Orienté Objet : les bases

## Table des matières
1. Les bases des classes et des objets
2. Les attributs et types de données
3. L'encapsulation et les propriétés
4. Les méthodes
5. Les constructeurs
6. L'héritage
7. Le polymorphisme
8. Les interfaces

## 1. Les bases des classes et des objets

### Qu'est-ce qu'une classe ?
Une classe est un modèle qui définit la structure et le comportement des objets. Elle peut être vue comme un "plan" à partir duquel on peut créer des objets.

### Exemple simple d'une classe
```csharp
public class Student
{
    // La classe est vide pour l'instant
}
```

### Création d'un objet (instance)
```csharp
Student student1 = new Student();
```

## 2. Les attributs et types de données

### Les attributs (champs)
Les attributs sont les données stockées dans une classe. Ils représentent les caractéristiques des objets.

### Types de données courantes
- string : texte
- int : nombres entiers
- double : nombres décimaux
- bool : valeurs booléennes (true/false)
- DateTime : dates

### Exemple avec des attributs
```csharp
public class Student
{
    
    public string firstName;
    public string lastName;
    public int age;
    public double grade;
    public bool isEnrolled;
}
```

> [!TIP]
> Idéalement les attributs sont notés `private` par défaut
> mais pour des raisons de simplification c’est la visibilité `public`
> qui est utilisée.

## 3. L'encapsulation et les propriétés

### L'encapsulation
Principe qui consiste à :
- Masquer les données internes de la classe
- Contrôler l'accès aux données via des propriétés

### Les propriétés
Les propriétés permettent de contrôler l'accès aux attributs de manière sécurisée.

```csharp
public class Student
{
    private string firstName;
    
    public string FirstName
    {
        get 
        { 
            //if ...
            return firstName; 
        }
        set 
        { 
            //if ...
            firstName = value; 
        }
    }

    // Version courte (propriété auto-implémentée)
    public string LastName { get; set; }
}
```

## 4. Les méthodes

### Définition
Les méthodes sont des fonctions qui définissent le comportement des objets.

### Types de méthodes
- Méthodes sans retour (void)
- Méthodes avec retour
- Méthodes avec paramètres

```csharp
public class Student
{
    private List<double> grades = new();

    // Méthode sans retour avec paramètre
    public void AddGrade(double grade)
    {
        // Logique pour ajouter une note
    }

    // Méthode avec retour
    public double CalculateAverage()
    {
        double sum = 0;
        foreach(double grade in grades)
        {
            sum += grade;
        }
        return sum / grades.Count;
    }
}
```

## 5. Les constructeurs

### Définition
Les constructeurs sont des méthodes spéciales qui initialisent les objets lors de leur création.

```csharp
public class Student
{
    public string firstName;
    public string lastName;

    // Constructeur par défaut
    public Student()
    {
        firstName = "Unknown";
        lastName = "Unknown";
    }

    // Constructeur avec paramètres
    public Student(string firstName, string lastName)
    {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}
```

## 6. L'héritage

### Définition
L'héritage permet à une classe d’hériter des caractéristiques d'une autre classe.

```csharp
// Classe de base
public class Person
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
}

// Classe dérivée
public class Student : Person
{
    public double Grade { get; set; }
}
```

## 7. Le polymorphisme

### Définition
Le polymorphisme permet à une méthode d'avoir différents comportements selon le contexte.

```csharp
public class Person
{
    public virtual string GetDescription()
    {
        return "Je suis une personne.";
    }
}

public class Student : Person
{
    public override string GetDescription()
    {
        return "Je suis un étudiant.";
    }
}
```

## 8. Le polymorphisme avec les listes

### Définition et utilisation
Le polymorphisme avec les listes permet de stocker des objets de différents types dérivés dans une même collection, tout en maintenant leur comportement spécifique.

### Exemple pratique
```csharp
public class School
{
    // Liste polymorphique qui peut contenir des Person et tous ses dérivés
    private List<Person> people = new();

    public void AddPerson(Person person)
    {
        people.Add(person);
    }

    public void PrintAllDescriptions()
    {
        foreach (Person person in people)
        {
            // La méthode appelée dépendra du type réel de l'objet
            Console.WriteLine(person.GetDescription());
        }
    }
}

// Utilisation
School school = new School();
school.AddPerson(new Person());          // Ajoute une personne
school.AddPerson(new Student());         // Ajoute un étudiant
school.AddPerson(new Teacher());         // Ajoute un professeur

// Affichera les descriptions spécifiques à chaque type
school.PrintAllDescriptions();
```

### Avantages
- Facilite la gestion de collections d'objets de types différents
- Permet d'appliquer des comportements spécifiques sans connaître le type exact
- Rend le code plus flexible et extensible

### Exemple avancé avec LINQ
```csharp
public class School
{
    private List<Person> people = new List<Person>();

    // Utilisation de LINQ avec polymorphisme
    public List<Student> GetAllStudents()
    {
        return people.OfType<Student>().ToList();
    }

    public double GetAverageStudentGrade()
    {
        return people.OfType<Student>()
                    .Average(s => s.Grade);
    }

    public List<Person> GetPeopleByRole(string role)
    {
        return people.Where(p => p.GetType().Name == role).ToList();
    }
}
```

## 9. Les interfaces

### Définition
Une interface définit un contrat que les classes doivent respecter.

```csharp
public interface IStudyable
{
    void Study();
    double TakeExam();
}

public class Student : IStudyable
{
    public void Study()
    {
        Console.WriteLine("L'étudiant étudie...");
    }

    public double TakeExam()
    {
        return 85.5; // Note d'exemple
    }
}
```

### Idées d’exercices pour pratiquer :

1. Créer une classe `Car` avec des attributs basiques
2. Ajouter des propriétés et des méthodes à la classe
3. Implémenter l'héritage avec une classe `ElectricCar`
4. Créer une interface `IVehicle` et l'implémenter
5. Utiliser le polymorphisme avec différents types de véhicules