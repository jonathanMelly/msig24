---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Gestion des Événements JavaScript
---

# Gestion des Événements JavaScript
## Interactions souris et clavier

---
layout: default
---

# Plan de la présentation

- Introduction aux événements JavaScript
- Événements de souris
- Événements de clavier
- Différentes méthodes d'attachement d'événements
- Bonnes pratiques
- Démo interactive
- Questions

---
layout: two-cols
---

# Qu'est-ce qu'un événement ?

- Action ou occurrence détectée par le programme
- Peut être initiée par l'utilisateur ou le navigateur
- Permet de rendre les pages web interactives
- Base de la programmation événementielle

::right::

```js
// Structure de base
element.addEventListener('event', function(e) {
    // Code à exécuter quand l'événement se produit
});
```

---

# Événements de souris

| Événement | Description |
|-----------|-------------|
| `click` | Clic souris simple |
| `dblclick` | Double-clic |
| `mousedown` | Bouton souris enfoncé |
| `mouseup` | Bouton souris relâché |
| `mousemove` | Déplacement de la souris |
| `mouseover` | Souris entre dans un élément |
| `mouseout` | Souris quitte un élément |
| `mouseenter` | Souris entre (sans propagation) |
| `mouseleave` | Souris quitte (sans propagation) |

---

# L'objet Event pour la souris

```js
element.addEventListener('click', function(event) {
    // Coordonnées relatives à la fenêtre
    console.log('clientX:', event.clientX, 'clientY:', event.clientY);

    // Coordonnées relatives au document
    console.log('pageX:', event.pageX, 'pageY:', event.pageY);

    // Bouton de souris
    console.log('Button:', event.button);

    // Modificateurs
    console.log('Alt:', event.altKey, 'Ctrl:', event.ctrlKey,
        'Shift:', event.shiftKey);
});
```

---

# Événements de clavier

| Événement | Description |
|-----------|-------------|
| `keydown` | Touche enfoncée |
| `keyup` | Touche relâchée |
| `keypress` | Touche enfoncée (caractères) |

<div class="text-sm mt-4">
  <strong>Note :</strong> <code>keypress</code> est déprécié, préférez <code>keydown</code>
</div>

---

# L'objet Event pour le clavier

```js
document.addEventListener('keydown', function(event) {
    // Code de la touche
    console.log('Key code:', event.keyCode); // Déprécié

    // Méthodes modernes
    console.log('Key:', event.key);
    console.log('Code:', event.code);

    // Modificateurs
    console.log('Alt:', event.altKey, 'Ctrl:', event.ctrlKey,
        'Shift:', event.shiftKey);

    // Empêcher le comportement par défaut
    // event.preventDefault();
});
```

---

# Différentes méthodes d'attachement

## 1. Attributs HTML (non recommandé)
```html
<button onclick="handleClick()">Cliquez-moi</button>
```

## 2. Propriétés d'événement (limitation : un seul gestionnaire)
```js
element.onclick = function(e) {
    console.log('Clic détecté');
};
```

## 3. addEventListener (recommandé)
```js
element.addEventListener('click', function(e) {
    console.log('Clic détecté');
}, options);
```

---

# La propagation des événements

<div class="grid grid-cols-2 gap-4">
<div>

## Phases
1. **Capture** : de la racine vers la cible (haut → bas)
2. **Target** : sur l'élément cible
3. **Bubbling** : de la cible vers la racine (bas → haut)

## Contrôle de la propagation
```js
// Arrête toute propagation ultérieure
event.stopPropagation();

// Empêche l'action par défaut (ne bloque pas la propagation)
event.preventDefault();
```

</div>
<div>

```js
// Phase de capture (3e paramètre = true)
parent.addEventListener('click', function(e) {
  console.log('Parent - phase capture');
}, true);

// Phase de bouillonnement (par défaut)
child.addEventListener('click', function(e) {
  console.log('Enfant - phase bubbling');
  
  // Arrête la propagation
  e.stopPropagation();
});
```

</div>
</div>

---
class: interactive-demo
---

# Démo interactive

[Voir la démo](https://jonathanmelly.github.io/msig24/supports/javascript-event-demo.html)

---

# Bonnes pratiques

- Préférer `addEventListener` aux autres méthodes
- Délégation d'événements pour les listes ou collections d'éléments
- Débounce/throttle pour les événements fréquents (`mousemove`, `scroll`)
- Nettoyage des écouteurs avec `removeEventListener`
- Utilisation de fonctions nommées pour faciliter le nettoyage

```js
// Délégation d'événements
document.querySelector('ul').addEventListener('click', function(e) {
    if (e.target.tagName === 'LI') {
        console.log('Item cliqué:', e.target.textContent);
    }
});
```

---

# Ressources utiles

- [MDN Web Docs: Événements](https://developer.mozilla.org/fr/docs/Web/Events)
- [Event reference](https://developer.mozilla.org/en-US/docs/Web/Events)
- [JavaScript.info: Introduction aux événements](https://fr.javascript.info/events)
- [Délégation d'événements](https://javascript.info/event-delegation)

---
layout: center
class: text-center
---

# Questions?

[Documentation](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener) · [Exemples de code](https://github.com/examples/js-events)