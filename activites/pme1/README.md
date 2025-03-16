# Visualiseur de clients pour PME

## Contexte
Vous travaillez pour une très petite entreprise qui possède un fichier CSV contenant la liste de ses clients. Le gérant souhaite une interface web simple pour consulter et filtrer cette liste.

## Données
Le fichier [`data.csv`](data.csv) contient :
- Nom
- Prénom
- Email
- Téléphone
- Ville
- Montant total des achats
- Date de dernier achat

## Objectifs

1. **Visualiser les clients**
    - Afficher la liste des clients dans un tableau HTML
    - Permettre le tri par nom ou par montant d'achat

2. **Filtrer les données**
    - Ajouter un champ de recherche pour filtrer par nom
    - Créer un filtre pour n'afficher que les clients d'une ville spécifique

3. **Ajouter un client**
    - Créer un formulaire simple pour ajouter un nouveau client

## Contraintes techniques

1. **Frontend**
    - HTML5 basique
    - CSS avec Flexbox pour la mise en page
    - JavaScript vanilla pour les interactions
    - Fetch API pour communiquer avec le backend

2. **Backend**
    - PHP simple pour lire et écrire dans le fichier CSV
    - API pour renvoyer les données au format JSON
    - Endpoint pour ajouter un nouveau client

## Étapes suggérées

1. Créer une page HTML avec un tableau pour afficher les clients
2. Développer un script PHP qui lit le CSV et renvoie les données en JSON
3. Utiliser JavaScript et Fetch pour récupérer et afficher les données
4. Ajouter les fonctionnalités de tri et de filtrage côté client
5. Créer un formulaire d'ajout et l'endpoint PHP correspondant

## Livrables

1. Une page HTML pour afficher les clients
2. Un script JavaScript pour gérer l'affichage et les interactions
3. Deux scripts PHP : un pour lire les données, un pour ajouter un client

Cette version simplifiée se concentre sur l'essentiel tout en couvrant les compétences demandées : HTML, JavaScript, PHP, Fetch et JSON. Elle est plus accessible tout en restant pertinente pour l'apprentissage.