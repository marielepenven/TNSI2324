# TP: les arbres binaires de recherche. 

**Rappel**: Un **arbre binaire de recherche (ABR)** est un arbre binaire dont les nœuds contiennent des valeurs qui peuvent être comparées entre elles, comme des entiers ou des chaînes de caractères par exemple, et tel que, pour tout nœud de l'arbre, toutes les valeurs situées dans le sous-arbre gauche (respectivement droit) sont plus petites (respectivement plus grandes) que la valeur situé dans le nœud. 

1. Déterminer si les deux arbres suivants sont des arbres binaires de recherche. 

   Arbre 1

  ![](/Arbres/IMG/arbre_1_TP2.jpg)

​    Arbre 2: 

   ![](/Arbres/IMG/arbre2_TP_2.png)

2. Effectuer le parcours infixe de ces deux arbres. Que constatez vous? Comment pouvez vous expliquer ce résultat ? 

Un arbre binaire de recherche est un arbre, nous pouvons donc utiliser l'implémentation des arbres que nous avons vu précédemment. 

Puisque nous verrons comment insérer un élément dans un arbre binaire de recherche, l'implémentation par des tuples n'est pas pertinente, nous utiliserons donc l'implémentation objet. 

```python
class Abr:
    
    def __init__(self,valeur,gauche=None,droit=None):
        self.valeur = valeur
        self.sag = gauche
        self.sad = droit
    
    def __str__(self):
        ''' permet un affichage sous forme d'une chaine de caractères'''
        return "["+str(self.valeur)+',['+str(self.sag)+'],['+str(self.sad)+']]'
    
```



3. Voici la fonction  `appartient(arbre,x)`, écrite en pseudo code, prenant en paramètre un arbre binaire de recherche et une valeur `x` et renvoyant `True` si `x` est dans l'arbre, `False`sinon. 

   ```
    fonction appartient (arbre, x):
        si arbre est vide:
           retourner FAUX
       sinon:
           
           si arbre.valeur> x:
               retourner appartient(sous arbre gauche, x)
           si arbre.valeur < x:
               retourner appartient(sous arbre droit, x)
           si arbre.valeur = x:
               retourner VRAI
           
   ```

    a. Appelons arbre1 l'ABR suivant. 

   ![](/Arbres/IMG/arbre_3TP_2.jpg)

   - Quelle est la taille de arbre1? 
   - Combien de comparaisons effectuerait appartient(arbre1,9)? 
   - Combien de comparaisons effectuerait appartient(arbre1,16)? 
   - Quel semble être l'intérêt des ABR? 

   b. En notant n la taille d'un ABR, indiquer, en fonction de n,  le nombre de comparaison à effectuer dans le pire des cas pour la recherche d'un élément x dans un ABR. 

   c. Implémenter la fonction `appartient(arbre,x)`. 

   

4. Notre méthode pour implémenter les arbres binaires de recherche n'est pas satisfaisante. En effet, elle consiste à demander à l'utilisateur de vérifier lui-même que l'arbre qu'il rentre est bien un arbre binaire de recherche. 

   Implémenter une fonction `ajoute(arbre,x)`qui prend en paramètre un arbre binaire de recherche (qui peut être un arbre de taille 1) et un élément x et qui renvoie un arbre binaire de recherche contenant les éléments de l'arbre initial ainsi que `x`.
