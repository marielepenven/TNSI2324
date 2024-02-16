# Exercices: Les arbres. 

### Exercice 1:

![](/Arbres/IMG/arbre_ex1.jpg)

1. Quelle est la racine de cet arbre? 
2. Quelle est la taille de cet arbre? 
3. Quelle est l'arité du nœud 1? 
4. Quelle est l'arité du nœud 7? 
5. Quelle est la profondeur du noeud 4 ? 
6. Quels sont les fils du noeud 5? 
7. Quelle est la hauteur de cet arbre? 
8. Cet arbre est-il un arbre binaire? 



	### Exercice 2: 

![](/Arbres/IMG/arbre_ex2.jpg)

1. Quelle est la racine de cet arbre? 
2. Quelles sont les feuilles de cet arbre? 
3. Quelle est le nœud parent du nœud 7? 
4. Quelle est la taille de cet arbre ? 
5. Quelle est la hauteur de cet arbre? 
6. Quelle est la profondeur du nœud 2? 
7. Cet arbre est-il un arbre binaire ? 
8. De quels nœuds est constitué le sous arbre droit issu du nœud 7? 
9. De quels nœuds est constitué le sous arbre gauche issu du nœud 5? 



## Exercice 3: 

|                     | Arbre 1                                                      | Arbre 2                                                      | Arbre 3                                                      |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|                     | ![](/Arbres/IMG/arbre_1ex_3.jpg) | ![](/Arbres/IMG/arbre_3ex_3.jpg) | ![](/Arbres/IMG/arbre_2ex_3.jpg) |
| Parcours en largeur |                                                              |                                                              |                                                              |
| Parcours préfixe    |                                                              |                                                              |                                                              |
| Parcours infixe     |                                                              |                                                              |                                                              |
| Parcours suffixe    |                                                              |                                                              |                                                              |

Effectuer les parcours en largeur, préfixe, infixe et suffixe des arbres précédents. 

### Exercice 4:

![](/Arbres/IMG/arbre_ex_4.jpg)

1. Cet arbre est-il un arbre binaire de recherche? Justifiez votre réponse. 
2. Insérez les valeurs 2, 12 et 18 dans cet arbre afin qu'il soit toujours un arbre binaire de recherche. 

### Exercice 5: Bac

Les premiers travaux concernant l'aide à la décision médicale se sont développés pendant les années soixante-dix parallèlement à avènement de l'informatique dans le secteur médical. L'arbre de décision est une technique décisionnelle fréquemment employée pour rechercher la meilleure stratégie thérapeutique. L'arbre de décision de cet exercice, présenté ci-dessous, est un arbre binaire que l'on nommera `arb_decision`. 

![](/Arbres/IMG/abre_ex_5.jpg)

Rappels:

- Un arbre binaire est une structure de données qui peut se représenter sous la forme d'une hiérarchie dont chaque élément, appelé nœud, porte une étiquette. 
- Le nœud initial est appelé racine. 
- Chaque nœud d'un arbre binaire possède au plus deux sous-arbres. 
- Chacun de ces sous-arbres est un arbre binaire, appelés sous-arbre gauche et sous-arbre droit. 
- Un nœud dont les sous-arbres sont vides est appelé une feuille. 
- Dans cet exercice, on utilisera la convention suivante: la hauteur d'un arbre binaire ne comportant qu'un nœud est égale à 1. 

Dans l'arbre de décision en présence d'une jaunisse chez un patient:

- un nœud représente un symptôme dont le médecin doit étudier la présence ou l'absence: la répons en peut être que oui ou non. 
- le sous-arbre gauche d'un nœud donné décrit la démarche à adopter si le symptôme est absent,
- le sous-arbre droit d'un nœud donné décrit la démarche à adopter le si symptôme est présent,
- l'étiquette d'une feuille est la maladie induite par le chemin parcouru. 

1. Déterminer la taille et la hauteur de donné en exemple en introduction (arbre de décision en présence d'une jaunisse ).

2. On choisit d'implémenter un arbre binaire à l'aide d'un dictionnaire. 

   ``` python
   arbre_vide={}
   arbre={'etiquette':'valeur',
   		'sag':sous_arbre_gauche,
   		'sad':sous_arbre_droit}
   ```

   Le code ci-dessous représente un arbre selon le modèle précédent. 

   ``` python
   {'etiquette':'a',
   'sag':{'etiquette':'b',
   	'sag':{},
   	'sad':{'etiquette':'d',
   			'sag':{},
   			'sad':{}}},
   'sad':{'etiquette':'f',
   		'sag':{'etiquette':'g',
   				'sag':{}
   				'sad':{}}
   		'sad':{}}}
   ```

   

​	a. A quelle représentation graphique correspond la structure implémentée ci-dessus? 

![](/Arbres/IMG/arbre_2ex_5.jpg)

b. Représenter graphiquement l'arbre correspondant au code ci-dessous. 

``` python
{'etiquette':'H',
'sag':{'etiquette':'G',
	'sag':{'etiquette':'E',
			'sag':{},
			'sad':{}},
	'sad':{'etiquette':'D',
			'sag':{},
			'sad':{'etiquette':'B',
					'sag':{},
					'sad':{}}}},
'sad':{'etiquette':'F',
		'sag':{'etiquette':'C',
				'sag':{}
				'sad':{'etiquette':'A',
						'sag':{},
						'sad':{}}},
		'sad':{}}}
```

3. La fonction `parcours(arb)`cidessous permet de réaliser le parcours des noeuds d'un arbre binaire `arb`donné en argument. 

``` python
def parcours(arb):
	if arb == {}:
		return None
	parcours(arb['sag'])
	parcours(arb['sad'])
	print(arb['etiquette'])
	
```

a. Donner l'affichage après l'appel de la fonction `parcours`avec l'arbre dont une représentation est ci-dessous. 

![](/Arbres/IMG/arbre_3ex_5.jpg)

b. Ecrire une fonction `parcours_maladies(arb)`qui n'affiche que les feuilles de l'arbre binaire non vide `arb`passé en argument, ce qui correspond aux maladies possiblement induites par l'arbre de décision. 

4. On souhaite maintenant afficher l'ensemble des symptômes relatifs à une maladie. On considère la fonction `symptomes(arbres,mal)`avec comme argument `arbre`un arbre de décision binaire et `mal`le nom d'une maladie.

   L'appel de cette fonction sur l'arbre de décision `abr_decision`de l'introduction fournti les affichages suivants. 

   ``` python
   >>> symptomes(arb_decision,"anémie hémolytique")
   symptômes de anémie hémolytique
   splénomégalie
   pas de bilirubine
   conjonctive jaune
   ```

   Pour cela, on modifie la structure précédente en ajoutant une clé `surChemin`qui sera un booléen indiquant si le nœud est sur le chemin de la maladie. 

   La clé `surChemin`est initialisée à `False`pour tous les nœuds. 

   

   ``` python
   arbre={'etiquette':'valeur',
   		'surChemin':False,
   		'sag':sous_arbre_gauche,
   		'sad':sous_arbre_droit}
   ```

   Recopier et compléter les lignes 6,8,14 et 18 du code suivant sur votre copie. 

   

![](/Arbres/IMG/code_ex_5.jpg)

### Exercice 6: Bac

Un arbre binaire de recherche est un arbre binaire pour lequel chaque nœud possède une étiquette dont la valeur est supérieure ou égale à toutes les étiquettes des nœuds de son fils gauche et strictement inférieure à celle des nœuds de sont filles droit. 

On rappelle que:

- sa taille est son nombre de noeuds;
- sa hauteur est le nombre de niveaux qu'il contient. 

Un éditeur réédite des ouvrages. Il doit gérer un nombre important d'auteurs de la littérature. Pour stocker le nom des auteurs, il utilise un programme informatique qui les enregistre dans un arbre binaire de recherche. 

L'arbre vide sera noté `Null`pour les algorithmes de cet exercice. 

Si `A`est un noeud non vide, `valeur(A)`renvoie le nom de l'auteur; `fils_gauche(A)`renvoie le fils gauche du noeud A et `fils_droit(A)`renvoie le fils droit du noeud `A`. 

L'ordre alphabétique est utilisé pour classer le nom des auteurs. 

Par exemple, on a APOLLINAIRE < BAUDELAIRE

Ainsi, pour tout noeud `A`, si `fils_gauche(A)`et `fils_droit(A)`ne sont pas `Null`, on a :

`valeur(fils_gauche(A)) <= valeur(A) < valeur(fils_droit(A))`

Par exemple, l'arbre binaire suivant `A1`est un arbre binaire de recherche:

 ![](/Arbres/IMG/arbre_1ex_6.jpg)

1. a. Recopier et compléter l'arbre binaire de recherche précédent en insérant successivement dans cet ordre les noms suivants:

   DUMAS ; HUGO;ZWEIG;ZOLA

   b. Quelle est la taille de l'arbre obtenu? Quelle est la hauteur de cet arbre? 

   c. Plus généralement, si l'arbre est de hauteur `h`, quel est le nombre maximal d'auteurs enregistrés dans cet arbre en fonction de `h `? 

On définit ici l'équilibre d'un arbre binaire: il s'agit d'un nombre entier positif ou négatif. Il vaut 0 si l'arbre est vide. Sinon, il vaut la différence des hauteurs des sous-arbres gauche et droit de l'arbre. 

Par exemple, si on considère l'arbre suivant que l'on nommera `A2`: 

![](/Arbres/IMG/arbre_2ex_6.jpg)

Son équilibre vaut -1 car sa hauteur de son sous-arbre gauche vaut 1, la hauteur de son sous-arbre droit vaut 2 et 1-2=-1. 

Un arbre est dit équilibré si son équilibre vaut -1, 0 ou 1. 

L'arbre précédent est donc équilibré. 

2. Recopier et compléter l'arbre de ce dernier exemple avec les noms FLAUBERT, BALZAC, PROUST, SAND, WOOLF, COLETTE, CHRISTIE et AUDIARD quitte à modifier l'ordre d'insertion de manière à ce que cet arbre reste équilibré. 

   L'éditeur souhaite utiliser une fonction récursive `recherche_auteur(ABR,NOM)`qui prend en paramaètres `ABR`un arbre binaire de recherche et `NOM`un nom d'auteur. La fonction renvoie `TRUE`si `NOM`est une étiquette de l'arbre `ABR`et `FALSE`dans le cas contraire. 

   On donne la fonction suivante

   ``` python
   Fonction mystere(ABR,t):
   	SI ABR = NULL:
   		RENVOYER FAUX
   	SINON SI valeur(ABR)=t:
   		RENVOYER VRAI
   	SINON:
   		RENVOYER mystere(fils_gauche(ABR,t)ou mystere(fils_droit(ABR),t))
   ```

3. Que renvoie l'appel `mystere(A2,"SIMENON")`? Justifier la réponse. 

   L'éditeur souhaite utiliser une fonction récursive `hauteur(ABR)`qui prend en paramètre un arbre binaire `ABR`et renvoie la hauteur de cet arbre. 

4. Ecrire un algorithme de la fonction `hauteur(ABR)`qui prend en entrée `ABR`un arbre binaire de recherche et renvoie sa hauteur. On pourra avoir recours aux fonctions `MIN(val1,val2)`et `MAX(val1,val2)`qui renvoient respectivement la plus petite et la plus grande valeur entre `val1`et `val2`. 

### Exercice 7: 

La fédération de badminton souhaite gérer ses compétitions à l'aide d'un logiciel. 

Pour ce faire, une structure d'arbre de compétition a été définie récursivement de la façon suivante:

un arbre de compétition est soit l'arbre vide noté $\emptyset$, soit un triplet composé d'une chaîne de caractères appelée valeur d'un arbre de compétition appelé sous-arbre gauche et d'un arbre de compétition appelé sous-arbre droit. 

On représente graphiquement un arbre de compétition de la façon suivante:

![](/Arbres/IMG/arbre_1ex_7.jpg)

Pour alléger la représentation d'un arbre de compétition, on ne notera pas les arbres vides, l'arbre précédent sera donc représenté par l'arbre `A`suivant:

![](/Arbres/IMG/arbre_2ex_7.jpg)

Cet arbre se lit de la façon suivante:

- 4 participants se sont affrontés: Joris, Kamel, Carine et Abdou. Leurs noms apparaissent en bas de l'arbre, ce sont les valeurs de feuilles de l'arbre. 
- Au premier tour, Kamel a battu Joris et Carine a battu Abdou. 
- En finale, Kamel a battu Carine, il est donc le vainqueur de la compétition. 

Pour s'assurer que chaque finaliste ait joué le même nombre de matchs, un arbre de compétition a toutes ces feuilles à la même hauteur. 

Les quatre fonctions suivantes pourront utilisées:

- La fonction `racine`qui prend en paramètre un arbre de compétition `arb`et renvoie la valeur de la racine. 

  Exemple: en reprenant l'exemple d'arbre de compétition présenté ci-dessus, `racine(A)`vaut `"Kamel"`. 

- La fonction `gauche`qui prend en paramètre un arbre de compétition `arb`et renvoie son sous-arbre gauche. 

  Exemple: en reprenant l'exemple d'arbre de compétition présenté ci-dessus, `gauche(A)`vaut l'arbre représenté graphiquement ci-après:

  ![](/Arbres/IMG/arbre_4ex_7.jpg)

- La fonction `droit`qui prend en argument un arbre de compétition `arb`et renvoie son sous-arbre droit. 

  Exemple: en reprenant l'exemple d'arbre de compétition présenté ci-dessus, `droit(A)`vaut l'arbre représenté graphiquement ci-dessous:

  ![](/Arbres/IMG/arbre_5ex_7.jpg)

- La fonction `est_vide`qui prend en argument un arbre de compétition et renvoie `True` si l'arbre est vide et `False`sinon. 

  Exemple: en reprenant l'exemple d'arbre de compétition présenté ci-dessus, `est_vide(A)`vaut `False`. 

Pour toutes les questions de l'exercice, on suppose que tous les joueurs d'une même compétition ont un prénom différent. 

1. a. On considère l'arbre de compétition `B`suivant: 

   ![](/Arbres/IMG/arbre_6ex_7.jpg)

   Indiquer la racine de cet arbre puis donner l'ensemble des valeurs des feuilles de cet arbre. 

   b. Proposer une fonction Python `vainqueur`prenant pour argument un arbre de compétition `arb`ayant au moins un joueur. Cette fonction doit renvoyer la chaîne de caractères constituée du nom du vainqueur du tournoi. 

   Exemple: `vainqueur(B)`vaut `"Lea"`. 

   c. Proposer une fonction Python `finale`prenant pour argument un arbre de compétition `arb`ayant au moins deux joueurs. Cette fonction doit renvoyer le tableau des deux chaînes de caractères qui sont les deux compétiteurs finalistes. 

   Exemple: `finale(B)`vaut `["Lea","Louis"]`

2. a. Proposer une fonction Python `occurences`ayant pour paramètre un arbre de compétition `arb `et le nom d'un joueur `nom`et qui renvoie le nombre d'occurences (d'apparitions) du joueur `nom`dans l'arbre de compétition `arb`. 

   Exemple: `occurences(B,"Anne")`vaut 2. 

   b. Proposer une fonction Python `a_gagne`prenant pour paramètres un arbre de compétition `arb`et le nom d'un joueur `nom`et qui renvoie le booléen `True`si le joueur `nom`a gagné au moins un match dans la compétition représenté par l'arbre de compétition `arb`. 

   Exemple: `a_gagne(B,"Louis")`vaut True. 

3. On souhaite programmer une fonction Python `nombre_matchs`qui prend pour arguments un arbre de compétition `arb`et le nom d'un joueur `nom`et qui renvoie le nombre de matchs joués par le joueur `nom` dans la compétition représentée par l'arbre de compétition `arb`. 

   a. Expliquer pourquoi les instructions suivantes renvoient une valeur erronée. On pourra pour cela identifier le noeud de l'arbre qui provoque une erreur. 

   ``` python
   def nombre_matchs(arb,nom):
   	"""arbre_competition, str -> int """
   	return occurences(arb,nom)
   ```

   

​		b. Proposer une correction pour la fonction `nombre_matchs`. 

4. Recopier et compléter la fonction liste_joueurs qui prend pour argument un arbre de compétition `arb`et qui renvoie un tableau contenant les participants au tournoi, chaque nom ne devant figurer qu'une seule fois dans le tableau. 

   L'opération + à la ligne 8 permet de concaténer deux tableaux. 

   Exemple: Si L1=[4,6,2] et L2=[3,5,1], l'instruction L1+L2 va renvoyer le tableau [4,6,2,3,5,1]. 

   

![](/Arbres/IMG/code_ex_7.jpg)
