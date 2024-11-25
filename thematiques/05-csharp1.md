# CSharp

Après un premier tour d'horizon il est temps de se lancer dans la programmation avec un langage plus 
riche et plus complexe, il s'agit du `C#`.

![tiobe.png](../supports/assets/tiobe.png)

## Supports théoriques 📖

### Introduction
- [Bases C#](../supports/csharp-voc-type-expr)
- [CheatSheet Cosmos/Csharp](https://raw.githubusercontent.com/jonathanMelly/cosmos/integration/doc/cheatsheet-csharp.pdf)

### Bases

<a href="/msig24/slides/csharp1/">Slides</a>

- [Gestion mémoire](../supports/variables1.md)
- [Entrées / Sorties / Aléatoire](../supports/input-output-random.md)
- [Logique et conditions](../supports/logique-conditions.md) | [kahoot](https://create.kahoot.it/details/307c3740-c9e2-4f2f-8f94-d8668d7953c8)
- [Répétitions](../supports/repetitions.md) | [Kahoot](https://create.kahoot.it/details/e2ba98fd-c89f-44ce-a5ff-b8c3538a5301)
- [Mathématiques](../supports/math.md) | [Kahoot](https://create.kahoot.it/details/08e07863-1309-40c0-a599-c171e5cfce08)
- [Persistence](../supports/file.md) | [Kahoot](https://create.kahoot.it/details/e65d5f12-5156-40df-9fe8-cf272aac9293)

### Conventions de codage
- [Conventions ETML](https://ici.section-inf.ch/cc)

## Activités 🚝

### Intro
- Bye bye Cosmos, Hello C# : Écrire un programme qui dit bonjour

#### Flashback
À l'aide de la [CheatSheet Cosmos/CSharp](https://raw.githubusercontent.com/jonathanMelly/cosmos/integration/doc/cheatsheet-csharp.pdf)
refaire le [Million](https://labs.section-inf.ch/codelabs/cosmos-base-01-million/index.html?index=..%2F..msig) (avec min 5 questions)

### Bases
- [X] [Rayon](../activites/cercle1/README.md)
- [X] [PileOuFace](../activites/pileface/README.md)
- [X] [Mot de passe](../activites/motdepasse1/README.md)
- [X] [Fourchette](../activites/fourchette/README.md)
- [ ] [Couleur](../activites/couleur/README.md)
- [ ] [Moyenne](../activites/notes/README.md)
- [ ] [Intérêts](../activites/interet/README.md)
- [ ] [Matrix](../activites/matrix/README.md)
- [ ] [Recettes](../activites/recette/README.md) 
- ...


#### Avancés
- [ ] [Formes](../activites/formes/README.md)
- [ ] [ToucherCouler](../activites/bataille-navale/README.md)
- [ ] [Morpion1](../activites/morpion1/README.md)
- ...

## Projet phare 💡

Il s’agit de faire une 3ème version de la [calculatrice](03-cosmos.md#projet-phare--calculatrice) 🧮 en incluant :

- dépôt git pour l'historique des modifications
  - au moins 3 commits
- code source respectant les [conventions de codage](http://ici.section-inf.ch/cc)
- contrôle de saisie
- fonctions min, max et moyenne
- arrondi configurable au démarrage :
  - soit pas d'arrondi
  - soit arrondi à X décimales (X defini par l'utilisateur)
  - valable pour tous les résultats calculés
- sauvegarde automatique des résultats dans un fichier nommé avec la date/heure du moment (extension .txt) :
```csharp
string dateString = DateTime.Now.ToString("dd.MM.yyyy_HH-mm-ss");
//23.11.2024_08-45-02
```
- branding : la calculette est personnalisée selon un fichier `brand.txt` qui contient le nom du sponsor
  - dans le titre, on affiche "sponsorisé par ....." (et les `...` sont remplacés par le contenu de `brand.txt`)
- tests : un PDF avec au moins 3 scénarios (voir [ci-dessous](#livrable))

### Livrable
- une archive avec le projet complet
  - y compris le dossier .git (dépôt)
  - y compris un PDF avec au moins 3 [scénarios de test](../supports/assets/TestsFonctionnelsSucrerie.docx)

### Version `spéciale`
- Implémenter le pavé numérique sur la console en utilisant les touches fléchées et ENTER à l’image de :

![calc1.gif](assets/calc1.gif)