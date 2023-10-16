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