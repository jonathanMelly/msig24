# Décomposition

Un projet ambitieux qui paraît difficile est souvent réalisable si on le réduit
à des sous-projets qu’on pense plus aisés.

![cle.png](cle.png)

Ainsi que ce soit émotionnel ou rationnel, la décomposition d’un problème donné
est souvent la clé pour le réaliser !

Voici donc quelques activités pour rafraîchir cette compétence.

## Échauffement

# Exercice : Décomposition des Nombres

## Question 1 : Décomposition en Facteurs Premiers
Décomposez le nombre 60 en ses facteurs premiers.

<details>
<summary>Réponse</summary>

60 peut être décomposé en facteurs premiers comme suit :

$$ 60 = 2 \times 2 \times 3 \times 5 = 2^2 \times 3 \times 5 $$

</details>

## Question 2 : Décomposition en Puissances de 10
Comment décomposer le nombre 4529 en une somme de puissances de 10 ?

> Pour rappel, un nombre élevé à la puissance 0 vaut 1 : $5^0 = 1$, $445^0 = 1$, ...

<details>
<summary>Réponse</summary>

Le nombre 4529 peut être décomposé comme suit :

$$ 4529 = 4000 + 500 + 20 + 9 $$

Ou en utilisant les puissances de 10 :

$$ 4529 = 4 \times 10^3 + 5 \times 10^2 + 2 \times 10^1 + 9 \times 10^0 $$
</details>

## Question 3 : Décomposition en Nombres Pairs et Impairs
Décomposez la liste suivante de nombres en deux sous-listes : une contenant les nombres pairs et l'autre contenant les nombres impairs.
Liste : 3, 12, 7, 8, 15, 6, 21, 10

<details>
<summary>Réponse</summary>

- Nombres pairs : 12, 8, 6, 10
- *Nombres impairs : 3, 7, 15, 21*
</details>

## Question 4 : Décomposition d'une Fraction en une Somme de Fractions Unitaires
Décomposez la fraction $\frac{5}{6}$ en une somme de fractions unitaires (fractions dont le numérateur est 1).

<details>
<summary>Réponse</summary>

La fraction $\frac{5}{6}$ peut être décomposée en :
$$ \frac{5}{6} = \frac{3}{6} + \frac{2}{6} = \frac{1}{2} + \frac{1}{3} $$
</details>

## Question 5 : Décomposition d'un Nombre en Forme Canonique
Décomposez le nombre 3240 en sa forme canonique (produit de facteurs premiers avec leurs puissances).

<details>
<summary>Réponse</summary>

3240 peut être décomposé en sa forme canonique comme suit :
$$ 3240 = 2^3 \times 3^4 \times 5^1 $$
</details>

## Restaurant

![livraison.png](livraison.png)

### Contexte

Vous êtes chargé(e) de développer une application qui permet de gérer les commandes d'un restaurant en ligne. Le
restaurant veut une solution qui permette de :

1. **Prendre des commandes** (menu et options pour chaque plat).
2. **Calculer le prix total** (en tenant compte des réductions et taxes).
3. **Gérer les livraisons** (vérifier les zones de livraison).
4. **Suivre l'état de la commande** (préparation, en cours de livraison, livrée).

### Partie 1 : Décomposition du problème

Décomposez le problème de gestion des commandes en plusieurs sous-problèmes simples. Pour chaque sous-problème,
identifiez :

- **Les données en entrée** (quelles informations sont nécessaires ?).
- **Les étapes principales** (quelles sont les étapes pour traiter ce sous-problème ?).
- **Le résultat attendu** (qu'est-ce qui doit être produit ou décidé ?).

Voici quelques pistes pour vous guider :

1. **Prendre des commandes**
    - Quels sont les éléments d'une commande ?
    - Comment les options sont-elles sélectionnées ?

2. **Calculer le prix total**
    - Quels facteurs doivent être pris en compte (prix de base, réductions, taxes) ?
    - Comment appliquer des réductions ?

3. **Gérer les livraisons**
    - Comment vérifier si une adresse est dans la zone de livraison ?
    - Que faire si l'adresse n'est pas éligible ?

4. **Suivre l'état de la commande**
    - Quelles sont les étapes possibles d'une commande ?
    - Comment mettre à jour l'état au fur et à mesure ?

### Partie 2 : Exemple de sous-problème

Prenez l'un des sous-problèmes que vous avez identifié et décrivez plus en détail :

- **Sous-problème : Calcul du prix total**
    1. **Entrées** : Liste des articles commandés, prix de base, réductions possibles, taxes applicables.
    2. **Étapes** :
        - Calculer le prix de base (somme des prix des articles).
        - Appliquer les réductions (si éligible).
        - Calculer les taxes sur le prix réduit.
        - Produire le prix final.
    3. **Résultat** : Le montant total à payer.

### Partie 3 : Implémentation en pseudocode (Facultatif)

Pour l'un des sous-problèmes, écrivez un pseudocode simple qui résout le problème.

Exemple pour le **calcul du prix total** :

```text
prix_base = somme des articles
prix_reduit = prix_base - reductions
prix_final = prix_reduit + taxes
```

### Annexes pour l’exercice `Restaurant`

- <a href="c-decomposer1.docx">Template à compléter1</a>
- <a href="x-decomposer1.docx">Corrigé</a>