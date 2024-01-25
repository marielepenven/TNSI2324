# Algorithme des k plus proches voisins

**Montre moi tes voisins, je te dirais qui tu es.**

Le problème est le suivant: ce fruit est-il une clémentine ou une orange ? 

![](/Algorithmes/IMG/orange_clementine.png)

La question est de pouvoir classer un objet en en connaissant quelques caractéristiques. Nous utiliserons, l'algorithme des k plus proches voisins (k-nn en anglais). 

Cet algorithme permet de prédire la classe d'un élément en fonction de la classe majoritaire de ses k plus proches voisins. C'est un exemple d'algorithme d'apprentissage supervisé. 

## I. Le machine-learning. 

L'apprentissage par une machine s'appelle le machine-learning. 

Visionnez la vidéo suivante jusqu'au moins 14'30 : [Le machine Learning](https://youtu.be/OEJX-q6UOag?si=EaYINvaeZxIKRTP-)

Lire l'article suivant: [Apprentissage automatique — Wikipédia (wikipedia.org)](https://fr.wikipedia.org/wiki/Apprentissage_automatique)



Répondre aux questions suivantes:

1. Comment définiriez vous le machine learning? 
2. De quoi a-t-on besoin pour un apprentissage supervisé? 
3. En quoi les GAFAM ont-ils un intérêt à développer le machine-learning? 

## II. Principe de l'algorithme des k-plus proches voisins. 

Nous allons travailler sur un exemple connu dans le monde du machine learning : le jeu de 	données « iris ».

En 1936, Edgar Anderson a collecté des données sur trois espèces d'iris : « iris setosa », « iris virginica » et « iris versicolor ».  

![](/Algorithmes/IMG/iris_setose.png)

![](/Algorithmes/IMG/iris_virginica.png)

![](/Algorithmes/IMG/iris_versicolor.png)

Pour chaque iris étudié, Anderson a mesuré (en cm) : 

- ​	la largeur des sépales  
- ​	la longueur des sépales  
- ​	la largeur des pétales  
- ​	la longueur des pétales  

Par souci de simplification, nous nous intéresserons uniquement à la largeur et à la longueur 	des pétales. 

Pour chaque iris mesuré, Anderson a aussi noté l'espèce ("iris setosa", "iris versicolor" ou 	"iris virginica")

Vous trouverez 50 de ces mesures dans le fichier iris.csv que vous trouverez sur le git. 

En résumé, vous trouverez dans ce fichier : 

- ​	la longueur des pétales  
- ​	la largeur des pétales  
- ​	l'espèce de l'iris (au lieu d'utiliser les noms des espèces, on utilisera des chiffres : 0 pour "iris setosa", 1 pour "iris versicolor" et 2 pour "iris virginica")  

![](/Algorithmes/IMG/extrait_donnees.png)

Vous devez savoir que ce jeu de données a, aujourd'hui, un intérêt purement pédagogique. En effet, il est exclusivement utilisé par des personnes désirant s'initier aux algorithmes de machine learning.  Avant d'entrer dans le vif du sujet (algorithme knn), nous allons chercher à obtenir une représentation graphique des données contenues dans le fichier iris.csv. 

Faire les questions suivantes:

a. Récupérer le fichier iris.csv, puis enregistrer le. 

b. Représenter graphiquement les données. Télécharger, pour cela,  le fichier placer_les_points_eleve.py. 

Vous utiliserez la fonction  DictReader du module csv pour ouvrir le fichier iris.csv. 

Vous devez obtenir un graphique de ce type. 

![](/Algorithmes/IMG/representation_iris.png)

Nous obtenons des "nuages" de points, on remarque ces points sont regroupés par espèces 	d'iris (pour "iris virginica" et "iris versicolor", les points ont un peu tendance à se mélanger).

Imaginez maintenant qu'au cours d'une promenade vous trouviez un iris, n'étant pas un spécialiste, il ne vous est pas vraiment possible de déterminer l'espèce. 

En revanche, vous êtes capables de mesurer la longueur et la largeur des pétales de cet iris. Partons  du principe qu'un pétale fasse 0,5 cm de large et 2 cm de long. 

Faire les questions suivantes:

a. Placer cette nouvelle donnée sur votre graphique. 

b. De quelle espèce semble être l'Iris que vous venez de rencontrer ?

c. Placer maintenant sur votre graphique un iris dont le pétale a une largeur de 0.75 cm et une longueur 2.5 cm.  A quel problème faites vous face? 

Pour résoudre ce problème, nous allons utiliser l'algorithme dit des "k plus proches voisins". 

En voici la méthode dans notre exemple:

- ​	on calcule la distance entre notre point (largeur du pétale = 0,75 cm ; longueur du pétale = 2,5 cm) et chaque point issu du jeu de données "iris" (à chaque fois c'est un calcul de distance entre 2 points tout ce qu'il y a de plus classique).
- ​	on sélectionne uniquement les k distances les plus petites (les k plus proches voisins).  
- ​	parmi les k plus proches voisins, on détermine quelle est l'espèce majoritaire. On associe à notre "iris mystère" cette "espèce majoritaire parmi les k plus proches voisins".

En prenant k=3, nous obtenons: 

![](/Algorithmes/IMG/representation_iris_cercle.png)

Les 3 plus proches voisins sont à l'intérieur du cercle  : nous avons deux "iris 	setosa" (point rouge) et un "iris versicolor" (point  vert). D'après l'algorithme des "k plus proches voisins", notre "iris mystère" appartient à l'espèce "setosa". 



### III. L'algorithme. 

Le problème est donc le suivant : 

On a un ensemble de classe C. 

Considérons un ensemble E d’éléments dont on connaît les caractéristiques et dont on sait à quelle classe ils appartiennent. 

L'objectif de l'algorithme des k-plus proches voisins est : soit un élément $x$  dont on connaît les caractéristiques, l'algorithme doit établir la classe de cet élément 



​	La première étape consiste à lister les étapes dont l'algorithme va avoir besoin :

- récupérer les données de l'ensemble E.
- établir une distance entre les données de l'ensemble E et l’élément $x$.  	
- sélectionner les k éléments de l'ensemble E dont la distance avec  $x$ est la plus petite.  	
- déterminer à quelle classe appartiennent ces k éléments.  	
- Déterminer la classe majoritaire parmi ces k éléments et en déduire la classe de $x$.  	

La question de la distance est une question difficile. En effet, il existe, en fonction des objets, à comparer, une grande quantité de distance. Dans l'exemple des Iris, on a pu représenter les objets par des points et utiliser la distance euclidienne (celle que l'on mesure habituellement). Mais en fonction des données récoltées, celle-ci ne sera pas nécessairement utilisable et il faudra alors réfléchir à autre chose. 	



Répondre aux questions suivantes:

1. Ecrire l'algorithme des k plus proches voisins en considérant que la fonction distance existe. 

2. Reprenons l'exemple de nos Iris. 

   a. Ecrire une fonction `distance` permettant de calculer la distance entre deux Iris sur le graphique. 

   b.  Ecrire une fonction `knn(inconnu,k,iris_connus)`prenant un paramètre un iris inconnu, le nombre k et un dictionnaire contenant les iris connus et indiquant la nature de l'iris en utilisant ses k plus proches voisins.

   

   

   
