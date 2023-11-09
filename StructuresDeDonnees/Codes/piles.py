class Pile_list:
    '''implémentation d'une pile à l'aide d'un tableau python'''
    def __init__(self):
        '''constructeur de la pile'''
        self.ma_pile =[]
        
    def empiler(self,x):
        '''empile l'élèment x dans la pile'''
        self.ma_pile.append(x)
    
    def depiler(self):
        '''depile un element de la pile'''
        self.ma_pile.pop()
        
    def element_depile(self):
        '''renvoie l'élèment dépiler de la pile'''
        return self.ma_pile.pop()
    
    def pile_vide(self):
        '''renvoie True si la pile est vide, False sinon
        >>> mapile = Pile_list()
        >>> mapile.pile_vide()
        True
        >>> mapile.empiler(3)
        >>> mapile.pile_vide()
        False
        '''
        return self.ma_pile == []
    
    def empiler(self,x):
        '''empile l'élèment x dans la pile'''
        self.ma_pile.append(x)
    
    def depiler(self):
        '''depile un element de la pile'''
        self.ma_pile.pop()
        
    def element_depile(self):
        '''renvoie l'élèment dépiler de la pile'''
        return self.ma_pile.pop()
        
    def __len__(self):
        '''affiche le nombre d'élèments contenus dans la pile'''
        return len(self.ma_pile)
    
    def __str__(self):
        '''renvoie le contenu de la pile sous forme d'une chaine de caractéres'''
        contenu=''
        for i in range(len(self)):
            contenu = contenu +" " + str(self.ma_pile[i])
        return contenu
    
    def depiler_entierement(self):
        pass
    
    def inverse_pile(self):
        pass
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
