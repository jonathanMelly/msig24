---
title: Introduction to HTML & CSS
theme: apple-basic
background: 'linear-gradient(90deg, #ff7e5f, #feb47b)'
layout: center
---

# HTML & CSS - Les bases 

---

# Sommaire 

<Toc minDepth="1" maxDepth="1"></Toc>

--- 
layout: image-right
image: '/images/cute-halloween-3d-skeleton.jpg'
---

# Qu'est-ce que HTML ?
### **HTML (HyperText Markup Language)** 
- Structure le contenu d'une page web comme  
  - les Titres
  - Paragraphes
  - Images 
  - Liens

 🦴 C'est le "squelette" d'un site web. 🦴

---
layout: image-right
image: '/images/css-skeleton.webp'
---

# Qu'est-ce que CSS ?
### **CSS (Cascading Style Sheets):** 
- Gère l'apparence et le style comme : 
  - les couleurs
  - les marges 
  - les tailles
  
- 👕 C'est "Les vêtements du squelette." 👕

---
layout: center
---

# Structure de base d'un fichier HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Exemple</title>
  </head>
  <body>
    <h1>Bienvenue</h1>
    <p>Ceci est un paragraphe.</p>
  </body>
</html>
```

---

## Balises HTML courantes

- Titres (du plus grand au plus petit) :
  - `<h1>` à `<h6>` 
- Paragraphe :
  - `<p>` 
- Lien hypertexte :
  - `<a href="url">` 
- Image :
  - `<img src="image.jpg" alt="Description">`
- Listes (non ordonnée et ordonnée) :
  - `<ul>` et `<ol>` 
- Conteneurs : 
  - `<div>`

---

# Lier un fichier CSS à HTML
## Ajouter un lien CSS dans le `<head>`
```html
<link rel="stylesheet" href="styles.css">
```

## Exemple d'arborescence
```
projet/
├── index.html
└── styles.css
```
--- 

# Exemple de code CSS
```css
/* Couleurs */
h1 {
  color: #3498db; /* Bleu */
  background-color: #f0f0f0; /* Gris clair */
  padding: 10px;
}
```
```css
body {
  font-family: 'Roboto', sans-serif;
}

/* Styliser les titres */
h1 {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px; /* Espacement des lettres */
}

```
---

# Utiliser une classe en CSS
Une classe en CSS est un moyen de sélectionner un ou plusieurs éléments HTML afin d'appliquer des styles spécifiques. Les classes sont extrêmement utiles pour réutiliser des styles dans un document ou à travers plusieurs pages.
### HTML
```html
<div class="container">
  <p class="highlight">Ceci est un texte important.</p>
</div>
```

### CSS
```css
.container {
  padding: 20px;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.highlight {
  color: red;
  font-weight: bold;
}
```
---
layout: center
---

# Bonus : Découverte des librairies CSS

---

# Bootstrap

- Librairie CSS avec des composants prêts à l'emploi (boutons, grilles, navigations).

Exemple d'utilisation : Ajouter le lien CDN dans le fichier HTML :

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```
Bouton stylé avec Bootstrap :


```html
<button class="btn btn-primary">Bouton Principal</button>
```

Lien vers la documentation [Bootstrap](https://getbootstrap.com/)

---

# Tailwind CSS 

- Librairie utilitaire CSS. Pas de composants pré-faits. Très flexible pour personnaliser entièrement le design.

Exemple d'utilisation : Ajouter le script CDN dans le fichier HTML :
```html
<script src="https://cdn.tailwindcss.com"></script>
```

Bouton stylé avec Tailwind CSS :
```html
<button class="bg-blue-500 text-white font-bold py-2 px-4 rounded">
  Bouton Principal
</button>
```

Lien vers la documentation [TailwindCSS](https://tailwindcss.com/)

---
layout: center 
---

# Questions ?
