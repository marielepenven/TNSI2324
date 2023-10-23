# Les Arbres

## I. Une nouvelle structure de données. 

### a. Définition. 

Un **arbre** est une structure de données hiérarchique.
Il est constitué de nœuds, reliés entre eux par des arêtes selon un relation père fils.  

![](/Arbres/IMG/pere-fils.jpg)

On distingue trois types de nœuds :

- la **racine** d'un arbre est l'unique nœud ne possédant pas de parent. On la place en haut de l'arbre. 
- les **feuilles** (ou nœuds externes), éléments ne possédant pas de fils dans l'arbre,
- les **nœuds internes** , éléments possédant au moins un fils. 

Le nom de chaque nœud est appelé son étiquette. 

### b. Propriétés. 

La **taille**  d'un arbre est son nombre total de nœuds. 
**L'arité** d'un nœud est son nombre total de fils. 
La **profondeur** d'un nœud est le nombre d'arêtes de son chemin le plus court vers la racine. 
La **hauteur** d'un arbre est la profondeur de son nœud le plus profond. 
Nous prendrons comme convention que :
Si un arbre est réduit à un seul nœud -racine, sa hauteur sera 0. 
Si un arbre est vide, sa hauteur est -1.

Exemple: 

![](/Arbres/IMG/arbre_binaire.jpg)

La racine de cet arbre est A. 
Cet arbre a 4 feuilles. 
La taille de cet arbre est 7. 
L'arité de D est 2. 
La profondeur de B est 1. 
La profondeur de G est 2. 
La hauteur de cet arbre est 2

## Les arbres binaires.

### a. Définition. 

Un **arbre binaire**  est un arbre dont chaque nœud possède au plus deux éléments fils. 

Exemples: 

Cet arbre n'est pas un arbre binaire. 

![](/Arbres/IMG/arbre_non_binaure.jpg)



Cet arbre est un arbre binaire. 

![](/Arbres/IMG/arbre_binaire.jpg)

### b. Sous arbres. 

Chaque nœud d'un arbre binaire ne pouvant pas avoir plus de fils, il est possible de séparer le « dessous » de chaque nœud en deux sous-arbres (éventuellement vides) : le sous-arbre gauche et le sous-arbre droit. 

![](/Arbres/IMG/sous_arbre.jpg)

Les deux sous-arbres représentés ici sont les sous-arbres du nœud racine T. 
Le nœud O admet comme sous-arbre gauche le nœud H et comme sous-arbre droit le nœud N. 
Les feuilles P, H et N ont pour sous-arbre gauche et pour sous-arbre droit l'arbre vide. 

### c. Les arbres binaires particuliers. 

#### 1. L'arbre dégénéré. 

Arbre dégénéré (filiforme ou peigne) : tous les nœuds internes n'ont qu'un seul fils, donc l'arbre n'a qu'une feuille.

![](/Arbres/IMG/peigne.jpg)

#### 2. L'arbre équilibré. 

Arbre équilibré : les hauteurs de ses sous arbres différent au plus d'une unité et sont eux-mêmes des arbres équilibrés.

![](/Arbres/IMG/arbre_équilibré.jpg)

#### 3. L'arbre parfait. 

Arbre parfait : arbre binaire dans lequel tous les nœuds possèdent zéro ou deux fils et toutes les feuilles sont à la même profondeur. 
Tous les niveaux sont donc remplis. 

![](/Arbres/IMG/arbre_parfait.jpg)

### d. Lien entre la taille et la hauteur. 

Si N désigne la taille d'un arbre binaire et h désigne sa hauteur, alors ces deux quantités sont contraintes par l'inégalité suivante :

$h \leq N \leq 2^h-1$


La borne gauche correspond au cas de l'arbre dégénéré. 
La borne droite correspond au cas de l'arbre parfait. 

## III. Parcours d'un arbre. 

Parcourir un arbre consiste à visiter chacun des nœuds de l'arbre afin d'effectuer un traitement sur chacune des étiquettes.
On distingue différents parcours selon l'ordre dans lequel les nœuds sont visités : des parcours en profondeur et en largeur. 

### a. Parcours en largeur. 

Un parcours en largeur visite les nœuds d'un arbre niveau par niveau : le nœud racine de profondeur nulle, les nœuds de profondeur 1, puis les nœuds de profondeur 2, etc..

Exemple: 

![](/Arbres/IMG/parcours.jpg)

Dans notre exemple, cela donne :
I-D-E-B-K-Z

### b. Parcours en profondeur. 

Un parcours en profondeur visite le sous arbre gauche avant le sous arbre droit pour chaque nœud. 
Il existe trois types de parcours en profondeur en fonction de l'ordre de visite des fils par rapport à leur père. 

#### 1. Parcours en profondeur préfixe. 

Père- Fils Gauche- Fils Droit. 
Si le fils fauche est également père, on visitera d'abord son propre fils gauche avant de passer à son fils droit. 

Exemple :

![](/Arbres/IMG/parcours.jpg)

Dans notre exemple, cela donne:

 I-D-B-E-K-Z

#### 2. Parcours en profondeur infixe. 

 Fils Gauche- Père- Fils Droit. 

Exemple :

![](/Arbres/IMG/parcours.jpg)

Dans notre exemple, cela donne B-D-I-K-E-Z

#### 3. Parcours en profondeur suffixe. 

 Fils Gauche- Fils Droit.- Pére. 

Exemple: 

![](/Arbres/IMG/parcours.jpg)

Dans notre exemple, cela donne B-D-K-Z-E-I

## IV. Les arbres binaires de recherche (ABR). 

Un **arbre binaire de recherche (ABR)** est un arbre binaire dont les nœuds contiennent des valeurs qui peuvent être comparées entre elles, comme des entiers ou des chaînes de caractères par exemple, et tel que, pour tout nœud de l'arbre, toutes les valeurs situées dans le sous-arbre gauche (respectivement droit) sont plus petites (respectivement plus grandes) que la valeur situé dans le nœud. 

Exemples:

Cet arbre est un arbre binaire de recherche. 

![](/Arbres/IMG/abr.jpg)

Cet arbre n'est pas un arbre binaire de recherche. 

![](/Arbres/IMG/non_abr.jpg)
