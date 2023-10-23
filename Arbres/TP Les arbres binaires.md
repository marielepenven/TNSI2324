# TP: Les arbres binaires. 





## Partie 1: en débranché !

Considérons un arbre binaire. 

1. Ecrire un algorithme récursif permettant de déterminer la taille d'un arbre. 
2. Ecrire un algorithme récursif permettant de déterminer la hauteur d'un arbre. 
3. Ecrire un algorithme récursif permettant d'effectuer le parcours préfixe un arbre. 
4. Ecrire un algorithme récursif permettant d'effectuer le parcours infixe d'un arbre. 
5. Ecrire un algorithme récursif permettant d'effectuer le parcours suffixe d'un arbre. 



## Partie 2: avec une classe Noeud . 

Dans cette partie, nous implémenterons les arbres grâce à une classe Noeud. 

```python
class Noeud:
    
    def __init__(self,valeur,gauche=None,droit=None):
        self.valeur = valeur
        self.sag = gauche
        self.sad = droit
    
    def __str__(self):
        return "["+str(self.valeur)+',['+str(self.sag)+'],['+str(self.sad)+']]'
    

```

Nous considérerons qu'un arbre binaire est constitué de noeuds. 

1. a. Dessiner l'arbre obtenu avec les instructions suivantes:

   ```python
   >>> noeud2=Noeud("B")
   >>> noeud4=Noeud("D")
   >>> noeud5=Noeud("E")
   >>> noeud3=Noeud("C",noeud4,noeud5)
   >>> noeud1=Noeud("A",noeud2,noeud3)
   ```

   b. qu'affiche l'instruction `print(noeud1)`? 

   Vérifier le résultat obtenu à l'aide de la console.

2. Comment pouvez vous implémenter l'arbre suivant ?

   ![](/Arbres/IMG/arbre_1_TP.jpg)

3. En utilisant les algorithmes que vous avez écrits dans la partie précédente, implémenter des fonctions permettant de déterminer la taille, la hauteur ainsi de réaliser les parcours préfixe, infixe et suffixe des arbres. 

   N'oubliez pas de tester votre code  !



### Partie 3: avec des Tuples. 

Il est également possible d'implémenter un arbre à l'aide de tuples (ou de tableaux, ou de dictionnaires). 

```python
arbre= (racine,sag,sad)
```

1. Dessiner l'arbre représenté par l'implémentation suivante:

   ```python
   arbre = ("A",("B",("C",None,None),None),("E",None,("F",("G",None,None),None)))
   ```

2. Comment pouvez implémenter l'arbre suivant:

   ![](/Arbres/IMG/arbre_2TP.jpg)

3. En utilisant les algorithmes que vous avez écrits dans la partie 1, implémenter des fonctions permettant de déterminer la taille, la hauteur ainsi de réaliser les parcours préfixe, infixe et suffixe des arbres. 

​		N'oubliez pas de tester votre code  !
