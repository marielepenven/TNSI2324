# Récursivité: les exercices. 



#### Exercice 1 : 

1. Écrire une fonction récursive `nb_diviseurs(j,n)` qui renvoie le nombre d'entiers entre 1 et j qui divise n.
2. Ecrire une fonction `est_parfait(n)` qui renvoie `True` si la somme des diviseurs de $n$ est égale à $2n$ : les entiers parfaits entre 1 et 30 sont 6 et 28 .  



#### Exercice 2 :

 Écrire une fonction qui calcule la moyenne d'un tableau t non vide :

1. de manière itérative,
2. de manière récursive. 	



#### Exercice 3 : 

Écrire une fonction récursive `nombre_de_chiffres (n)` qui prend en paramètre un entier positif ou non et renvoie son nombre de chiffres. 

Par exemple, `nombre_de_chiffres(34126)` doit renvoyer 5. 



#### Exercice 4 :

 Écrire une fonction récursive `nombre_de_bits(n)` qui prend en paramètre un entier positif ou nul et renvoie le nombre de bits valant 1 dans la représentation binaire de n. 

Par exemple, `nombre_de_bits(255)` doit renvoyer 8.



#### Exercice 5 :

 Écrire une fonction récursive `pgcd(a,b)` qui renvoie le pgcd de deux nombres entiers positifs. 

Par exemple, `pgcd(84,60)=12`



#### Exercice 6 : 

1. En partant du coin supérieur gauche, dessinez sur une feuille la figure suivante sans lever le stylo et sans repasser deux fois sur le même trait :

![](/LaReccursivite/img/trace.jpg)


2. Écrire une fonction récursive à deux paramètres (la longueur du plus grand carré, le nombre de carrés imbriqués) permettant de réaliser ce dessin avec le module turtle [](https://docs.python.org/fr/3/library/turtle.html)

   

#### Exercice 7: 

L'objectif de cet exercice est de  dessiner le flocon de Von Koch avec le module turtle.

1. Ecrire une fonction récursive qui permet de dessiner le fractal de Kosh ci-dessous. 

![](/LaReccursivite/img/fractaldevonkoch.jpg)



. La fonction de Koch prendra comme argument la longueur du segment et l'ordre : `koch(l,n)`

2. Ecrire une fonction (non récursive) utilisant la fonction de Kosh qui permet de dessiner le flocon de Kosh ci-dessous. Sont dessinés ci-dessous les flocons d'ordre 0, 1, 2 et 3. Cette fonction aura comme arguments la longueur du segment et l'ordre : `flocon(1,n)`

![](/LaReccursivite/img/flocondevonkoch.jpg)
