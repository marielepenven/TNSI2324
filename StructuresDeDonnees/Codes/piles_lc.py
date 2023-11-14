class Cell:
    '''Cellule d'une liste chainee'''
    def __init__(self,valeur,suivant=None):
        self.valeur=valeur
        self.suivant=suivant

    def __str__(self):
        return str(self.valeur)

class Lc:
    '''Liste chaînée'''
    def __init__(self, tete=None):
        '''tete : lien vers la premiere cellule'''
        self.tete=tete
        
        
    #Ex 3
    def __str__(self):
        '''renvoie une forme lisible de Lc'''
        if self.tete is None:
            return '[]'
        else:
            cellule=self.tete
            valeurs=[cellule.valeur]
            while cellule.suivant is not None:
                cellule=cellule.suivant
                valeurs.append(cellule.valeur)
            return str(valeurs)
    
    #Ex 4
    def vide(self):
        '''renvoie True si la liste est vide
        False sinon'''
        # A compléter
        if self.tete is None :
            return True
        else:
            return False
    
    #Ex 5
    def __len__(self):
        '''renvoie la longueur de la liste'''
        if self.vide():
            return 0
        compteur = 1
        cell_en_cours = self.tete
        while cell_en_cours.suivant != None:
            cell_en_cours = cell_en_cours.suivant
            compteur += 1
        return compteur
        
        
    
    #Ex 6
    def __getitem__(self, index):
        '''renvoie l'élement  d'index donné,
           numéroté à partir de 0'''
        if self.vide() :
            return None
        i = 0
        en_cours = self.tete
        while i < index and en_cours is not None: 
            i += 1
            en_cours = en_cours.suivant
        if en_cours is None:
            raise IndexError("Indice invalide")
        return en_cours.valeur

    
    #Ex 7
    def inserer(self,x,index):
        '''insere l'élément x dans la liste
        à l'index donné, numéroté à partir de 0'''
        i = 0
        if self.tete is None and index !=0:
            raise IndexError("Indice incorrect")
        elif self.tete is None and index == 0:
            self.tete = Cell(x)
            return(self)
        elif index == 0:
            cellule_en_cours = self.tete
            self.tete = Cell(x,cellule_en_cours)
            return (self)
        en_cours = self.tete
        while i != index-1 and en_cours is not None: 
            en_cours = en_cours.suivant
            i += 1
        if en_cours is None:
            raise IndexError("Indice incorrect")
        nouvelle_cell = Cell(x,en_cours.suivant)
        en_cours.suivant = nouvelle_cell       
        return self
        
            
    #Ex 8
    def supprimer(self,index):
        ''' Supprime l'élément d'index donné
        numéroté  partir de 0, de la liste'''
        if index == 0: # reste a traiter le cas où self.tete.suivant n'existe pas
            self.tete = self.tete.suivant
        else:
            i = 0
            en_cours = self.tete
            while i < index-2 and en_cours is not None: 
                en_cours = en_cours.suivant
                i += 1
            if en_cours.suivant.suivant and en_cours.suivant:
                en_cours.suivant = en_cours.suivant.suivant
            else :
                en_cours.suivant = None
        return self
    
class Pile_lc:
    '''implémentation d'une pile à l'aide d'un tableau python'''
    def __init__(self):
        '''constructeur de la pile'''
        self.ma_pile = Lc()
        
    def empiler(self,x):
        '''empile l'élèment x dans la pile'''
        self.ma_pile.inserer(x,0)
    
    def depiler(self):
        '''depile un element de la pile'''
        self.ma_pile.supprimer(0)
        
        
    def element_depile(self):
        '''renvoie l'élèment dépilé de la pile'''
        j = self.ma_pile.__getitem__(0) #self.ma_pile[0]
        self.ma_pile.supprimer(0)
        return j
        
    
    def pile_vide(self):
        '''renvoie True si la pile est vide, False sinon
        >>> mapile = Pile_list()
        >>> mapile.pile_vide()
        True
        >>> mapile.empiler(3)
        >>> mapile.pile_vide()
        False
        '''
        return self.ma_pile.vide()

        
    def __len__(self):
        '''affiche le nombre d'élèments contenus dans la pile'''
        return len(self.ma_pile) # self.ma_pile.__len__()
    
    def __str__(self):
        '''renvoie le contenu de la pile sous forme d'une chaine de caractéres'''
        return self.ma_pile.__str__()
    
    def depiler_entierement(self):
        while not self.pile_vide():
            self.depiler()
    
    def inverse_pile(self):
        nv_lc = Lc()
        while not self.pile_vide():
            nv_lc.inserer(self.element_depile(),0)
        self.ma_pile = nv_lc
            
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

