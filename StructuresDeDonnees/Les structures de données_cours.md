### Les structures de données.



## I. Généralités.





​	En informatique, une variable a un nom et correspond à de l'information placée en 	mémoire. 



​	Le type de donnée ou plus simplement le type est contenu dans cette information : 		une valeur appartenant à un ensemble précis. : entier, flottant, chaîne de caractères, 		…



​	Afin d'organiser ou de traiter des données, on peut définir une structure de données. 

​	Celle-ci peut regrouper des objets de types différents et permet de stocker les 			données d'une manière particulière. 



​	Par exemple, en Python, il existe les tuples, les listes et les dictionnaires. 



​	Ce sont des types abstraits de données. 



​	Un type abstrait est caractérisé par une interface de programmation, c'est à dire un ensemble 	d'opérations qui permettent de manipuler les données de ce type. 

​	On distingue :

  - les constructeurs qui 	permettent de créer une nouvelle structure de données ;
  - les opérateurs, qui 	permettent de modifier la structure de données, par exemple en 	ajoutant ou en retirant des données,
  - les accesseurs qui 	donnent des informations sur la structure de données, comme par 	exemple son nombre d’éléments.  	
  - Les itérateurs qui 	permettent d'énumérer les éléments de la structure de données. 			





​	Spécifier un type abstrait, c'est définir son interface. 



​	Implémenter un type abstrait, c'est fournir le code de ces opérations en utilisant des types 	existants. 

​	Plusieurs implémentations peuvent répondre à une même spécification. Le programmeur 	peut alors choisir celle qui lui convient le mieux. 



​	Une structure de données a plusieurs caractéristiques. 

  - Structure linéaire ou 	non linéaire. Lorsque les éléments sont ordonnés, s'il y a une 	chronologie, on parle de structure linéaire.
  - Structure homogène ou 	non homogène. Les éléments sont tous du même type ou pas. Cela 	peut poser des problèmes suivants que le typage est statique ou 	dynamique.  	
  - Structure statique ou 	dynamique. La taille est fixée et ne peut pas être modifiée ou 	elle peut varier suivant les besoins.  	



​	Nous allons étudier, cette année, les listes chaînées, les piles, les files, les arbres et les 	graphes. 


## II. Les listes chaînées.


### 1. Les listes en python.

​	Nous avons vu, en classe de première, une structure de donnée en python, appelée `list`. 



​	Nous avons vu un certain nombre de méthodes associées à cette structure :

​	append, pop, remove, len, …..

​	Nous avons appris à utiliser l'interface liée au type list mais nous n'en connaissons pas 	l'implémentation. 
Le type `list` est, en réalité, un tableau dynamique. C'est à dire qu'il place tous les éléments de notre liste dans  des emplacements de mémoire contigus.  
![](/StructuresDeDonnees/img/tableau.jpg)

​
​	Le tableau étant dynamique, l'insertion d'un nouvel élément dans la liste est possible, il faut 	néanmoins décaler tous éléments à droite pour faire de la place au nouvel élément. Cela 	prend beaucoup de temps si l’élément ne doit pas être inséré à la fin du tableau. 

![](/StructuresDeDonnees/img/tableaumodif.jpg)
​	

​	
​	Imaginons une structure de liste qui pourrait insérer un élément en temps constant. 



### 2. Les listes chaînées.



​	Une liste chaînée permet de représenter une liste, c'est à dire une séquence finie de valeurs.

​	Comme le nom le suggère, sa structure est caractérisé par le fait que les éléments sont 	chaînés les uns aux autres, permettant le passage d'un élément au suivant. 



​	Ainsi, chaque élément est stocké dans un petit bloc alloué quelque part dans la mémoire, que 	l'on pourra appeler maillon ou cellule, et y est accompagné d'une deuxième information : 	l'adresse mémoire où se trouve la cellule contenant l’élément suivante de la liste. 

​	
![](/StructuresDeDonnees/img/cellule.jpg)

Les cellules forment ainsi une liste chainée. 

![](/StructuresDeDonnees/img/listechainee.jpg)
​	

​	Pour insérer un élément, il suffit de changer deux « pointeurs » : 
![](/StructuresDeDonnees/img/insererlistechainee.jpg)


​	

## III.  Les Piles.


​	Un pile est un ensemble ordonnée d’éléments qui se comporte comme une pile d'assiettes : 	on peut ajouter une assiette sur la pile ou prendre l'assiette sur le dessus de la pile. 
	

​![](/StructuresDeDonnees/img/imagepile.jpg)



​	C’est la règle du dernier entré premier sorti : LIFO (*Last In First Out*).



​	Exemple :

  - Lors 	de la navigation sur le web, les url des pages visitées sont 	stockées dans une pile.
  - La 	fonction «Annuler la frappe» (en anglais «Undo») d’un 	traitement de texte mémorise les modifications apportées au texte 	dans une pile.  	



​	Son interface minimale est la suivante : 

- `creer_pile()` : son constructeur qui retourne une pile vide ;
- `pile_vide(P)` :indique True si la pile P est vide et False sinon ;
- `empiler(P,x,)` : ajoute l’élément x au sommet de la pile P (en anglais, on dirai push(P,x)
- `dépiler(P)`  : retire, s 'il existe, le dernier élément de la pile P (en anglais, on dirait pop(P,x)



​	Exemple :

​	Considérons une classe Pile() dans laquelle les méthodes ci-dessus auraient été implémentées.

​	Donner le contenu de mapile à chaque étape :
	``` python

         mapile = Pile()   

        mapile.empile('Zoe')

        mapile.empile('Luc')

        mapile.empile('Sofian')

        mapile.empile('Agathe')

        mapile.depile()

        mapile.depile()

        mapile.empile('Louis')

        mapile.depile()
	 ```



​	En python, il est possible d'utiliser différentes structures afin d'implémenter une pile :
	- les tuples
 	- les list (python)
 	- les listes chaînées.  	





## IV.  Les files.



​	Une file est un ensemble ordonné d’éléments qui se comporte comme une file d'attente : un nouvel arrivant se met à la fin 	de la file, tandis que la prochaine personne servie est celle en tête de file. 

	​![](/StructuresDeDonnees/img/imagefile.jpg)



​	C'est la règle du premier arrivé, premier servi : FIFO (First In, First Out). 


​	Exemple : Elles sont utilisées lors, par exemple, de l'envoi d'instruction à un processeur. 

​	Son interface minimale est la suivante : 

	- `creer_file()` : son constructeur qui retourne une file vide ;
	- `file_vide(F)` :indique True si la file F est vide et False sinon ;
	- `enfiler(F,x)` : ajoute l’élément x à la fin de la file F.  
	- `défiler(F)` : retire, s 'il existe, le premier élément de la pile F.  


​	Exemple :

​	Considérons une classe File dans laquelle les méthodes ci-dessus auraient été implémentées.

​	Donner le contenu de mafile à chaque étape :

	```python

​		mafile = File()

​		mafile.file_vide()

​		mafile.enfiler('Coucou')

​		mafile.enfiler('Ca')

​		mafile.enfiler('Va')

​		mafile.defiler()

​		mafile.enfiler('Bien')

​		mafile.defiler()

​		mafile.defiler()

​		mafile.defiler()
	```


​	

​	Il est possible d'utiliser plusieurs méthodes pour les implémenter :

	 -les listes python
  	- deux 	piles. 
   



## V. Les dictionnaires.

	Un dictionnaire, en informatique,  est une structure de données qui associe des clés à des 	valeurs. 

​	Cela se rapproche très fortement de la définition classique d'un dictionnaire tel que nous le 	connaissons : à un mot 		(la clé), on associe sa définition (la valeur). 



​	L'interface minimale d'un dictionnaire est la suivante :

	 - `creer_dico()` : 	son constructeur qui retourne un dictionnaire vide.
 	 - `ajouter(d,cle,valeur)` : 	opérateur qui ajoute cle au dictionnaire et l'associe à valeur.  	
 	 - `valeur_cle(d,cle)` : 	accesseur qui retourne la valeur associée à cle, si elle est 	présente.  	
 	 - `cles_dico(d)` : 	itérateur qui énumère les clés du dictionnaire.  	
 	 - `supprime(d,cle)` : 	supprime la clé et la valeur associée du dictionnaire.  	



​	Exemple :

​	Considérons une classe dictionnaire  dans laquelle les méthodes ci-dessus auraient été 	implémentées.

​	Donner le contenu de mondic à chaque étape ou la valeur obtenue :

	```python

​	mondic=creer_dico()

​	modic.ajouter('seconde ',8)

​	mondic.ajouter('premiere',7)

​	mondic.ajouter('terminale',6)

​	mondic['seconde']

​	mondic.supprime('premiere')

​	mondic.cles_dico()
	```



​	Le langage python fournit directement le type structuré dict qui implémente un dictionnaire :
	- `creer_dico()` : 	`d = dict()` ou `d={}`
	- ajouter(d,cle,valeur) : 	`d[cle]=valeur`
 	- valeur_cle(d,cle) : 	`d[cle]`
 	- cles_dico(d) : 	`for cle in d :`
  	- supprime(d,cle) : 	`del d[cle]`







​	









​	



​	

​	

​	



​	
