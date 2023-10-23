# Les graphes :exercices. 



Exercice 1 : On souhaite organiser un tournoi de football avec 4 équipes (numérotées de 1 à 4). 

Chaque équipe rencontre une seule fois toutes les autres. 

1. Représenter la situation sous forme d'un graphe.

2. Combien d'arêtes ce graphe possède-t-il ? En déduire le nombre de matchs au total pour ce tournoi.  

3. Ce graphe est-il connexe ?  

   

Exercice 2 : Un club de tennis doit sélectionner deux joueurs parmi quatre pour représenter le club à un tournoi national. Les quatre joueurs sont notés A, B, C et D. Pour réaliser la sélection, le club organise des matchs : chaque joueur rencontre les trois autres. 

Régle : 

- Tout match gagné donne un point.
- Tout match perdu enlève un point.  

Les joueurs sélectionnés sont les joueurs ayant obtenu le plus grand nombre de points. On donne le résultat sous la forme d'un graphe orienté. 

![](/Graphes/IMG/ex2.jpg)

Le sens de l'arc A → B indique que le joueur A a battu le joueur B. 

1. Donner le nombre de points de chaque joueur.
2. En déduire les joueurs sélectionnés.  



Exercice 3 : On considère un groupe de dix personnes présentes sur un réseau social, le tableau suivant indique les paires de personnes qui ont une relation d'amitié sur ce réseau social. 

| i    | Amis de i |
| ---- | --------- |
| 1    | 3 -6-7    |
| 2    | 6-8       |
| 3    | 1-6-7     |
| 4    | 5-1       |
| 5    | 4-1       |
| 6    | 1-2-3-7   |
| 7    | 1-3-6     |
| 8    | 2         |
| 9    |           |
| 10   | 4-5       |

1. 1. 1. Représenter cette situation par un graphe dans lequel une arête montre le lien 		amitié.
      2. Ce graphe est-il connexe ? Si non, donner ses composantes connexes.  		
      3. L'adage « les amis de nos mais sont nos amis « est-il vérifié ? Si non, que faudrait-il faire pour qu'il le soit ?  		



Exercice 4 : Tracer les graphes associés aux matrices d'adjacences suivantes :

1. $$
   M1 = \begin{pmatrix}
   0 & 0 & 1 & 1 \\
   0 & 0 & 1 & 0 \\
   1 & 1 & 0 & 1 \\
   1 & 0 & 1 & 0
   \end{pmatrix}
   $$

   

2. $$
   M_2= \begin{pmatrix}
   0&1&0&0&0\\
   0&0&1&1&1\\
   0&1&0&1&0\\
   0&0&1&0&0\\
   1&1&0&1&0
   \end{pmatrix}
   $$

   

3. $$
   M_3 = \begin{pmatrix}
   0&3&4&0\\
   1&0&2&0\\
   3&4&0&1\\
   0&0&1&0
   \end{pmatrix}
   $$

   



Exercice 5 : Écrire la matrice d'adjacence du graphe suivant :

![](/Graphes/IMG/ex4.jpg)



Exercice 6 : Dans le fichier `graphe_adj_eleve.py `, 

1. Ajouter une méthode `afficher()` à la classe `Graphe()`pour afficher le graphe sous la forme suivante :

   

​	0 - > 1 3

​	1 - > 2 3 

​	2 - > 3

​	3 - > 1



​	C'est à dire une ligne par sommet, avec pour chacun la liste de ses voisins. 

1. Ajouter une méthode `degre(s)` à la classe `Graphe()` qui donne le nombre d'arcs issus du sommet s. On appelle cela le degré du sommet s.
2. Ajouter une méthode `supprimer_arc(s1,s2)` pour supprimer l'arc entre les sommets s1 et s2. S'il n'y a pas d'arc, cette méthode n'a aucune effet.  



Exercice 7 : Dans le fichier `graphe_succ_eleve.py` , 

1. Ajouter une méthode `afficher()` à la classe `Graphe()`  pour afficher le graphe sous la forme suivante

   0 {1,3}

   1 {2,3}

   3 {1}

   2 {3}

   

   c'est à dire une ligne  par sommet, avec pour chacun l'ensemble de ses voisins. L'ordre des sommets n'est pas important.  

   

2. Ajouter une méthode `degre(s)` à la classe `Graphe()` qui donne le nombre d'arcs issus du sommet s. On appelle cela le degré du sommet s.

3. Ajouter une méthode `supprimer_arc(s1,s2)` pour supprimer l'arc entre les sommets s1 et s2. S'il n'y a pas d'arc, cette méthode n'a aucune effet.  



Exercice 8: Dans le fichier `graphe_succ_eleve.py` , 

1. ajouter une méthode `chemin(u,v)` à la classe Graphe() qui indique les sommets à parcourir pour rejoindre le sommet u au sommet v. 
2. ajouter une méthode `chemin_pluscourt(u,v)`à la classe Graphe() qui indique le chemin le plus court permettant de rejoindre le sommet u au sommet v. 

Exercice 9: Dans le fichier `graphe_adj_eleve.py `, , 

1. ajouter une méthode `chemin(u,v)` à la classe Graphe() qui indique les sommets à parcourir pour rejoindre le sommet u au sommet v. 
2. ajouter une méthode `chemin_pluscourt(u,v)`à la classe Graphe() qui indique le chemin le plus court permettant de rejoindre le sommet u au sommet v. 



