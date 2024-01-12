# Les algorithmes gloutons.



### I. Le voyageur de commerce.

Un commercial partant de Nancy doit visiter les villes de Metz, Paris, Reims et Troyes et doit revenir à Nancy. 

Voici le tableau des distances routières kilométriques entre ces différentes villes :

​	

|        | Nancy | Metz | Paris | Reims | Troyes |
| ------ | ----- | ---- | ----- | ----- | ------ |
| Nancy  |       | 55   | 303   | 188   | 183    |
| Metz   | 55    |      | 306   | 176   | 203    |
| Paris  | 303   | 306  |       | 142   | 153    |
| Reims  | 188   | 173  | 142   |       | 123    |
| Troyes | 183   | 203  | 153   | 123   |        |

Question 1 : Combien d'itinéraires différents peut-il faire ?



Ce commercial souhaite effectuer le parcours le plus court possible. 



Nous sommes face à un problème d'optimisation : il s'agit non pas de proposer une solution, mais de proposer la meilleure des solutions. 

L'**optimisation** est une branche des mathématiques cherchant à modéliser, à analyser et à résoudre les problèmes qui consistent à minimiser ou maximiser une fonction sur un ensemble. 

Dans notre cas, il s'agit de trouver la distance la plus courte que pourra effectuer le commercial et déterminer le parcours qui lui est associé.



Question 2 : Quel est le parcours le plus court que pourra effectuer le commercial ? Cette solution est-elle unique ?



Une manière simple répondre à la question consiste à lister tous les parcours possibles et à trouver celui qui a la plus courte distance. 



Cette technique, si elle est efficace, ne peut pas être utilisée, car elle est beaucoup trop longue si le nombre de villes devient beaucoup plus important. 

Pour 100 villes, il y a $100 \times  99 \times 98 \times ..\times 2 \times 1$ possibilités, soit $100!= 9.33 \times 10^{57}$ possibilités, ce qui même pour un ordinateur, fait beaucoup de calculs à faire. 

Nous allons donc utiliser pour résoudre ce problème un algorithme glouton. 



## II. Algorithmes gloutons.

Les algorithmes gloutons existent pour résoudre des problèmes d'optimisation. 

Ils correspondent à une solution optimale obtenue en effectuant une suite de meilleur choix pour chaque étape de l'algorithme. A chaque étape, on fait le meilleur choix possible. 



​	Remarques :

- ​	il n'y a pas de retour possible en arrière : quand un choix est fait à une étape, il ne peut pas être modifié ultérieurement.
- ​	Lorsqu'un choix est fait, on tente de résoudre ensuite un problème plus petit.  
- ​	Dans certains cas, cette approche permet d'arriver à un résultat optimum global, mais ça n'est pas toujours vrai.  



Reprenons notre problème du voyageur de commerce et déterminons l'algorithme glouton 	correspondant. 



Question 3 : Supposons que notre commercial ait à effectuer les 4 étapes prévues dans l'exemple ci-dessus. Considérons une liste contenant toutes les destinations à visiter et une table contenant les distances. 
1. 
a. Comment choisissez vous sa première étape ? Que devez vous faire,ensuite, avec la liste des étapes à parcourir ?  
b. Comment choisissez vous sa deuxième étape ?  
c. Quand cet algorithme s'arrête-t-il ?  
d. En procédant ainsi, donner le parcours effectué par le commercial. Que pouvez vous dire ?  

 Supposons maintenant que le commercial ait n  villes à parcourir,  

2. ​	a. écrire un algorithme glouton lui permettant d'obtenir son itinéraire en supposant qu'il veuille le 		parcours le plus court possible.

​			b. Nous souhaitons maintenant programmer cet algorithme en utilisant Python. 

-  Comment pouvez vous représenter tableau_distance ?

-   Quelle fonction peut/doit on faire avant d'écrire la fonction principale ?  	

-  Écrire le code de cet algorithme (vous utiliserez les données de l'exemple précédent).  	



## II. Le problème du rendu de monnaie.

Problème: on veut programmer une caisse automatique pour qu'elle rende la monnaie de façon optimale, c'est-à-dire avec le nombre minimal de pièces et billets. 

​	La valeur des pièces et billets à disposition sont :

​	0,01 – 0,02 - 0,05 - 0,1- 0,20- 0,50 -1- 2 – 5 – 10 – 20 – 50 - 100 et 200. 

On dispose d'autant d’exemplaires qu'on le souhaite de chaque pièce et billet. 



Exemple : Jules veut acheter un objet coûtant 53€ avec un billet de 100€. La caisse doit lui rendre 47€. La meilleure façon de rendre la monnaie est de le faire avec deux billets de 20,un billet de 5 et une pièce de deux euros. 

Exercice :

​	a. Écrire un algorithme glouton du rendu de monnaie. Programmez le en python. 

​	b. Appliquez cet algorithme en considérant que Jules doit payer la somme de 3,68€ avec un 	billet de 		20€. 

​	c. Programmez cet algorithme en python.

​	d. Faire fonctionner votre programme  en considérant que Jules doit payer la somme de 4,59€ 	avec 		un billet de 50€.

​	e. À votre avis, l’algorithme glouton donne-t-il ici toujours la solution optimale ? (Vous pouvez tenter 			une justification)

1. ​	
