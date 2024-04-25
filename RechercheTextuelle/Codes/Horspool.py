import doctest

def decalage(motif):
    ''' renvoie le dictionnaire des décalages du motif
    >>> decalage("TAG")
    {'A': 1, 'T': 2}
    '''
    pass 

def horspool(chaine,motif):
    '''renvoie la première position du motif dans la chaine, -1 s'il n'y est pas
    >>> horspool("TGCATAGCAT", "TAG")
    4
    >>> horspool("TGCATAGCAT", "TAT")
    -1 
    '''
    pass

    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
            
