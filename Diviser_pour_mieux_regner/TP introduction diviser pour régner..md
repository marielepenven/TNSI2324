# Diviser pour régner

## I. La recherche dichotomique. 



1. Ouvrir le fichier dichotomie.py et établir un jeu de test afin de vérifier que la fonction `recherche_dichotomique`fonctionne correctement. 

2.  Quel est le principe de la recherche dichotomique? Expliquer en quelques mots.

3. Cette fonction est programmée en itératif. Ecrire une fonction qui fait la même chose en récursif. 

## II. Diviser pour régner. 



Cette expression puise ses origines dans une locution latine “*divide ut regnes*“. Elle serait attribuée en premier lieu à Philippe de Macédoine, père d’Alexandre le Grand, qui a régné au 4e siècle avant JC. Elle a alors à cette époque-là plutôt le sens d’une injection: “Divise afin que tu règnes!”.

Elle a ensuite été reprise par Louis XI et popularisée par Machiavel au 15e siècle sous la forme “*divide et imperia*“: “Divise et règne”.

Il s’agit d’une stratégie politique qui vise à asseoir sa propre autorité et à affaiblir l’ (les) adversaire(s) en créant des dissensions, des oppositions et des luttes. Il est en effet plus facile de lutter contre des opposants de moindre puissance se querellant entre eux que de gouverner en face d’un contre-pouvoir uni et puissant.

En informatique, **diviser pour régner **est une technique algorithmique consistant à :

1. Diviser : découper un problème initial en sous-problèmes ;
2. Régner : résoudre les sous-problèmes (récursivement ou directement s'ils sont assez petits) ;
3. Combiner : calculer une solution au problème initial à partir des solutions des sous-problèmes.

Question: Expliquer pourquoi la recherche dichotomique est un exemple d'algorithme utilisant la technique diviser pour régner. 

## III. Le tri fusion. 

Le tri fusion repose sur la stratégie diviser pour régner. 

Considérons un tableau `t `.

Le principe de cet algorithme est le suivant:

1. diviser le tableau `t` en deux tableaux `t1` et `t2`de même taille (à plus ou moins un élément). 
2. trier indépendamment les deux moitiés `t1`et `t2`récursivement. 
3. fusionner les deux tableaux triés ` t1`et `t2`. 

Prenons un exemple. 

Voici exécution du tri fusion sur la liste [23,12,4,56,35,32,42,57,3]

![](\Diviser_pour_mieux_regner\IMG\exemple_tri_fusion.jpg)

1. Quelles sont les différentes étapes que vous pouvez identifier? 
2. Effectuer le même travail sur la liste [15,13,17,3,12,8,9]. *Appeler votre enseignante*
3. Ecrire un algorithme pour le tri fusion. Vous décomposerez votre travail en utilisant une fonction `fusionner(t1,t2)`effectuant la fusion de deux tableaux triés.  *Appeler votre enseignante*
4. Implémenter cet algorithme en python et tester le. 

Nous avons donc maintenant un nouvel algorithme de tri. Afin de savoir si celui-ci est plus rapide que les tris que nous avons étudié, nous allons mesurer leurs temps d' exécution. 

**Définition : Le coût (en temps) d'un algorithme est l'ordre de grandeur  du nombre d'opérations élémentaires effectué par un algorithme. Cette estimation dépend du nombre de ses entrées et de leur dimension. Une opération élémentaire est une affectation, un calcul, une comparaison.**

5. Télécharger et enregistrer le fichier `tris.py`. 

   Dans le même répertoire, télécharger et enregistrer le fichier `vitesse tris eleve.py`

   Exécutez le programme. Expliquez l'affichage obtenu. 

6. Complétez le programme afin d'afficher les courbes relatives aux tris selection et au tri fusion.

   Quelle conclusion pouvez vous en tirer? 

7. Quel est le pire des cas d'un algorithme de tri? 

   Afficher les courbes relatives aux tris dans le pire des cas. 

8. Cout du tri fusion. 

   a. Soient deux listes de tailles m et p. Quelle est le coût de la fusion de deux listes? 

   b. Considérons une liste de taille $n = 2^k$ . 

   - pour k=1, combien de fusion de listes doit on effectuer? Quel est alors le cout de ces fusions? 
   - pour k= 2, combien de fusion de listes doit on effectuer? Quel est alors le cout de ces fusions?
   - pour k = 3, combien de fusion de listes doit on effectuer? Quel est alors le cout de ces fusions? 
   - pour k, combien de fusion de listes doit on effectuer? Quel est alors le cout de ces fusions? 

   

   Bilan: de manière générale, le tri fusion d'une liste dont la taille n vérifie $2^k\leq n<2^{k+1}$ a un cout de l'ordre de $k \times n$. 

   Nous dirons que le tri fusion a un cout en $\Theta (nlogn)$ ce qui est plus efficace que les tris que nous avons vu en classe de première. 

   

   

   

​		
