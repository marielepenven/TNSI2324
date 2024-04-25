import doctest

def recherche_naive_1(chaine,motif):
    ''' renvoie True si le motif se trouve dans la chaine, False sinon

    >>> recherche_naive_1("abcabcabc","cd")
    False
    
    >>> recherche_naive_1("abcdabdcbabec","ba")
    True
    
    '''
    pass

def recherche_naive_2(chaine,motif):
    ''' renvoie la liste des positions à partir desquelles on trouve le motif dans la chaine

    >>> recherche_naive_2("abcabcabc","cd")
    []
    
    >>> recherche_naive_2("abcdabdcbabec","ba")
    [8]
    
    >>> recherche_naive_2("abcabcabcab","bc")
    [1, 4, 7]
    '''
    pass

if __name__ == "__main__":
    doctest.testmod(verbose=True)
            
        
