# Programme en tant que données. 

## I. Programmes et données. 

Une particularité de l'architecture de Von Neumann est d'utiliser la même mémoire pour stocker le programme en cours d'exécution et les données qu'il manipule. Rien n'empêche donc un programme de produire comme résultat le code d'un autre programme, puis d'exécuter celui-ci. 

De même, un programme peut accéder au code d'un autre programme comme s'il s'agissait de données, par exemple, pour l'analyser ou pour le transformer en un autre programme. 

On peut distinguer deux grands types de langages : les langages *interprétés* et les langages *compilés*. On a par exemple:

- langages interprétés : Java (+ JavaScool) et Python ;
- langages compilés : C, C++, Pascal et OCaml.

## a. les langages interprétés. 

Dans ces langages, le code source (celui que vous écrivez) est interprété, par un logiciel qu'on appelle *interpréteur*. Celui-ci va utiliser le code source et les données d'entrée pour calculer les données de sortie :

![](/Calculabilite_decidabilite/IMG/langage_interprete.png)

L'interprétation du code source est un processus « pas à pas » : l'interpréteur va exécuter les lignes du code une par une, en décidant à chaque étape ce qu'il va faire ensuite.

### b. Les langages compilés. 

Dans ces langages, le code source (celui que vous écrivez) est tout d'abord compilé, par un logiciel qu'on appelle *compilateur*, en un *code binaire* qu'un humain ne peut pas lire mais qui est très facile à lire pour un ordinateur. C'est alors directement le système d'exploitation qui va utiliser le code binaire et les données d'entrée pour calculer les données de sortie :

![](/Calculabilite_decidabilite/IMG/langage_compile.png)

### c. Les différences. 

On pourrait discuter très longtemps des avantages et inconvénients des différents types de langages mais les deux points qui sont les plus intéressants sont les suivants :

- Dans un langage interprété, le même code source pourra marcher directement sur tout ordinateur. Avec un langage compilé, il faudra (en général) tout recompiler à chaque fois ce qui pose parfois des soucis.
- Dans un langage compilé, le programme est directement exécuté sur l'ordinateur, donc il sera en général plus rapide que le même programme dans un langage interprété.



## II. Calculabilité, décidabilité. 

### 

[L' Entscheidungsproblem ou la fin des mathématiques ? | Voyages au pays des maths | ARTE (youtube.com)](https://www.youtube.com/watch?v=Zci9m08HQws)

### a. Calculabilité. 

La calculabilité est la discipline qui étudie ce qu'il est possible ou non de résoudre grâce à l'outil informatique quels que soient le type ou les performances de la machine utilisée. Il s'agit d'informatique théorique, directement issue de la logique mathématique. 

Une fonction calculable est une fonction qui peut être définie par un algorithme. 

Plusieurs modèles de calcul sont utilisés en calculabilité:

- les automates cellulaires,
- les fonctions récursives
- le lambda-calcul
- les machines de Turing: [La Machine de Turing réalisée - Vidéo Dailymotion](https://www.dailymotion.com/video/xrn0yi)

Quelque soit le modèle de calcul utilisé, la classe de fonctions calculables par ceux-ci est unique. 

### b. Décidabilité. 

En algorithmique, un problème de décision est une question à laquelle on répond par oui ou par non. On dit qu’un problème est décidable s’il existe un algorithme, c’est-à-dire une méthode qui se termine en un nombre fini d’étapes, qui permet de répondre par oui ou par non à la question posée par le problème. Sinon on dit que le problème est indécidable.

 Hilbert a posé en 1928 la question en logique mathématique qu’on appelle le problème de la décision, en allemand «Entscheidungsproblem ». Peut-on déterminer par un algorithme si un énoncé quelconque est vrai ou faux, si c’est un théorème?

### c. L'indécidabilité du problème de l'arrêt. 

En théorie de la calculabilité, le problème de l'arrêt consiste, étant donné un programme informatique quelconque, à dire s'il finira par s'arrêter. 

https://youtu.be/92WHN-pAFCs

C’est Alan Turing qui, en 1936, dans le cadre de son fameux article « On Computable Numbers, with an Application to the Entscheidungsproblem », démontre le théorème de l’indécidabilité du problème de l’arrêt qui s’énonce ainsi : Le problème de l’arrêt est indécidable.

Ce résultat met définitivement fin à tout espoir d’automatiser de façon algorithmique le calcul de n’importe quelle fonction. C’est ce qui fait son importance, à la fois historique, scientifique et philosophique

Démontrons l'indécidabilité du problème de l'arrêt. 

Donnée : le couple constitué d’un programme Python $\pi$  pour une fonction $f$ qui prend un argument, et d’une valeur $x$ pour cet argument 

Réponse : décider si le calcul de $f(x)$ par le programme termine ou ne termine pas. 

Démontrons par l'absurde le problème de l'arrêt. 

Supposons qu'il existe un programme python qui décide du problème de l'arrêt. 

```python
def testArret(programme,x):
	.........
    if .......: 
        # si le programme s'arrête sur l'entrée x
        return True
    else: 
        return False
```

On définit alors le programme suivant:

```python
1. def testSurSoi(programme):
2. 	if testArret(programme,programme):
3. 		while True:
4. 			continue
5. 	else:
6. 		return True
```

Nous effectuerons l'appel `testSurSoi(testSurSoi)`. 

- soit cet appel se termine, ce qui signifie qu’on n’est pas entré dans la boucle infinie des lignes 3–4. Mais alors cela signifie que l’appel `testArret(testSurSoi,testSurSoi)`a renvoyé la valeur `False`, ce qui ne peut arriver que si l’appel `testSurSoi(testSurSoi)`ne termine pas: c’est contradictoire;
-  ou bien cet appel ne termine pas, ce qui signifie qu’on est entré dans la boucle. Cela ne peut arriver que si l’appel `testSurSoi(testSurSoi)` termine : c’est contradictoire.



 On aboutit dans tous les cas à une contradiction, ce qui achève notre démonstration par l’absurde!
