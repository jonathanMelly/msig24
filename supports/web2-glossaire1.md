# Glossaire 1 des éléments CSS et JavaScript

## CSS - Concepts fondamentaux

### Modèles de mise en page

| Terme       | Description                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Flexbox** | Modèle de mise en page unidimensionnel pour organiser des éléments en lignes ou colonnes. Idéal pour les alignements simples.           |
| **Grid**    | Modèle de mise en page bidimensionnel permettant de contrôler à la fois les lignes et les colonnes. Parfait pour les layouts complexes. |

### Propriétés CSS principales

| Propriété         | Description                                                                                                                            |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **display**       | Définit le type de boîte de rendu utilisée pour un élément. Valeurs clés : `flex`, `grid`, `block`, `inline`, `none`.                  |
| **border-radius** | Arrondit les coins d'un élément. Peut prendre jusqu'à 4 valeurs (haut-gauche, haut-droit, bas-droit, bas-gauche).                      |
| **transform**     | Modifie l'apparence d'un élément sans changer le flux du document (rotation, mise à l'échelle, translation, etc.).                     |
| **transition**    | Anime les changements de propriétés CSS sur une durée définie. Exemple : `transition: all 0.3s ease;`                                  |
| **position**      | Contrôle la méthode de positionnement d'un élément. Valeurs clés : `static`, `relative`, `absolute`, `fixed`.                          |
| **overflow**      | Définit le comportement d'un élément lorsque son contenu dépasse ses dimensions. Valeurs clés : `visible`, `hidden`, `scroll`, `auto`. |

### Propriétés Flexbox

| Propriété           | Description                                                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **justify-content** | Aligne les éléments le long de l'axe principal. Valeurs clés : `flex-start`, `flex-end`, `center`, `space-between`, `space-around`. |
| **align-items**     | Aligne les éléments le long de l'axe secondaire. Valeurs clés : `flex-start`, `flex-end`, `center`, `stretch`, `baseline`.          |
| **flex-direction**  | Définit la direction de l'axe principal. Valeurs : `row`, `column`, `row-reverse`, `column-reverse`.                                |
| **flex-wrap**       | Détermine si les éléments doivent être forcés sur une seule ligne ou peuvent s'envelopper sur plusieurs lignes.                     |

### Propriétés Grid

| Propriété                 | Description                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------|
| **grid-template-columns** | Définit le nombre et la taille des colonnes de la grille. Exemple : `grid-template-columns: 1fr 2fr 1fr;`   |
| **grid-template-rows**    | Définit le nombre et la taille des rangées de la grille. Exemple : `grid-template-rows: 2fr 1fr 2fr;`       |
| **grid-column**           | Spécifie la position d'un élément sur les colonnes de la grille. Exemple : `grid-column: 2;` (2ème colonne) |
| **grid-row**              | Spécifie la position d'un élément sur les rangées de la grille. Exemple : `grid-row: 3;` (3ème rangée)      |
| **justify-self**          | Aligne un élément individuellement sur l'axe horizontal. Exemple : `justify-self: center;`                  |
| **align-self**            | Aligne un élément individuellement sur l'axe vertical. Exemple : `align-self: start;`                       |

### Unités CSS

| Unité     | Description                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------|
| **px**    | Pixels - Unité fixe précise. 1px équivaut généralement à un point sur l'écran.                       |
| **%**     | Pourcentage - Relatif à la taille de l'élément parent.                                               |
| **em**    | Relatif à la taille de police de l'élément. 1em = taille de police actuelle.                         |
| **rem**   | Relatif à la taille de police de l'élément racine (html). Évite les problèmes d'héritage en cascade. |
| **vw/vh** | Relatif à la largeur (vw) ou hauteur (vh) de la fenêtre. 1vw = 1% de la largeur de la fenêtre.       |
| **fr**    | Fraction - Spécifique à CSS Grid, représente une fraction de l'espace disponible.                    |

### Fonctions CSS

| Fonction            | Description                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------|
| **translate(x, y)** | Déplace un élément horizontalement (x) et verticalement (y). Exemple : `transform: translate(10px, 20px);` |
| **repeat()**        | Répète un modèle. Utilisé principalement avec Grid. Exemple : `grid-template-columns: repeat(3, 1fr);`     |

## JavaScript - Concepts fondamentaux

### Concepts de base

| Terme         | Description                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------|
| **Variable**  | Espace de stockage nommé pour stocker des données. Déclaration avec `let`, `const` ou `var`.             |
| **Fonction**  | Bloc de code réutilisable qui exécute une tâche spécifique.                                              |
| **Événement** | Action détectée par le navigateur (clic, chargement, etc.) qui peut déclencher du code JavaScript.       |
| **DOM**       | Document Object Model - Représentation sous forme d'arbre des éléments HTML, manipulable via JavaScript. |

### Manipulation du DOM

| Méthode                        | Description                                                                                            |
|--------------------------------|--------------------------------------------------------------------------------------------------------|
| **document.getElementById()**  | Sélectionne un élément HTML par son attribut `id`.                                                     |
| **element.addEventListener()** | Attache une fonction (gestionnaire d'événements) à un élément pour répondre à un événement spécifique. |
| **element.style**              | Accède et modifie les propriétés de style CSS d'un élément.                                            |
| **element.innerHTML**          | Obtient ou définit le contenu HTML d'un élément.                                                       |

### Fonctions JavaScript utiles

| Fonction         | Description                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------|
| **alert()**      | Affiche une boîte de dialogue avec un message et un bouton OK.                                        |
| **prompt()**     | Affiche une boîte de dialogue avec un champ de saisie et retourne la valeur entrée par l'utilisateur. |
| **confirm()**    | Affiche une boîte de dialogue avec des boutons OK et Annuler, retourne `true` ou `false`.             |
| **setTimeout()** | Exécute une fonction après un délai spécifié (en millisecondes).                                      |

### Structures de contrôle

| Structure     | Description                                                              |
|---------------|--------------------------------------------------------------------------|
| **if...else** | Exécute différents blocs de code selon une condition.                    |
| **switch**    | Évalue une expression et exécute du code en fonction de cas spécifiques. |
| **for**       | Boucle qui répète du code un nombre déterminé de fois.                   |
| **while**     | Boucle qui répète du code tant qu'une condition est vraie.               |

### Manipulation d'objets et de données

| Concept               | Description                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| **Objet**             | Collection de paires clé-valeur. Exemple : `{x: 0, y: 0}`                                                  |
| **Template literals** | Chaînes de caractères qui permettent l'interpolation d'expressions. Exemple : `` `Position: ${x}, ${y}` `` |
| **Opérateur +=/-=**   | Raccourcis pour ajouter/soustraire une valeur à une variable. Exemple : `position.x += 10;`                |

## Relations entre CSS et JavaScript

| Relation                      | Description                                                                                                              |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **element.style.property**    | JavaScript peut modifier directement les propriétés CSS d'un élément. Exemple : `element.style.backgroundColor = 'red';` |
| **element.classList**         | Permet d'ajouter, supprimer ou basculer des classes CSS.                                                                 |
| **element.style.transform**   | Utilisé pour appliquer des transformations CSS via JavaScript, comme dans notre exemple de translation du visage.        |
| **window.getComputedStyle()** | Obtient toutes les propriétés CSS calculées pour un élément.                                                             |

Ce glossaire couvre tous les concepts CSS et JavaScript vus dans notre tutoriel sur la création d'un visage interactif.
Il peut servir de référence rapide pour comprendre les différentes propriétés et méthodes utilisées.