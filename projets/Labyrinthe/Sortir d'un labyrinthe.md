# Sortir d'un labyrinthe. 

L'objectif de ce projet est de trouver un chemin pour sortir d'un labyrinthe.  Ce projet sera noté sur 10 points. 

![](/Labyrinthe/labyrinthe.jpg)

### A. Le labyrinthe. 

Un labyrinthe est généré dans un fichier texte. 

Les symboles # représentent les murs et les . les espaces libres. 

La lettre 'e' représente l'entrée du labyrinthe et la lettre 's', la sortie à atteindre. 

1. Ecrire une fonction `creer_liste(document)`qui prend en paramètre le fichier texte et qui renvoie ce fichier sous forme d'un tableau contenant une liste de chaine de caractères (une ligne correspond à un élément du tableau).

### B. Voir un labyrinthe comme un graphe. 

Nous pouvons représenter un labyrinthe comme un graphe. 

Chaque espace libre du labyrinthe est considéré comme un sommet et ses successeurs sont les espaces libres adjacents. Nous allons donc représenter un labyrinthe comme un graphe. Nous utiliserons une implémentation avec un dictionnaire avec la liste des successeurs. 

2. En utilisant le code fourni, compléter la classe Labyrinthe. 



### C. Au choix.

3. Choisir au moins un des points suivants et écrire le code permettant d'y répondre.

- Améliorer le code afin qu'il trouve le chemin le plus court. 
- générer un labyrinthe de manière aléatoire. Attention, l'entrée et la sortie doivent nécessairement pouvoir être  reliées. 
- proposer une version jeu du labyrinthe avec un utilisateur. 
- ou toute autre idée !

**Barème**

|                                       | Points   |
| ------------------------------------- | -------- |
| fonction `creer_liste(document)`      | 1 point  |
| fonction `get_entree` et `get_sortie` | 1 point  |
| fonction `creeListeAdjacence`         | 1 point  |
| fonction `trouveRecursif`             | 3 points |
| Au choix                              | 2 points |
| commentaires                          | 1 point  |
| propreté du code                      | 1 point  |















