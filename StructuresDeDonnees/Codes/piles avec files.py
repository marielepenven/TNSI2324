class Pile_list:
    '''implémentation d'une pile à l'aide d'un tableau python'''
    def __init__(self):
        '''constructeur de la pile'''
        self.ma_pile =[]
    
    def pile_vide(self):
        '''renvoie True si la pile est vide, False sinon'''
        return self.ma_pile == []
    
    def empiler(self,x):
        '''empile l'élèment x dans la pile'''
        self.ma_pile.append(x)
        return self
    
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
        for i in range(len(self)):
            print(self.depiler())
        return self
    
    def inverse_pile(self):
        retourne = []
        for i in range(len(self)):
            dessus = self.element_depile()
            retourne.append(dessus)
        self.ma_pile = retourne
        return self
    
    

class Files_2piles:
    
    def __init__(self):
        self.entree = Pile_list() # pile dans laquelle on ajoute les nouveaux élèments
        self.sortie = Pile_list() # pile dans laquelle on prend les élèments retirés
        
    def __str__(self):
        return str(self.entree)+str(self.sortie)
    
    
    def file_vide(self):
        return self.entree.pile_vide() and self.sortie.pile_vide()
           
        
    def enfiler(self,x):
        self.entree.empiler(x)
        
    def defiler(self):
        if self.sortie.pile_vide():
            while not self.entree.pile_vide():
                self.sortie.empiler(self.entree.element_depile())
        if self.sortie.pile_vide():
            raise IndexError("retirer sur une file vide")
        self.sortie.depiler()
    
    def element_defiler(self):
         if self.sortie.pile_vide():
            while not self.entree.pile_vide():
                self.sortie.empiler(self.entree.element_depile())
         if self.sortie.pile_vide():
            raise IndexError("retirer sur une file vide")
         rep = self.sortie.element_depile()
         return rep
        
    def __len__(self):
         return len(self.entree)+len(self.sortie)
        
        
        
        