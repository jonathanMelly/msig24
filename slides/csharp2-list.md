---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: 'text-center'
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: C# Collections et LINQ
mdc: true
---

# C# Collections et LINQ
## Une introduction pour débutants

---
layout: default
---

# Les Listes en C#

<v-click>

Une liste est comme une boîte où on peut ranger plusieurs éléments du même type.

</v-click>

<v-click>

```csharp
// Créer une nouvelle liste
List<int> nombres = new List<int>() { 1, 2, 3, 4, 5 };
```

</v-click>

<v-click>

Opérations de base :
```csharp {none|1|2|3|all}
nombres.Add(6);           // Ajouter
nombres.Remove(3);        // Supprimer le premier 3
nombres.RemoveAt(0);      // Supprimer à l’index 0
int premier = nombres[0]; // Accéder à l’élément 0
```

</v-click>

---
layout: two-cols
---

# Opérations Courantes

<v-click>

```csharp {1|2|3|all}
List<string> fruits = new();
fruits.Clear();            // Vider
int taille = fruits.Count; // Taille
```

</v-click>

::right::

<v-click>

# Points Importants

- Index commence à 0
- Taille dynamique
- Un seul type d'éléments

</v-click>

---
layout: center
---

# Opérations sur les Listes
<div class="my-8">
  <ListOperations></ListOperations>
</div>


---
layout: center
---

# LINQ 🚀
## La boîte à outils magique

---

# Filtrer avec Where

<v-click>

```csharp {1|1-3|4}
List<int> nombres = new List<int>() { 1, 2, 3, 4, 5, 6 };

var pairs = nombres.Where(n => n % 2 == 0);
// Résultat : 2, 4, 6
```

</v-click>

<v-click>

- Filtre les éléments selon une condition
- Retourne une nouvelle collection
- Ne modifie pas la collection originale

</v-click>

---

# Transformer avec Select

<v-click>

```csharp
List<string> names = new List<string>() { "Alex", "Marie" };

var majuscules = names.Select(p => p.ToUpper());
// Résultat : "ALEX", "MARIE"
```

</v-click>

<v-click>

- Transforme chaque élément
- Peut changer le type de sortie
- Crée une nouvelle collection

</v-click>

---

# Trier avec OrderBy

<v-click>

```csharp
List<string> fruits = new List<string>() 
{ 
    "banane", "pomme", "orange" 
};

var tries = fruits.OrderBy(f => f);
// Résultat : "banane", "orange", "pomme"
```

</v-click>

---
layout: end
---

# Merci !

Des questions ? 🤔