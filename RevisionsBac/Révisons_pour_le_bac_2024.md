# Révisons pour le bac. 

## Exercice 1: 

*Cet exercice porte sur l’architecture matérielle, les réseaux, les routeurs et les  protocoles de routage.*

 On considère un réseau local N1 constitué de trois ordinateurs M1, M2, M3 et dont  les adresses IP sont les suivantes : 

- M1 : 192.168.1.1/24 ; 

-  M2 : 192.168.1.2/24 ; 

-  M3 : 192.168.2.3/24. 

  

On rappelle que le “/24” situé à la suite de l’adresse IP de M1 signifie que l’adresse  réseau du réseau local N1 est 192.168.1.0.

Depuis l’ordinateur M1, un utilisateur exécute la commande ping vers l’ordinateur M3  comme suit :

```
 util@M1 ~ % ping 192.168.2.3
 PING 192.168.2.3 (192.168.2.3): 56 data bytes
 Hôte inaccessible
```

1. Expliquer le résultat obtenu lors de l’utilisation de la commande ping (on part du principe que la connexion physique entre les machines est fonctionnelle). 

 On ajoute un routeur R1 au réseau N1 :

“Un routeur moderne se présente comme un boîtier regroupant carte mère,  microprocesseur, ROM, RAM ainsi que les ressources réseaux nécessaires (Wi-Fi,  Ethernet…). On peut donc le voir comme un ordinateur minimal dédié, dont le  système d’exploitation peut être un Linux allégé. De même, tout ordinateur disposant  des interfaces adéquates (au minimum deux, souvent Ethernet) peut faire office de  routeur s’il est correctement configuré (certaines distributions Linux minimales  spécialisent la machine dans cette fonction).” 

Source : Wikipédia, article “Routeur”

2. Définir l’acronyme RAM. 
3. Expliquer le terme Linux. 
4. Expliquer pourquoi il est nécessaire d’avoir “au minimum deux” interfaces réseau dans un routeur.

Le réseau N1 est maintenant relié à d’autres réseaux locaux (N2, N3, N4) par  l’intermédiaire d’une série de routeurs (R1, R2, R3, R4, R5, R6) :

![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex1_revisions_2024.jpg)

5. Attribuer une adresse IP valide à l’interface eth0 du routeur R1 sachant que l’adresse réseau du réseau N1 est 192.168.1.0.

Dans un premier temps, on utilise le protocole de routage RIP (Routing Information  Protocol). On rappelle que dans ce protocole, la métrique de la table de routage  correspond au nombre de routeurs à traverser pour atteindre la destination. 

 La table de routage du routeur R1 est donnée dans le tableau suivant :

Table de routage du routeur R1. 

| destination | interface de sortie | métrique |
| ----------- | ------------------- | -------- |
| N1          | eth0                | 0        |
| N2          | eth1                | 2        |
| N2          | eth2                | 4        |
| N3          | eth1                | 3        |
| N3          | eth2                | 3        |
| N4          | eth1                | 1        |
| N4          | eth2                | 3        |

6.  Déterminer le chemin parcouru par un paquet de données pour aller d’une machine appartenant au réseau N1 à une machine appartenant au réseau N2.

Le routeur R3 tombe en panne. Après quelques minutes, la table de routage de R1  est modifiée afin de tenir compte de cette panne.

7. Dresser la table de routage du routeur R1 suite à la panne du routeur R3. 

 Le routeur R3 est de nouveau fonctionnel. Dans la suite de cet exercice, on utilise le  protocole de routage OSPF (Open Shortest Path First). On rappelle que dans ce  protocole, la métrique de la table de routage correspond à la somme des coûts :

coût=$\frac{10^8}{d}$ où d est la bande passante d'une liaison en bit/s. 

 Le réseau est constitué de 3 types de liaison de communication : 

- Fibre avec un débit de 1 Gbit/s ; 
-  Fast-Ethernet avec un débit de 100 Mbit/s ; 
- Ethernet avec un débit de 10 Mbit/s.

8. Calculer le coût de chacun de ces liaisons de communication. 

La table de routage du routeur R1 est donnée dans le tableau suivant:

Table de routage du routeur R1. 

| destination | interface de sortie | métrique |
| ----------- | ------------------- | -------- |
| N1          | eth0                | 0        |
| N2          | eth1                | 10.1     |
| N2          | eth2                | 1.3      |
| N3          | eth1                | 11.3     |
| N3          | eth2                | 0.3      |
| N4          | eth1                | 10       |
| N4          | eth2                | 1.2      |

 D’autre part, le type des différentes liaisons inter-routeurs sont les suivantes : 

-  R1 - R2 : Fibre ; 
- R1 - R3 : Ethernet ; 
-  R2 - R6 : INCONNU ; 
- R3 - R6 : Fast-Ethernet ; 
-  R3 - R4 : Fibre ; 
- R4 - R5 : Fast-Ethernet ; 
- R5 - R6 : Fibre.

9. Déduire de la table de routage de R1 et du schéma du réseau le type de la  liaison inter-routeur R2 - R6. 

 Des travaux d’amélioration ont été réalisés sur ce réseau : la liaison inter-routeur R1 R3 est désormais de type Fibre. 

10. Modifier la table de routage de R1 en tenant compte de cette amélioration.

 On ajoute un réseau local N5 et un routeur R7 au réseau étudié ci-dessus. Le routeur  R7 possède trois interfaces réseaux eth0, eth1 et eth2. eth0 est directement relié au  réseau local N5. eth1 et eth2 sont reliés à d’autres routeurs (ces liaisons inter-routeur  sont de type Fibre).

 Les deux tableaux suivants présentent un extrait des tables de routage des routeurs  R1 et R3 :

Extrait table de routage du Routeur R1. 

| destination | interface de sortie | métrique |
| ----------- | ------------------- | -------- |
| ...         | ...                 | ...      |
| N5          | eth1                | 1.2      |
| N5          | eth2                | 0.2      |

Extrait table de routage du routeur R3. 

| destination | interface de sortie | métrique |
| ----------- | ------------------- | -------- |
| ...         | ...                 | ...      |
| N5          | eth1                | 1.3      |
| N5          | eth2                | 1.1      |
| N5          | eth3                | 0.3      |

11. Recopier et compléter le schéma du réseau (Figure. 1) en ajoutant le routeur  R7 et le réseau local N5. 

## Exercice 2: 

*Cet exercice porte sur les graphes, les algorithmes sur les graphes, les bases de  données et les requêtes SQL.*

 La société CarteMap développe une application de cartographie-GPS qui permettra  aux automobilistes de définir un itinéraire et d’être guidés sur cet itinéraire. Dans le  cadre du développement d’un prototype, la société CarteMap décide d’utiliser une  carte fictive simplifiée comportant uniquement 7 villes : A, B, C, D, E, F et G et 9  routes (toutes les routes sont considérées à double sens).

 Voici une description de cette carte : 

- A est relié à B par une route de 4 km de long ; 
-  A est relié à E par une route de 4 km de long ; 
- B est relié à F par une route de 7 km de long ; 
-  B est relié à G par une route de 5 km de long ; 
-  C est relié à E par une route de 8 km de long ; 
-  C est relié à D par une route de 4 km de long ; 
-  D est relié à E par une route de 6 km de long ; 
-  D est relié à F par une route de 8 km de long ; 
-  F est relié à G par une route de 3 km de long. 

1. Représenter ces villes et ces routes sur sa copie en utilisant un graphe  pondéré, nommé G1. 
2. Déterminer le chemin le plus court possible entre les villes A et D. 
3. Définir la matrice d’adjacence du graphe G1 (en prenant les sommets dans  l’ordre alphabétique).

 Dans la suite de l’exercice, on ne tiendra plus compte de la distance entre les  différentes villes et le graphe, non pondéré et représenté ci-dessous, sera utilisé :

![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex2_revisions_2024.jpg)

 Chaque sommet est une ville, chaque arête est une route qui relie deux villes.

4. Proposer une implémentation en Python du graphe G2 à l’aide d’un  dictionnaire.
5.  Proposer un parcours en largeur du graphe G2 en partant de A. 

 La société CarteMap décide d’implémenter la recherche des itinéraires permettant de  traverser le moins de villes possible. Par exemple, dans le cas du graphe G2, pour  aller de A à E, l’itinéraire A-C-E permet de traverser une seule ville (la ville C), alors  que l’itinéraire A-H-G-E oblige l’automobiliste à traverser 2 villes (H et G).

 Le programme Python suivant a donc été développé (programme p1) :

```python
1  tab_itineraires=[]
2  def cherche_itineraires(G, start, end, chaine=[]):
3		chaine = chaine + [start]
4       if start == end:   
5           return chaine
6       for u in G[start]:
7            if u not in chaine:   
8				nchemin = cherche_itineraires(G, u, end, chaine)
9               if len(nchemin) != 0:
10					tab_itineraires.append(nchemin)
11      return []
12
13 def itineraires_court(G,dep,arr):
14	   cherche_itineraires(G, dep, arr)
15	   tab_court = ...
16	   mini = float('inf')
17     for v in tab_itineraires:
18     	   if len(v) <= ... :    
19		   mini = ...
20     for v in tab_itineraires:
21        if len(v) == mini:  
22              tab_court.append(...)
23     return tab_court
```

 La fonction` itineraires_court` prend en paramètre un graphe G, un sommet de  départ `dep` et un sommet d’arrivée `arr`. Cette fonction renvoie une liste Python  contenant tous les itinéraires pour aller de `dep` à `arr` en passant par le moins de  villes possible.

 Exemple (avec le graphe G2) :

```python
 itineraires_court(G2, 'A', 'F')
 >>> [['A', 'B', 'I', 'F'], ['A', 'H', 'G', 'F'], ['A', 'H', 'I', 
'F']]
```

On rappelle les points suivants : 

- la méthode `append` ajoute un élément à une liste Python ; par exemple,  `tab.append(el) `permet d’ajouter l’élément `el` à la liste Python `tab` ; 
- en python, l’expression ``  ['a'] + ['b'] `vaut ` ['a', 'b']` ; 
-  en python `float('inf')` correspond à l’infini.

6. Expliquer pourquoi la fonction `cherche_itineraires` peut être qualifiée de  fonction récursive. 
7. Expliquer le rôle de la fonction `cherche_itineraires` dans le programme p1. 
8. Compléter la fonction `itineraires_court`.

 Les ingénieurs sont confrontés à un problème lors du test du programme p1. Voici  les résultats obtenus en testant dans la console la fonction `itineraires_court`  deux fois de suite (sans exécuter le programme entre les deux appels à la fonction  `itineraires_court`) :

```python
 exécution du programme p1
 itineraires_court(G2, 'A', 'E')
 >>> [['A', 'C', 'E']]
 itineraires_court(G2, 'A', 'F')
 >>> [['A', 'C', 'E']]
```

 alors que dans le cas où le programme p1 est de nouveau exécuté entre les 2 appels  à la fonction `itineraires_court`, on obtient des résultats corrects :

```python
 exécution du programme p1
 itineraires_court(G2, 'A', 'E')
 >>> [['A', 'C', 'E']]
 exécution du programme p1
 itineraires_court(G2, 'A', 'F')
 >>> [['A', 'B', 'I', 'F'], ['A', 'H', 'G', 'F'], ['A', 'H', 'I', 
'F']]
```

9. Donner une explication au problème décrit ci-dessus. Vous pourrez vous  appuyer sur les tests donnés précédemment.

 La société CarteMap décide d’ajouter à son logiciel de cartographie des données sur  les différentes villes, notamment des données classiques : nom, département,  nombre d’habitants, superficie, …, mais également d’autres renseignements  pratiques, comme par exemple, des informations sur les infrastructures sportives  proposées par les différentes municipalités.

Dans un premier temps, la société a pour projet de stocker toutes ces données dans  un fichier texte. Mais, après réflexion, les développeurs optent pour l’utilisation d’une  base de données relationnelle. 

10. Expliquer en quoi le choix d’utiliser un système de gestion de base de  données (SGBD) est plus pertinent que l’utilisation d’un simple fichier texte.

On donne les deux tables suivantes:

Table ville

| id   | nom      | num_dep | nombre_hab | superficie |
| ---- | -------- | ------- | ---------- | ---------- |
| 1    | Annecy   | 74      | 125694     | 67         |
| 2    | Tours    | 37      | 136252     | 34.4       |
| 3    | Lyon     | 69      | 513275     | 47.9       |
| 4    | Chamonix | 74      | 8906       | 246        |
| 5    | Rennes   | 35      | 215366     | 50.4       |
| 6    | Nice     | 06      | 342522     | 72         |
| 7    | Bordeaux | 33      | 249712     | 49.4       |

Table sport

| id   | nom                     | type               | note | id_ville |
| ---- | ----------------------- | ------------------ | ---- | -------- |
| 1    | Richard Bozon           | piscine            | 9    | 4        |
| 2    | Bignon                  | terrain multisport | 7    | 5        |
| 3    | Ballons perdus          | terrain multisport | 6    | 1        |
| 4    | Mortier                 | piscine            | 8    | 2        |
| 5    | Block'Out               | mur d'escalade     | 8    | 2        |
| 6    | Trabets                 | mur d'escalade     | 7    | 4        |
| 7    | Centre aquatique du lac | piscine            | 9    | 2        |

Dans la table `ville`, on peut trouver les informations suivantes : 

- l’identifiant de la ville (`id`) : chaque ville possède un id unique ; 
-  le nom de la ville (`nom`) ; 
-  le numéro du département où se situe la ville (`num_dep`) ; 
-  le nombre d’habitants `(nombre_hab`) ; 
-  la superficie de la ville en km² (`superficie`).

Dans la table sport, on peut trouver les informations suivantes : 

- l’identifiant de l’infrastructure (`id`) : chaque infrastructure a un id unique ; 
-  le nom de l’infrastructure (`nom`) ; 
- le type d’infrastructure (`type`) ; 
- la note sur 10 attribuée à l’infrastructure (`note`) ; 
-  l’identifiant de la ville où se situe l’infrastructure (`id_ville`).

 En lisant ces deux tables, on peut, par exemple, constater qu’il existe une piscine  Richard Bozon à Chamonix.

11. Donner le schéma relationnel de la table `ville`. 

12. Expliquer le rôle de l’attribut `id_ville` dans la table `sport`. 

13. Donner le résultat de la requête SQL suivante :

    ```sql
     SELECT nom
     FROM ville
     WHERE num_dep = 74 AND superficie > 70
    ```

14. Écrire une requête SQL permettant de lister les noms de l’ensemble des  piscines présentes dans la table` sport`.

 Suite à de bons retours d’utilisateurs, la note du terrain multisport “Ballon perdus” est  augmentée d’un point (elle passe de 6 à 7).

15. Écrire une requête SQL permettant de modifier la note du terrain multisport  “Ballon perdus” de 6 à 7. 
16. Écrire une requête SQL permettant d’ajouter la ville de Toulouse dans la table  `ville`. Cette ville est située dans le département de la Haute-Garonne (31).  Elle a une superficie de 118 km². En 2023, Toulouse comptait 471941  habitants. Cette ville aura l’identifiant 8. 
17. Écrire une requête SQL permettant de lister les noms des murs d’escalade  disponibles à Annecy.



## Exercice 3: 

*Cet exercice porte sur la notion de listes, la récursivité et la programmation  dynamique.*

 Pour extraire de l’eau dans des zones de terrain instable, on souhaite forer un  conduit dans le sol pour réaliser un puits tout en préservant l’intégrité du terrain. Pour  représenter cette situation, on va considérer qu’en forant à partir d’une position en  surface, on s’enfonce dans le sol en allant à gauche ou à droite à chaque niveau,  jusqu’à atteindre le niveau de la nappe phréatique.

Le sol pourra donc être représenté par une pyramide d’entiers où chaque entier est  le score de confiance qu’on a dans le forage de la zone correspondante. Une telle  pyramide est présentée sur la figure 1, à gauche, les flèches indiquant les différents  déplacements possibles d’une zone à une autre au cours du forage. 

 Un conduit doit partir du sommet de la pyramide et descendre jusqu’au niveau le plus  bas, où se situe l’eau, en suivant des déplacements élémentaires, c’est-à-dire en  choisissant à chaque niveau de descendre sur la gauche ou sur la droite. Le score  de confiance d’un conduit est la somme des nombres rencontrés le long de ce  conduit. Le conduit gris représenté à droite sur la figure 1 a pour score de confiance  4+2+5+1+3=15.

![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex3_revisions_2024.jpg)

On va utiliser un ordinateur pour chercher à résoudre ce problème. Pour cela, on  représente chaque niveau par la liste des nombres de ce niveau et une pyramide par  une liste de niveaux.

 La pyramide ci-dessus est donc représentée par la liste de listes

 `ex1 = [[4],[6,2],[3,5,7],[5,1,6,2],[4,7,3,5,2]]`

1. Dessiner la pyramide représentée par la liste de liste

   ` ex2 = [[3],[1,2],[4,5,9],[3,6,2,1]]`

2. Déterminer un conduit de score de confiance maximal dans la pyramide ex2 et  donner son score. 

On souhaite déterminer le score de confiance maximal pouvant être atteint pour une  pyramide quelconque. Une première idée consiste à énumérer tous les conduits et à  calculer leur score pour déterminer les meilleurs. 

3. Énumérer les conduits dans la pyramide de trois niveaux représentée sur la  figure 2.

   ![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex3_2_revisions_2024.jpg)

 Afin de compter le nombre de conduits pour une pyramide de `n` niveaux, on  remarque qu’un conduit est uniquement représenté par une séquence de `n`  déplacements `gauche` ou `droite`.

4. En considérant un codage binaire d’un tel conduit, où `gauche` est représenté  par 0 et `droite` par 1, déterminer le nombre de conduits dans une pyramide  de `n` niveaux. 
5.  Justifier que la solution qui consiste à tester tous les conduits possibles pour  calculer le score de confiance maximal d’une pyramide n’est pas raisonnable.

 On dira dans la suite qu’un conduit est maximal si son score de confiance est  maximal. Afin de pouvoir calculer efficacement le score maximal, on peut analyser la  structure des conduits maximaux.

![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex3__3_revisions_2024.jpg)

- Première observation : si on a des conduits maximaux `cm1` et `cm2`  (représentés en gris dans la figure 3) pour les deux pyramides obtenues en  enlevant le sommet de `ex1`, on obtient un conduit maximal en ajoutant le  sommet 4 devant le conduit de plus grand score parmi `cm1` et `cm2`. Ici le score  de `cm1` est 6+5+6+5=22 et le score de `cm2` est 2+7+6+5=20 donc le conduit  maximal dans `ex1` est celui obtenu à partir de `cm1` et dessiné à droite dans la  figure 3.
- Deuxième observation : si la pyramide n’a qu’un seul niveau, il n’y a que le  sommet, dans ce cas, il n’y a pas de choix à faire, le seul conduit possible est  celui qui contient le sommet et le nombre de ce sommet est le score maximal  que l’on peut obtenir.

Avec ces deux observations, on peut calculer le score maximal possible pour un  conduit dans une pyramide p par récurrence. Posons `score_max(i,j)` le score  maximal possible depuis le nombre d’indice `j` du niveau `i`, c’est-à-dire dans la petite  pyramide issue de ce nombre. On a alors les relations suivantes :

-  `score_max(len(p)-1,j,p) = p[len(p)-1][j]` ; 
- `score_max(i,j,p) = p[i][j] +  max(score_max(i+1,j,p),score_max(i+1,j+1,p))`.

 Le score maximal possible pour `p` toute entière sera alors `score_max(0,0,p)`.

6. Écrire la fonction récursive `score_max` qui implémente les règles précédentes.

 Si on suit à la lettre la définition de `score_max`, on obtient une résolution dont le coût  est prohibitif à cause de la redondance des calculs. Par exemple ``score_max(3,1,p)``  va être calculé pour chaque appel à `score_max(2,0,p)` et `score_max(2,1,p)`. Pour  éviter cette redondance, on décide de mettre en place une approche par  programmation dynamique. Pour cela, on va construire une pyramide `s` dont le  nombre à l’indice `j` du niveau `i` correspond à `score_max(i,j,p)`, c’est-à-dire au  score maximal pour un conduit à partir du nombre correspondant dans `p`.

7. Écrire une fonction pyramide_nulle qui prend en paramètre un entier `n` et  construit une pyramide remplie de 0 à n niveaux. 

8. Compléter la fonction `prog_dyn` ci-dessous qui prend en paramètre une  pyramide `p`, et qui renvoie le score maximal pour un conduit dans `p`. Pour cela,  on construit une pyramide `s` remplie de 0 de la même taille et la remplit avec  les valeurs de `score_max` en commençant par le dernier niveau et en  appliquant petit à petit les relations données ci-dessus.

   ```python
   def prog_dyn(p):
   	n = len(p)
   	s = ...
   	# remplissage du dernier niveau
   	for j in ....:
   		s[n-1][j] = ....
   	# remplissage des autres niveaux
   	for i in ....:
   		s[i][j] = ...
   	# renvoie du score maximal
   	return s[0][0]
   ```

   

9. Montrer que le coût d’exécution de cette fonction est quadratique en `n` pour  une pyramide à `n` niveaux.
10. Expliquer comment adapter la fonction `score_max` pour éviter la redondance  des calculs afin d’obtenir également un coût quadratique, tout en gardant une  approche récursive.



## Exercice 4: 

*Cet exercice porte sur les systèmes d’exploitation, les commandes UNIX, les  structures de données (de type LIFO et FIFO) et les processus.*

 “Linux ou GNU/Linux est une famille de systèmes d’exploitation open source de type  Unix fondée sur le noyau Linux, créé en 1991 par Linus Torvalds. De nombreuses  distributions Linux ont depuis vu le jour et constituent un important vecteur de  popularisation du mouvement du logiciel libre.” 

Source : Wikipédia, extrait de l’article consacré à GNU/Linux. 

“Windows est au départ une interface graphique unifiée produite par Microsoft, qui  est devenue ensuite une gamme de systèmes d’exploitation à part entière,  principalement destinés aux ordinateurs compatibles PC. Windows est un système  d’exploitation propriétaire.” Source : Wikipédia, extrait de l’article consacré à Windows.

1. Expliquer succinctement les différences entre les logiciels libres et les logiciels  propriétaires. 
2. Expliquer le rôle d’un système d’exploitation.

 On donne ci-dessous une arborescence de fichiers sur un système GNU/Linux (les  noms encadrés représentent des répertoires, les noms non encadrés représentent  des fichiers, / correspond à la racine du système de fichiers) :

![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex4_revisions_2024.jpg)

3. Indiquer le chemin absolu du fichier `rapport.odt`. 

On suppose que le répertoire courant est le répertoire `elsa`. 

4. Indiquer le chemin relatif du fichier `photo_1.jpg`.

 L’utilisatrice Elsa ouvre une console (aussi parfois appelée terminal), le répertoire  courant étant toujours le répertoire `elsa`. On fournit ci-dessous un extrait du manuel  de la commande UNIX `cp` :

```Unix
 NOM
    cp - copie un fichier
 UTILISATION
    cp fichier_source fichier_destination
```

5. Déterminer le contenu du répertoire `documents` et du répertoire `boulot` après  avoir exécuté la commande suivante dans la console:

   ` cp documents/fiche.ods documents/boulot`

 “Un système d’exploitation est multitâche (en anglais : multitasking) s’il permet  d’exécuter, de façon apparemment simultanée, plusieurs programmes informatiques.  GNU/Linux, comme tous les systèmes d’exploitation modernes, gère le multitâche.” “Dans le cas de l’utilisation d’un monoprocesseur, la simultanéité apparente est le  résultat de l’alternance rapide d’exécution des processus présents en mémoire.” 

Source : Wikipédia, extraits de l’article consacré au Multitâche.

Dans la suite de l’exercice, on s’intéresse aux processus. On considère qu’un  monoprocesseur est utilisé. On rappelle qu’un processus est un programme en cours  d’exécution. Un processus est soit élu, soit bloqué, soit prêt.

6. Recopier et compléter le schéma ci-dessous avec les termes suivants : élu, bloqué, prêt, élection, blocage, déblocage.

   ![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex4_2_revisions_2024.jpg)

7. Donner l’exemple d’une situation qui contraint un processus à passer de l’état  élu à l’état bloqué. 

“Dans les systèmes d’exploitation, l’ordonnanceur est le composant du noyau du  système d’exploitation choisissant l’ordre d’exécution des processus sur le  processeur d’un ordinateur.” Source : Wikipédia, extrait de l’article consacré à l’ordonnancement.

 L’ordonnanceur peut utiliser plusieurs types d’algorithmes pour gérer les processus. L’algorithme d’ordonnancement par “ordre de soumission” est un algorithme de type  FIFO (First In First Out), il utilise donc une file.

8. Nommer une structure de données linéaire de type LIFO (Last In First Out).

 À chaque processus, on associe un instant d’arrivée (instant où le processus  demande l’accès au processeur pour la première fois) et une durée d’exécution  (durée d’accès au processeur nécessaire pour que le processus s’exécute  entièrement).

 Par exemple, l’exécution d’un processus P4 qui a un instant d’arrivée égal à 7 et une  durée d’exécution égale à 2 peut être représentée par le schéma suivant :

![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex4__3_revisions_2024.jpg)

 L’ordonnanceur place les processus qui ont besoin d’un accès au processeur dans  une file, en respectant leur ordre d’arrivée (le premier arrivé étant placé en tête de  file). Dès qu’un processus a terminé son exécution, l’ordonnanceur donne l’accès au  processus suivant dans la file.

 Le tableau suivant présente les instants d’arrivées et les durées d’exécution de cinq  processus :

| Processus | Instant d'arrivée | durée d'exécution. |
| --------- | ----------------- | ------------------ |
| P1        | 0                 | 3                  |
| P2        | 1                 | 6                  |
| P3        | 4                 | 4                  |
| P4        | 6                 | 2                  |
| P5        | 7                 | 1                  |

9. Recopier et compléter le schéma ci-dessous avec les processus P1 à P5 en  utilisant les informations présentes dans le tableau ci-dessus et l’algorithme  d’ordonnancement “par ordre de soumission”.

   ![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex4_4_revisions_2024.jpg)

    On utilise maintenant un autre algorithme d’ordonnancement : l’algorithme  d’ordonnancement “par tourniquet”. Dans cet algorithme, la durée d’exécution d’un  processus ne peut pas dépasser une durée Q appelée quantum et fixée à l’avance.  Si ce processus a besoin de plus de temps pour terminer son exécution, il doit  retourner dans la file et attendre son tour pour poursuivre son exécution.

    Par exemple, si un processus P1 a une durée d’exécution de 3 et que la valeur de Q  a été fixée à 2, P1 s’exécutera pendant deux unités de temps avant de retourner à la  fin de la file pour attendre son tour ; une fois à nouveau élu, il pourra terminer de  s’exécuter pendant sa troisième et dernière unité de temps d’exécution.

   10. Recopier et compléter le schéma ci-dessous, en utilisant l’algorithme  d’ordonnancement “par tourniquet” et les mêmes données que pour la  question 9, en supposant que le quantum Q est fixé 2.

       ![](D:\DISQUE ESSB\lycee\T NSI\sujets bac\ex4_5_revisions_2024.jpg)

​	On considère deux processus P1 et P2, et deux ressources R1 et R2.

11. Décrire une situation qui conduit les deux processus P1 et P2 en situation  d’interblocage.

## Exercice 5: 

*Cet exercice porte sur la programmation Python (dictionnaire), la programmation  orientée objet, les bases de données relationnelles et les requêtes SQL.*

 *Cet exercice est composé de 3 parties indépendantes.*

 On veut créer une application permettant de stocker et de traiter des informations sur  des livres de science-fiction. On désire stocker les informations suivantes : 

* l’identifiant du livre (id) ; 

*  le titre (titre) ; •

* le nom de l’auteur (nom_auteur) ; 

*  l’année de première publication (ann_pub) ; 

*  une note sur 10 (note). 

  

Voici un extrait des informations que l’on cherche à stocker :

Table Livres de science-fiction:

| id   | titre                 | auteur   | ann_pub | note |
| ---- | --------------------- | -------- | ------- | ---- |
| 1    | 1984                  | Orwell   | 19496   | 10   |
| 2    | Dune                  | Herbert  | 1965    | 8    |
| 3    | Fondation             | Asimov   | 1951    | 9    |
| 4    | Ubik                  | K.Dick   | 1953    | 9    |
| 5    | Blade Runner          | K.Dick   | 1968    | 8    |
| 6    | Les Robots            | Asimov   | 1950    | 10   |
| 7    | Ravage                | Barjavel | 1943    | 6    |
| 8    | Chroniques martiennes | Bradbury | 1950    | 7    |
| 9    | Dragon échu           | Hamilton | 2003    | 8    |
| 10   | Farenheit 451         | Bradbury | 1953    | 8    |

##### Partie A:

 Dans cette première partie, on utilise un dictionnaire Python. On considère le  programme suivant :

```python
 1 dico_livres = {
 	'id' : [1, 2, 14, 4, 5, 8, 7, 15, 9, 10],
 	'titre' : ['1984', 'Dune', 'Fondation', 'Ubik', 'Blade Runner',
 			'Les Robots', 'Ravage', 'Chroniques martiennes',
 			'Dragon déchu', 'Fahrenheit 451'],
 	'auteur' : ['Orwell', 'Herbert', 'Asimov',
 		'K.Dick', 'K.Dick', 'Asimov', 'Barjavel',
 		'Bradbury', 'Hamilton', 'Bradbury'],
 		'ann_pub' : [1949, 1965, 1951, 1953,1968, 
		1950, 1943, 1950, 2003, 1953],
 	'note' : [10, 8, 9, 9, 8, 10, 6, 7, 8, 8]
  }
 2 a = dico_livres['note']
 3 b = dico_livres['titre'][2]
```

1. Déterminer les valeurs des variables `a` et `b` après l’exécution de ce  programme.

 La fonction `titre_livre` prend en paramètre un dictionnaire (de même structure  que dico_livres) et un identifiant, et renvoie le titre du livre qui correspond à cet  identifiant. Dans le cas où l’identifiant passé en paramètre n’est pas présent dans le  dictionnaire, la fonction renvoie `None`.

```python
1 def titre_livre(dico, id_livre):
2     for i in range(len(dico['id'])):
3      	if dico['id'][i] == ... :   
4             return dico['titre'][...]
5     return ...
 
```

2. Recopier et compléter les lignes 3, 4 et 5 de la fonction `titre_livre`. 
3. Écrire une fonction `note_maxi` qui prend en paramètre un dictionnaire `dico`  (de même structure que `dico_livres`) et qui renvoie la note maximale. 
4. Écrire une fonction `livres_note` qui prend en paramètre un dictionnaire `dico`  (de même structure que `dico_livres`) et une note `n`, et qui renvoie la liste  des titres des livres ayant obtenu la note `n` (on rappelle que `t.append(a)`  permet de rajouter l’élément `a` à la fin de la liste `t`). 
5. Écrire une fonction `livre_note_maxi` qui prend en paramètre un dictionnaire  `dico` (de même structure que `dico_livres`) et qui renvoie la liste des titres  des livres ayant obtenu la meilleure note sous la forme d’une liste Python.

##### Partie B

 Dans cette partie, on utilise le paradigme orientée objet (POO). On propose deux  classes : `Livre` et `Bibliotheque`.

```python
1  class Livre:
2      def __init__(self, id_livre, titre, auteur, ann_pub, note):
3          self.id = id_livre
4          self.titre = titre
5          self.auteur = auteur
6          self.ann_pub = ann_pub
7          self.note = note
8      def get_id(self):
9          return self.id
10     def get_titre(self):
11         return self.titre
12     def get_auteur(self):
13         return self.auteur
14     def get_ann_pub(self):
15         return self.ann_pub
16        
17 class Bibliotheque:
18     def __init__(self):
19         self.liste_livre = []
20     def ajout_livre(self, livre):
21         self.liste_livre.append(livre)
22      def titre_livre(self, id_livre):
23         for livre in self.liste_livre :
24              if ... == id_livre :
25                  return ...
26         return ... 
```

6. Citer un attribut et une méthode de la classe `Livre`. 
7.  Écrire la méthode `get_note` de la classe `Livre`. Cette méthode devra  renvoyer la note d’un livre. 
8. Écrire le programme permettant d’ajouter le livre Blade Runner à la fin de la  “bibliothèque” en utilisant la classe `Livre` et la classe `Bibliotheque` (voir le  tableau en début d’exercice). 
9. Recopier et compléter la méthode `titre_livre` de la classe `Bibliotheque`.  Cette méthode prend en paramètre l’identifiant d’un livre et renvoie le titre du  livre si l’identifiant existe, ou `None` si l’identifiant n’existe pas.

##### Partie C 

On utilise maintenant une base de données relationnelle. Les commandes  nécessaires ont été exécutées afin de créer une table livres. Cette table livres  contient toutes les données sur les livres. On obtient donc la table suivante :

livres

| id   | titre                 | auteur   | ann_pub | note |
| ---- | --------------------- | -------- | ------- | ---- |
| 1    | 1984                  | Orwell   | 19496   | 10   |
| 2    | Dune                  | Herbert  | 1965    | 8    |
| 14   | Fondation             | Asimov   | 1951    | 9    |
| 4    | Ubik                  | K.Dick   | 1953    | 9    |
| 8    | Blade Runner          | K.Dick   | 1968    | 8    |
| 7    | Les Robots            | Asimov   | 1950    | 10   |
| 15   | Ravage                | Barjavel | 1943    | 6    |
| 17   | Chroniques martiennes | Bradbury | 1950    | 7    |
| 9    | Dragon échu           | Hamilton | 2003    | 8    |
| 10   | Farenheit 451         | Bradbury | 1953    | 8    |

 L’attribut `id` est la clé primaire pour la table `livres`.

10. Expliquer pourquoi l’attribut `auteur` ne peut pas être choisi comme clé  primaire. 

11. Donner le résultat renvoyé par la requête SQL suivante :

    ```sql
     SELECT titre
     FROM livres
     WHERE auteur = ‘K.Dick’
    ```

12. Écrire une requête SQL permettant d’obtenir les titres des livres écrits par  Asimov publiés après 1950. 
13. Écrire une requête SQL permettant de modifier la note du livre Ubik en la  passant de 9/10 à 10/10

 On souhaite proposer plus d’informations sur les auteurs des livres. Pour cela, on  crée une deuxième table auteurs avec les attributs suivants : 

* `id` de type INT ; 
* `nom` de type TEXT ; 
* `prenom` de type TEXT ; 
* `annee_naissance` de type INT (année de naissance).

table `auteurs`

| id   | nom      | prenom | annee_naissance |
| ---- | -------- | ------ | --------------- |
| 1    | Orwell   | George | 1903            |
| 2    | Herbert  | Franck | 1920            |
| 3    | Asimov   | Isaac  | 1920            |
| 4    | K.Dick   | Philip | 1928            |
| 5    | Bradbury | Ray    | 1920            |
| 6    | Barjavel | René   | 1911            |
| 7    | Hamilton | Peter  | 1960            |

La table `livres`est aussi modifiée comme suit:

| id   | titre                 | id_auteur | ann_pub | note |
| ---- | --------------------- | --------- | ------- | ---- |
| 1    | 1984                  | 1         | 19496   | 10   |
| 2    | Dune                  | 2         | 1965    | 8    |
| 14   | Fondation             | 3         | 1951    | 9    |
| 4    | Ubik                  | 4         | 1953    | 9    |
| 8    | Blade Runner          | 4         | 1968    | 8    |
| 7    | Les Robots            | 3         | 1950    | 10   |
| 15   | Ravage                | 6         | 1943    | 6    |
| 17   | Chroniques martiennes | 5         | 1950    | 7    |
| 9    | Dragon échu           | 7         | 2003    | 8    |
| 10   | Farenheit 451         | 5         | 1953    | 8    |

14. Expliquer l’intérêt d’utiliser deux tables (`livres` et `auteurs`) au lieu de  regrouper toutes les informations dans une seule table. 

15.  Expliquer le rôle de l’attribut `id_auteur` de la table `livres`. 

16. Écrire une requête SQL qui renvoie le nom et le prénom des auteurs des livres  publiés après 1960.

17. Décrire par une phrase en français le résultat de la requête SQL suivante :

    ```sql
     SELECT titre
     FROM livres
     JOIN auteurs ON id_auteur = auteurs.id
     WHERE ann_pub - annee_naissance < 30;
    ```

 Un élève décide de créer une application d’annuaire pour sa classe. On pourra  retrouver, grâce à cette application, différentes informations sur les élèves de la  classe : nom, prénom, date de naissance, numéro de téléphone, adresse email, etc.

18. Expliquer en quoi la réalisation de ce projet pourrait être problématique.