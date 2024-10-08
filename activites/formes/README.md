# Formes
Dessiner des formes géométriques sur la console

## Description de l'exercice

1. **Objectif** : Créer un programme qui permet à l'utilisateur de dessiner plusieurs formes géométriques (triangle,
   rectangle, rond, losange) sur la console en utilisant des caractères "X".

2. **Formes à dessiner** :
    - Un **triangle** isocèle aligné sur sa base.
    - Un **rectangle** de dimensions choisies par l'utilisateur.
    - Un **losange** centré, formé par des "X".
    - Une approximation d'un **cercle**.

3. **Entrées** :
    - L'utilisateur doit choisir la forme qu'il souhaite dessiner.
    - Pour certaines formes, l'utilisateur doit entrer des dimensions :
        - Pour le triangle : la hauteur.
        - Pour le rectangle : la largeur et la hauteur.
        - Pour le losange : la longueur de la diagonale.
        - Pour le cercle : le rayon (pour une approximation de cercle en caractères).

4. **Sorties** :
    - Le programme affiche la forme choisie sur la console en utilisant des caractères "X".
    - Par exemple :
        - **Triangle** (hauteur 4) :
          ```
             X
            XXX
           XXXXX
          XXXXXXX
          ```
        - **Rectangle** (largeur 5, hauteur 3) :
          ```
          XXXXX
          XXXXX
          XXXXX
          ```
        - **Losange** (diagonale de 5) :
          ```
            X
           XXX
          XXXXX
           XXX
            X
          ```
        - **Cercle** (rayon approximatif) :
            - Représenter un cercle est plus difficile, donc une approximation pourrait ressembler à ceci pour un rayon
              de 3 :
          ```
           XXX
          XXXXX
          XXXXX
           XXX
          ```

5. **Calculs et logique** :
    - Utiliser des boucles pour itérer sur les lignes et les colonnes.
    - Manipuler les conditions pour positionner correctement les "X" (par exemple, calculer les espaces pour centrer les
      formes comme le triangle et le losange).
    - Pour le cercle, utiliser une formule géométrique comme l'équation d'un cercle $( (x - h)^2 + (y - k)^2 = r^2 $)
      pour dessiner les points à proximité du contour.
    <details>
   <summary>Si besoin, cliquer ici pour voir un pseudo-code</summary>
   
   ```mermaid
   graph TD
    A[Début] --> B[Entrer le rayon du cercle]
    B --> C["Définir les coordonnées du centre (cx et cy)"]
    C --> D[Pour chaque y de 0 à 2*r]
    D --> E[Pour chaque x de 0 à 2*r]
    E --> F{"(x - cx)^2 + (y - cy)^2 <= r^2 ?"}
    F -- Oui --> G["Afficher X"]
    F -- Non --> H[Afficher un espace]
    G --> J[Passer à l'itération suivante de x]
    H --> J
    J --> L{"Fin de double boucle (y==2*r) ?"}
    L -- Oui --> K[Fin]
    L -- Non --> N[Afficher une nouvelle ligne après chaque ligne de y]
    N --> D
    N --> E
   ```
   </details>

6. **Fonctionnalité additionnelle (optionnelle)** :
    - Permettre à l'utilisateur de choisir le caractère à utiliser au lieu de "X".
    - Ajouter une option pour dessiner plusieurs formes en une seule exécution.
    - Proposer un menu interactif pour choisir les formes.
