# Hello WEB

## Activité 1: Hello
Pour débuter en PHP orienté WEB (on peut aussi faire du PHP hors WEB), voici une suggestion :

### Setup
Pour PHP, on a besoin d’un serveur WEB qui connaît le PHP habituellement couplé à un serveur de base de données.

#### Version minimale

##### PHP
Le plus simple pour PHP est d’utiliser [nomad](https://github.com/jonathanMelly/nomad) pour installer php en local :

```shell
nomad -version 8.3 install php
```
puis
```shell
cd apps
cd php
php -S localhost:8080 -t c:\msig\prog\web
```

##### MariaDB
En attendant que [nomad](https://github.com/jonathanMelly/nomad) offre un package `MariaDb`, on peut utiliser :
[MariaDB portable](https://mariadb.org/download/?t=mariadb&o=true&p=mariadb&r=5.5.29&os=windows&cpu=x86_64&pkg=msi&mirror=archive)

#### Alternatives
Il existe d’autres manières de mettre en place un environnement :

- [docker](https://github.com/jonathanMelly/docker/blob/main/web1.md)
- uwamp
- easyphp

### Index
Aller dans le dossier WWW (c:\msig\web ou le dossier choisi après le `-t`) et éditer/créer le fichier index.php dans le dossier msig (à créer) avec notepad++ :

```php
<?php 
echo "Hello master MSIG"
```

Sauvegarder le fichier 

### Test
Lancer le navigateur à l'adresse http://localhost/msig/ 

Vérifier que la page affiche le texte 'Hello master MSIG' 

## Activité 2 : Tuto "apprentice" et références

### Tutos phpapprentice
Pour apprendre le langage PHP, je suggère la ressource suivante : https://phpapprentice.com/

Vous pouvez donc aller **jusqu'au chapitre 10** pour découvrir la syntaxe de PHP…

### Référence
Outre l'exemple basique (Hello Formulaire) présenté après, voici quelques ressources de l'ETML en français :

https://enseignement.section-inf.ch/moduleICT/133/Index.html (PHP WEB)

https://enseignement.section-inf.ch/moduleICT/151/Index.html (Base de données)

https://enseignement.section-inf.ch/moduleICT/150/Index.html (E-Commerce)

Et voici encore une source intéressante : https://www.w3schools.com/php/ 
