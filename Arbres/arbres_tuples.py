    
def taille(arbre):
    ''' determine la taille d'un arbre'''
    if arbre is None:
        return 0
    else:
        return 1+taille(arbre[1])+taille(arbre[2])
    
   
def hauteur(arbre):
    ''' determine la hauteur d'un arbre'''
    if arbre is None:
        return -1
    else:
        return 1+ max(hauteur(arbre[1]),hauteur(arbre[2]))
    
def parcours_préfixe(arbre):
    ''' affiche le parcours préfixe d'un arbre'''
    if arbre is None:
        return
    else:
        print(arbre[0], end='-')
        parcours_préfixe(arbre[1])
        parcours_préfixe(arbre[2])
        
def parcours_infixe(arbre):
    '''affiche le parcours infixe d'un arbre'''
    if arbre is None:
        return
    else:
        parcours_infixe(arbre[1])
        print(arbre[0], end='-')
        parcours_infixe(arbre[2])
        
def parcours_suffixe(arbre):
    ''' affiche le parcrous suffixe d'un arbre'''
    if arbre is None:
        return
    else:
        parcours_suffixe(arbre[1])
        parcours_suffixe(arbre[2])
        print(arbre[0],end='-')
    
        

