# Les graphes. 


### Introduction: le problème des sept ponts de Königsberg. 

En 1736, la ville de Königsberg (actuelle Kaliningrad en Russie) est construite autour de  deux îles situées sur la Pregel et reliées entre elles par un pont. Six autres ponts relient  les rives de la rivière à l’une ou l’autre des deux îles comme représentés sur la figure ci- dessous. 

![](/Graphes/IMG/ponts_de_konigsberg_et_schéma.jpg)

Les habitants se demandaient s’il existe ou non une promenade dans les rues de  Königsberg permettant, à partir d’un point de départ au choix, de passer une et une  seule fois par chaque pont et de revenir à son point de départ, étant entendu qu’on ne  peut traverser la Pregel qu’en passant sur les ponts. 

Afin de répondre à cette question, nous allons représenter cette carte en matérialisant chaque masse terrestre par un point et chaque pont par un arc. 

![](Graphes/IMG/graphe_ponts.jpg)

Dans ce cas très simple, il est assez intuitif de démontrer que la promenade demandée n'existe pas. 

En effet, il suffit de supposer que la promenade recherchée existe. On peut alors, à partir de la promenade, ordonner les sept arêtes du graphe de façon que deux arêtes consécutives par rapport à notre ordre soient adjacentes dans le graphe (en considérant que la dernière et la première arête sont consécutives, puisqu'il y a retour au point de départ).

Ainsi tout sommet du graphe est-il nécessairement incident à un nombre pair d'arêtes (puisque s'il est incident à une arête il est aussi incident à l'arête précédente ou qui lui succède dans l'ordre). Mais le graphe a des sommets qui sont incidents à trois arêtes, d'où l'impossibilité.

### I. Définitions. 

### a. Sommets, arcs, orientations. 





Un graphe est un ensemble de sommets liés entre eux par des arcs ou des arêtes. 

Prenons l'exemple d'un site web, chaque page forme un sommet et les liens permettant de naviguer d'une page à l'autre constituent les arêtes. 

Chaque sommet (ou nœud) contient une donnée que l'on appelle une étiquette. 

On appelle ordre d'un graphe son nombre de sommets. 

On différencie différents types de graphes:

- les graphes non orientés: les arêtes peuvent parcourues indifféremment dans n'importe quel sens. 

- Les graphes orientés: les arêtes ne peuvent être parcourus que dans une sens donné. On parle alors d'arc. On dit que l'arc (x,y) part du sommet x et arrive au sommet y. 

- Les graphes pondérés: chaque arête porte une valuation, aussi appelée poids ou coût. 

  Dans le cas du protocole OPSF, on utilise des graphes pondérés.

Exemples. 

Graphe 1: 

![](/Graphes/IMG/exemple_1_graphe.jpg)

Considérons le graphe ci-dessus:

il est constitué de l'ensemble des sommets S={a,b,c,e,f} ainsi que de l'ensemble des arêtes

A= {(a,b),(a,e),(b,c),(c,e),(e,f)}. 

C'est un graphe non orienté. 

Graphe 2:

![](/Graphes/IMG/exemple_2_grpahe.jpg)

Graphe 3:

![](/Graphes/IMG/exemple_3_graphe.jpg)

Lorsqu'il existe un arc d'un sommet s vers un sommet t, on dit que t est adjacent ou voisin à s. 

Exemple 2:

Citer l'ensemble des sommets adjacents 

- au sommet c dans le graphe 1. 
- au sommet 3 dans le graphe 2
- au sommet v3 dans le graphe 3. 

### b. Chemin. 

Dans un graphe donnée, un chemin reliant un sommet u à un sommet v est une séquence finie de sommets reliés deux à deux par des arcs et menant de u à v. 

Exemple 2: 

1. Citer un chemin reliant le sommet c au sommet f dans le graphe 1. Ce chemin est-il unique? 

2. Citer un chemin reliant le sommet 4 au sommet 2 dans le graphe 2.

   Existe-t-il un chemin reliant le sommet 2 au sommet 4 dans le graphe 2? 

Une **boucle** est une arête reliant un sommet à lui-même.

Des arêtes multiples sont deux arêtes, ou plus, qui joignent les mêmes sommets.

Un **cycle** est un chemin dans un graphe non orienté dont les deux extrémités sont identiques.

Un graphe simple est un graphe ne contenant ni boucle, ni arêtes multiples. 
 Le **degré** d’un sommet est le nombre d’arêtes incidentes à ce sommet, c’est-à-dire ayant ce sommet pour extrémités, les boucles étant comptées deux fois. 
 Un sommet de degré zéro est dit isolé.

La longueur d’un chemin est définie comme le nombre *d’arcs* qui constituent le chemin. 
 La **distance** entre deux sommets est la longueur du plus court chemin reliant ces deux sommets.

Exemple 4: 

- Indiquer l'ordre du sommet 3 pour le graphe 2. 
- Quelle est la distance entre les sommets b et f dans le graphe 1? 

On dit qu'un graphe non orienté est connexe si pour toute paire de sommets, il existe un chemin de u à v. 

Exemple 4:

graphe connexe:

![](/Graphes/IMG/graphe_connexe.jpg)

graphe non connexe: 

![](/Graphes/IMG/graphe_non_connexe.jpg)

#### c. Successeurs et prédécesseurs. 

L’ensemble des **successeurs** d’un sommet u est l’ensemble des sommets v tels qu’il existe une arête allant de u vers v.

L’ensemble des **prédécesseurs** d’un sommet u est l’ensemble des sommets v tels qu’il existe une arête allant de v vers u.

Exemple : Donner l'ensemble des successeurs et des prédecesseurs pour le graphe 2. 



## II. Implémentation d'un graphe. 

1. Il existe de multiples façons de représenter un graphe en machine, selon la nature du graphe, mais aussi selon la nature des opérations et des algorithmes à effectuer sur ce graphe.  

2. Nous en verrons deux.  

### a. Matrice d'adjacence. 

Une matrice est un tableau en deux dimensions dans lequel sont contenus des nombres.

Exemple:

$$ \begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix} $$


Nous noterons` mat[i][j]`l'élément de la i-éme ligne et de la j-iéme colonne de cette matrice,

i et j commençant à zéro (pour coller à ce que nous implémenterons à l'aide des tableaux). 

Exemple :

Déterminer les valeurs de `mat[0][2]`, `mat[1][0]`et `mat[2][2]`. 



Un graphe peut être représenté par un ensemble de sommet et par une matrice d'adjacence :

- s'il y a un lien entre le sommet i et le sommet j, on pose alors `mat[i][j]=1` ou `mat[i][j]= True .` Si le graphe est pondéré, on indique la valuation de l'arête. 
- s'il n'y  a pas de lien entre le sommet i et le sommet j, on pose alors `mat[i][j]=0` ou `mat[i][j]=False`

Exemple: Construire les matrices d'adjacences des graphe 1, 2 et 3. Nous considérerons les sommets dans l'ordre croissant ou dans l'ordre alphabétique. 







Remarque: Lorsqu'un graphe est non orienté, la matrice d'adjacence est symétrique. 



La matrice d'adjacence est simple à mettre en place mais elle possède quelques défauts:

- elle occupe un espace mémoire proportionnel à $N \times N$ , où N est l'ordre du graphe. 
- pour parcourir la liste des voisins d'un sommet, il est nécessaire de parcourir toute une ligne de la matrice, alors même qu'il peut n'y avoir que très peu de voisins. 
- Elle limite le nombre de sommets à un nombre connu d'avance. 

Pour pallier à ces défauts, nous pouvons utiliser le modèle suivant.

### b. Dictionnaire d'adjacence. 

Dans cette nouvelle représentation, un graphe est un dictionnaire qui associe à chaque sommet l'ensemble de ses voisins.  On appelle cela un dictionnaire d'adjacence. 

On peut aussi utiliser la liste de prédécesseurs. Ces deux listes sont identiques dans un graphe non orienté : liste des voisins. Dans le cas d’un graphe pondéré, les listes sont remplacées par des dictionnaires.

Le graphe est alors un dictionnaire de dictionnaires : le dictionnaire de successeurs a pour clés les étiquettes des sommets successeurs et pour valeurs les valuations des arêtes associées

Exemple: Construire les dictionnaires d'adjacence des graphe 1, 2 et 3. 

### c. Implémentation. 

Compléter les codes des deux fichiers python `graphe_adj_eleve.py` et `graphe_succ_eleve.py` 	afin d'implémenter la structure de graphe. 

Tester votre code sur les exemples vus dans le cours. 

## III. Algorithmes sur les graphes. 

L'idée du parcours est de visiter tous les sommets d'un graphe en partant d'un sommet quelconque. Ces algorithmes de parcours de graphe sont à la base de nombreux algorithmes très utilisés: routage des paquets de données dans un réseau, découverte du chemin le plus court pour aller d'une ville à une autre....

#### a. Parcours en largeur. 

Aussi appelé BFS (Breath-First Search), le parcours en largeur explore un graphe à partir d'un sommet A donné, en s'éloignant progressivement de A. Plus précisement, il consiste à explorer d'abord tous les voisins de A, puis les voisins de chacun de chacun de ces voisins (qui n'ont pas encore été visités), et ainsi de suite. 

Cela permet d'explorer systématiquement les chemins entre chaque sommet d'un graphe, par exemple, pour en déterminer les distances relatives. 

![](/Graphes/IMG/parcours_largeur.jpg)

Remarque: Si le graphe est non connexe, on ne peut pas franchir tous ses sommets, et de même s'il est connexe et orienté, on peut ne pas les rencontrer tous. 

L'algorithme s'implémente avec une file. Nous utiliserons une fonction marquer permettant d'indiquer si un sommet a déjà été visité ou non. 

``` python
ParcoursLargeur(Graphe G, Sommet s):
	F = File() # créer une file permettant de visiter le Graphe de proche en proche
	F.enfiler(s)
	marquer(s)
	Sommets = File() # créer une file que l'on va retourner avec les sommets visités
	Sommets.enfiler(s)
	tant que la file est non vide:
		s = F.defiler()
		afficher(s)
		Pour tout voisin t de s dans G:
			si t est non marqué:
				F.enfiler(t)
				marquer(t)
				Sommets.enfiler(t)
	Renvoyer Sommets
```



Exemple: 

1. Appliquez cet algorithme au graphe ci-dessous en partant de A. On notera sur une même ligne le nœud actuellement visité et le contenu de la file f.

![](/Graphes/IMG/graphe1_parcours_largeur.jpg)

2. Faire un tableau des distances entre A et les autres nœuds.

3.  Qui a-t-il de remarquable entre ce tableau et le parcours en largeur ?

4. Appliquez à nouveau cet algorithme au graphe ci-dessous en prenant A comme nœud initial.

![](/Graphes/IMG/grpahe2_parcours_largeur.jpg)

#### b. Parcours en profondeur. 

Aussi appelé DFS (Depth-First Search), le parcours en profondeur explore un graphe en suivant chaque chemin le plus loin possible puis, lorsqu'il rencontre un "cul de sac " (un sommet qui n'a d'arcs que vers des sommets déjà visités), revient en arrière vers le sommet précédent disposant d'arcs non visités, et recommence. 

Cela permet, par exemple, de déterminer rapidement s'il existe un cycle dans un graphe ou de trouver le plus court chemin entre deux sommets. 

L'algorithme s'implémente avec une pile. Nous utiliserons une fonction marquer permettant d'indiquer si un sommet a déjà été visité ou non. 

``` python
explorer(graphe G, sommet s)
	Sommets=Pile()
	Sommets.empiler(s)
	marquer(s)
	pour tout sommet t voisin du sommet s
		si t n'est pas marqué:
			explorer(G,t)
	Renvoyer Sommets
```

Exemple: 

1. Appliquez cet algorithme au graphe ci-dessous en partant de A. 

  ![](/Graphes/IMG/graphe1_parcours_largeur.jpg)

2. Appliquez cet algorithme au graphe ci-dessous en partant de A. 

  ![](/Graphes/IMG/grpahe2_parcours_largeur.jpg)





#### c. Chercher un chemin. 

Il est parfois nécessaire de trouver un chemin entre deux sommets d'un graphe, voici un algorithme qui permet de faire cette recherche.

``` python
trouve_chemin(graphe_G, sommet_debut,sommet_fin,chaine=[]):
	ajouter sommet_debut à chaine
	si sommet_debut=sommet_fin:
		renvoyer chaine
	sinon:
		pour tout v voisin de sommet_debut:
			si v n'appartient pas à chaine:
				chemin = trouve_chemin(graphe_G,v,sommet_fin,chaine)
				si chemin est non_vide:
					renvoyer chemin
		renvoyer None

```

Exemple: 

Appliquer cet algorithme à la recherche d'un chemin entre A et C aux graphes ci-dessous. 

![](/Graphes/IMG/graphe1_parcours_largeur.jpg)

![](/Graphes/IMG/grpahe_2_parcours_largeur.jpg)



#### d. Détection d'un cycle. 

Un **cycle** est un chemin dans un graphe non orienté dont les deux extrémités sont identiques.

Pour pouvoir détecter si un graphe possède au moins un cycle, nous pouvons utiliser l'algorithme suivant:

``` python
trouve_cycle(graphe G, sommet s):
	pile = Pile()
	pile.empiler(s)
	tant que pile n'est pas vide:
		x  = pile.depile()
		pour chaque v voisin de x:
			si v n'est pas marqué:
				pile.empile(v)
			si x est marqué:
				renvoyer Vrai
			sinon:
				marquer(x)
	renvoyer Faux
```

Exemple: Appliquer cet algorithme aux deux graphes ci-dessous en prenant A comme noeud initial. 

![](/Graphes/IMG/graphe1_parcours_largeur.jpg)

![](/Graphes/IMG/grpahe_2_parcours_largeur.jpg)

### e. Implémentons. 

Reprenez les deux fichiers python `graphe_adj_eleve.py` et `graphe_succ_eleve.py` et ajouter trois méthodes : 

- `marquer(sommet)`permettant de marquer le sommet d' un graphe. (Vous aurez peut être besoin de modifier votre implémentation de graphe en ajoutant un attribut à chaque sommet)
- `parcours_largeur(graphe,sommet)`permettant de parcourir en largeur un graphe. 
- `parcours_profondeur(graphe,sommet) `permettant de parcourir en longueur un graphe. 

