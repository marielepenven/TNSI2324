# Diviser pour régner: Exercices

## Exercice 1 (bac): 

Une ligne polygonale est constituée d'une liste ordonnée de points, appelés sommets, joints par des segments. L'algorithme de Douglas Peuker permet de simplifier une ligne polygonale en supprimant certains de ses sommets. L'effet de l'algorithme appliqué aux lignes polygonales du contour de la France métropolitaine est illustré ci-dessous. 

![](/Diviser_pour_mieux_regner/IMG/ex1_diviser_pour_régner.jpg)

On implémentera cet algorithme dans la dernière question de l'exercice. Pour cela, nous allons d'abord implémenter des fonctions auxiliaires. 

On suppose dans la suite que les sommets sont des points du plan dont les coordonnées $(x,y)$ dans un repère orthonormé fixé sont représentées par des tuples de longueur 2. 

1. La distance qui sépare deux points A et B de coordonnées $(x_A,y_A)$ et $(x_B,y_B)$ est donnée par la formule $\sqrt{(x_B-x_A)²+(y_B-y_A)²}$ . 

   On rappelle que la fonction `sqrt`du module `math`de Python renvoie la racine carrée d'un nombre positif ou nul. 

   a. Ecrire une instruction qui permet d'importer la fonction `sqrt()`du module `math`. 

   b. Supposant l'import réalisé, écrire une fonction `distance_points(a,b)`qui prend en argument deux tuples `a`et `b`représentant les coordonnées de deux points et renvoie la distance qui les sépare. 

2. On dispose d'une fonction `distances_point_droite(p,a,b)`qui prend en argument les tuples représentant les coordonnées respectives des points P, A et B et qui renvoie la distance du point P à la droite (AB). L'exécution de cette fonction produit une erreur dans les cas où les points A et B sont confondus. 

   A l'aide de fonctions `distance_points`et `distance_point_droite`, écrire une fonction `distance(p,a,b)`qui renvoie la distance entre le point P et la droite (AB) si les points A et B sont distincts et la distance AP sinon. 

Dans la suite, on dira que la fonction `distance`calcule la distance entre le point P et les points A et B, éventuellement confondus. 

3. On a besoin d'une fonction `le_plus_loin(ligne)`qui prend en argument une liste de tuples représentant les coordonnées des points d'une ligne polygonale. 

   Cette fonction doit renvoyer un tuple composé de :

   - l'indice du point de coordonnées `p` de la ligne polygonale extrémités `deb`et `fin`, pour lequel la distance `distance(p,deb,fin)`est la plus grande;
   - la valeur correspondante de cette distance. 

   On fournit le code incomplet suivant:

   ```python
   def le_plus_loin(ligne):
   	n = len(ligne)
   	deb = ligne[0]
   	fin = ligne[n-1]
   	dmax = 0
   	indice_max = 0
   	for idx in range(1,n-1):
   		p = ....
   		d = distance(p,deb,fin)
   		if ...... :
   			......
   			......
   	return ......
   ```

   Recopier et compléter le code de cette fonction. 

4. Ecrire une fonction `extrait(tab,i,j)`qui renvoie la copie du tableau `tab`des cases d'indice i inclus à j inclus pour $\leq i\leq j<len(tab)$ . 

   L'appel `extrait([7,4,9,12],2,3)`renverra ainsi `[9,12]`. 

L'algorithme de Douglas- Peuker repose sur une stratégie de type "diviser pour régner". 

Pour éliminer des sommets "proches de l'alignement", un seuil est fixé. 

Etant donnée une ligne polygonale, le principe de l'algorithme est le suivant:

- si la ligne ne contient qu'un ou deux sommets, l'algorithme se termine;

- sinon, on considère la droite formée par les extrémités de la ligne (son premier et dernier sommet), et on sélectionne le point le plus éloigné de cette droite (dans le cas où les extrémités sont confondues, on sélectionne le point le plus éloigné de celles-ci):

  - si la distance entre le point sélectionné et la droite (ou les extrémités lorsqu'elles sont confondues) est inférieure au seuil fixé, on ne que conserve que les extrémités de la ligne polygonale;

    ![](/Diviser_pour_mieux_regner/IMG/ex1_fig2_diviser_pour_régner.jpg)

  		- sinon, on applique l'algorithme de manière récursive aux deux parties de la ligne polygonale formées de la séquence formée du premier sommet jusqu'au sommet sélectionné d'une part et de la séquence formée du sommet sélectionné jusqu'au dernier sommet d'autre part. L'algorithme renvoie alors la concaténation des séquences simplifiées ainsi obtenues. 

![](/Diviser_pour_mieux_regner/IMG/ex1_fig3_diviser_pour_régner.jpg)

​	L'algorithme appelé sur la ligne polygonale [A,B,C,D,E,F,G] ci_dessus va récursivement être appelé sur les 	lignes polygonales [A,B,C] et [C,D,E,F,G]. 

​	La ligne polygonale que l'on obtiendra à la fin de l'algorithme sera[A,C,E,G]. 

![](/Diviser_pour_mieux_regner/IMG/ex1_fig4_diviser_pour_régner.jpg)	

5. L'algorithme de Douglas-Peuker est implémenté par la fonction `simplifie` ci-dessous, qui prend en argument la ligne polygonale et le seuil choisi. 

   ```python
   def simplifie(ligne,seuil):
   	n = len(ligne)
   	if n<= 2: 
   		return .....
   	else:
   		indice_max,dmax = le_plus_loin(ligne)
   		if dmax <= seuil:
   			return ......
   		else: 
   			#bloc à écrire
   			
   ```

   

​	Recopier et compléter le code. 

## Exercice 2 (bac): 

Cet exercice traitre du calcul de la somme d'une arbre binaire. Cette somme consiste à additionner toutes les valeurs numériques contenues dans les nœuds de l'arbre. 

L'arbre utilisé dans les parties A et B est le suivant:

![](/Diviser_pour_mieux_regner/IMG/ex2_fig1_diviser_pour_régner.jpg)

#### Partie A: Parcours d'un arbre. 

1. Donner la somme de l'arbre précédent. Justifier la réponse en explicitant le calcul qui a permis de l'obtenir. 

2. Indiquer la lettre correspondante aux noms `racine`, `noeud`, `SAG`(sous arbre gauche) et `SAD`(sous arbre droit). Chaque lettre A,B, C , D et E devra être utilisée une seule fois. 

   ![](/Diviser_pour_mieux_regner/IMG/ex2_fig2_diviser_pour_régner.jpg)

3. Laquelle de ces quatre propositions effectue un parcours en largeur de l'arbre? 

   Proposition A: 7-6-4-3-9-2-1

   Proposition B: 3-6-7-4-2-9-1

   Proposition C: 3-6-2-7-4-9-1

   Proposition D: 7-4-6-9-1-2-3

4. Ecrire en langage Python la fonction `somme`qui prend en paramètre une liste de nombres et qui renvoie la somme de ses éléments. 

​		Exemple: `somme([1,2,3,4])`est égale à 10

5. La fonction `parcourir(arbre)`pourrait se traduire en langage naturel par:

   ```
   parcourir(A):
   	L = liste_vide
   	F = file_vide
   	enfiler A dans F
   	Tant que F n'est pas vide
   		défiler S de F
   		ajouter la valeur de la racine de S dans L
   		Pour chaque sous arbre SA non vide de S
   			enfiler SA dans F
   	renvoyer L
   ```

   Donner le type de parcours obtenu grâce à la fonction `parcourir`. 

#### Partie B: Méthode 'diviser pour régner'. 

6. Parmi les quatre propositions A,B, C et D ci-dessous, indiquer la seule proposition correcte:

   En informatique, le principe de diviser pour régner signifie:

   Proposition A: diviser une fonction en deux fonctions plus petites. 

   Proposition B: utiliser plusieurs modules

   Proposition C: séparer les informations en fonction de leurs types. 

   Proposition D: diviser un problème en deux problèmes plus petits et indépendants. 

   

7. L'arbre présenté dans le probléme peut être décomposé en racine et sous arbres:

   ![](/Diviser_pour_mieux_regner/IMG/ex2_fig3_diviser_pour_régner.jpg)

​	Indiquer dans l'esprit de 'diviser pour régner' l'égalité donnant la somme d'un arbre en fonction de la 	somme des sous arbres et de la valeur numérique de la racine. 

8. Ecrire en langage Python une fonction récursive `calcul_somme(arbre)`. Cette foncton calcule la somme de l'arbre passé en paramètre. 

   Les fonctions suivantes sont disponibles:

   - `est_vide(arbre)`: renvoie `True`si `arbre`est vide et renvoie `False`sinon;
   - `valeur_racine(arbre)`: renvoie la valeur numérique de la racine de `arbre`;
   - `arbre_gauche(arbre)`: renvoie le sous arbre gauche de `arbre`;
   - `arbre_droit(arbre)`: renvoie le sous arbre droit de `arbre`. 

   

    

