class Noeud:
    
    def __init__(self,valeur,gauche=None,droit=None):
        self.valeur = valeur
        self.sag = gauche
        self.sad = droit
    
    def __str__(self):
        ''' permet un affichage sous forme d'une chaine de caractères'''
        return "["+str(self.valeur)+',['+str(self.sag)+'],['+str(self.sad)+']]'
    


        
def taille(arbre):
    ''' determine la taille d'un arbre'''
    if arbre is None:
        return 0
    else:
        return 1+taille(arbre.sag)+taille(arbre.sad)
    
   
def hauteur(arbre):
    ''' determine la hauteur d'un arbre'''
    if arbre is None:
        return -1
    else:
        return 1+ max(hauteur(arbre.sag),hauteur(arbre.sad))
    
def parcours_préfixe(arbre):
    ''' affiche le parcours préfixe d'un arbre'''
    if arbre is None:
        return
    else:
        print(arbre.valeur, end='-')
        parcours_préfixe(arbre.sag)
        parcours_préfixe(arbre.sad)
        
def parcours_infixe(arbre):
    '''affiche le parcours infixe d'un arbre'''
    if arbre.valeur is None:
        return
    else:
        parcours_infixe(arbre.sag)
        print(arbre.valeur, end='-')
        parcours_infixe(arbre.sad)
        
def parcours_suffixe(arbre):
    ''' affiche le parcrous suffixe d'un arbre'''
    if arbre.valeur is None:
        return
    else:
        parcours_suffixe(arbre.sag)
        parcours_suffixe(arbre.sad)
        print(arbre.valeur,end='-')
    
        
