# TP: les requêtes en SQL

## I. Mise en place. 



Téléchargez la version finale de la base cinéma précédente : [cinema_v2.sqlite](./TP2_fichiers/cinema_v2.sqlite)  

Pour écrire et tester vos requêtes SQL, il faut :
1. choisir l’onglet “Exécuter le SQL”

2. créer un nouvel onglet (optionnel, mais permet de garder une trace des
  requêtes précédentes

3. écrire la requête SQL correspondant au besoin formulé

4. exécuter la requête SQL

5. vérifier le résultat obtenu  

  ![](/BaseDeDonnees/IMG/sql.png)

Rappel du schéma relationnel :
![](/BaseDeDonnees/IMG/schema_bdd_cinema_v2.png)

A garder sous les yeux pour la rédaction des requêtes.

## II. Modification, insertion et suppression



Pour chaque proposition suivante, écrire la requête SQL correspondante.  
R01 - Ajoutez le réalisateur "Johnny BEGOOD" avec l'id 31 dans la table
Personnes  
R02 - Ajoutez le genre "horreur" dans la table Genres (sans vous soucier de la colonne idGenre)  
R03 - Ajoutez le cinéma "Mon salon" avec l'id 4, votre adresse personnelle, 1 salle et 4 fauteuils  
R04 - Modifiez le nom de l'acteur : Morgan Freeman (et pas Frimane)  
R05 - Modifiez la date de sortie du Films Seven : 1995 (et pas 1895)  
R06 - Modifiez le rôle de Leonardo DiCaprio dans Inception : Cobb (et pas
Kobe)  
R07 - Supprimez le réalisateur “Johnny BEGOOD” ajouté précédemment ?  
R08 - Supprimez le cinéma “Mon salon” ajouté précédemment ?  

## II. Modification, insertion et suppression sous contrainte



 Pour chaque proposition suivante, écrire la requête SQL correspondante.  

R09 - Supprimez l'acteur "Jason Statham" de la base de données ?  

 Pour chaque requête SQL ci-dessous expliquez pourquoi l’exécution
produira une erreur (sans exécuter la requête bien entendu). Si cette erreur
est liée à une contrainte d’intégrité, précisez laquelle.  

|Requête SQL |Problème|
|:---:|:---:|
|![](r1.png)||
|![](r2.png)||
|![](r3.png)||
|![](r4.png)||
|![](r5.png)||
|![](r6.png)||

## III. Interrogation sur une table  



Pour chaque proposition suivante, écrire la requête SQL correspondante.  
R10 - Listez le contenu complet de la table Personnes  
R11 - Listez les titres de film et leurs années de sortie  
R12 - Listez les noms et prénoms des personnes par ordre alphabétique  
R13 - Classez les titres des films du plus vieux au plus récent  
R14 - Listez les prénoms des personnes (sans les doublons)  
R15 - Listez les personnes (nom et prénom) dont le prénom est “Kevin“  
R16 - Listez les films sortis dans les années 90 (de 1990 à 1999 inclus). On ne
précisera que le titre.  
R17 - Quelles sont les Personnes dont le nom commence par la lettre P ?  
R18 - Listez les 5 films (titre et année) les plus récents  
R19 - Citez les titres des Films qui sont soit sortis en 1999 ou en 2001  
R20 - Déterminez l’année et le titre du film le plus récent  
R21 - Calculez le nombre de salles moyen des cinémas  
R22 - Calculez le nombre total de fauteuils disponibles pour tous les cinémas  
R23 - Calculez combien de films sont sortis en 1995  

## IV. Interrogation sur plusieurs tables (jointures)  

Pour chaque proposition suivante, écrire la requête SQL correspondante.  

R24 - Listez tous les films (titre) correspondant au genre “Drame”  
R25 - Donnez le titre des films réalisés par David Fincher  
R26- Donnez le titre et l’année de la comédie la plus récente  
R27 - Listez les acteurs (nom et prénom) qui jouent dans le film “Usual Suspects”  
R28 - Déterminez dans quel cinéma (nom et adresse) et à quelle date puis-je visionner le film “Seven”  
R29 - Listez les films (titre, date et genre) proposés par le “CGR Niort”  
R30 - Affichez le plus grand cinéma (en nombre de fauteuils) pour aller voir le
film "Les évadés"  

