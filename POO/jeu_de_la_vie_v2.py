import os
import time
import copy
import random

class Cellule:
    def __init__(self,etat,place):
        '''
        constructeur de la cellule.
        l'attribut etat indique si la cellule est morte (0) ou vivante(1)
        l'attribut place indique la place de la cellule dans le tableau en utilisant un tuple (i,j), i étant le numéro de la ligne et j le numéro de sa colonne
        '''
        self.etat=etat
        self.place=place
        
        
    def est_vivant(self):
        '''renvoie True si la cellule est vivante'''
        return self.etat == 1
    
    def donne_place(self):
        '''renvoie le tuple indiquant la position de la cellule dans la grille'''
        return self.place
      
    
        

class JeuDeLaVie:
    def __init__(self, tableau):
        """
        Affecte un tableau à deux dimensions à l'attribut tableau
        
        :param tableau: tableau à deux dimensions
        """
        self.board = tableau
        
    def affiche(self):
        """
        Affiche le tableau dans la console.
        
        On affiche "O" pour une cellule vivante.
        On affiche "." pour une cellule morte.
        """
        
        os.system('clear')
        for row in self.board:
            for case in row:
                if case.est_vivant():
                    print("O", end='')
                else:
                    print(".", end='')
            print()
            
    def etat_de_cellule(self,i,j):
        '''renvoie True si la cellule de ligne i et de colonne j est vivante, False sinon
            renvoie False si la cellule de ligne i et de colonne j n'est pas dans le tableau'''
        if i<0 or j<0:
            return False
        elif i>=len(self.board) or j>=len(self.board[i]):
            return False
        else:
            return self.board[i][j].est_vivant()
    
    def voisin_cellule(self,i,j):
        '''renvoie le nombre de cellules vivantes voisines de la cellule de place i,j'''
        compteur=0
        for k in range(0,3):
            if self.etat_de_cellule(i-1,j-1+k) == True:
                compteur +=1
        if self.etat_de_cellule(i,j-1) == True:
            compteur +=1
        if self.etat_de_cellule(i,j+1) == True:
            compteur +=1
        for k in range(0,3):
            if self.etat_de_cellule(i+1,j-1+k) == True:
                compteur +=1
        return compteur
    
    def nouvelle_cellule(self,i,j):
        '''renvoie une cellule dans l'état suivant suivant de la cellule placée à la ligne i et à la colonne j
            '''
        nb_voisin = self.voisin_cellule(i,j)
        if nb_voisin == 3 and (not self.board[i][j].est_vivant()):
            return Cellule(1,(i,j))
        elif (nb_voisin == 2 or nb_voisin ==3) and self.board[i][j].est_vivant():
            return Cellule(1,(i,j))
        else:
            return Cellule(0,(i,j))
        
       
         
    def tour(self):
        """
        Met à jour toute les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        # On crée un nouveau tableau de la même taille (peu importe ce qu'il y a dedans
        board_suivant = copy.deepcopy(self.board)
        for i in range(len(self.board)): # On parcourt les lignes
            for j in range(len(self.board[0])): # On parcourt les colonnes
                board_suivant[i][j] = self.nouvelle_cellule(i,j)
        # On remplace le board par le suivant
        self.board = copy.deepcopy(board_suivant)
                
        
    
        
    def run(self, nombre_tours, delai):
        """
        Méthode principale du jeu.

        Fait tourner le jeu de la vie pendant nombre_tours.
        Elle rafraichit l'affichage à chaque tour
        et attend delai entre chaque tour.
        
        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d'attente en secondes entre chaque tour
        """
        # On affiche le board avant le premier tour
        self.affiche()
        time.sleep(1)
        for i in range(nombre_tours):
            self.tour()
            self.affiche()
            time.sleep(delai)
            
def construire_un_tableau_cellulesmortes(nb_lignes,nb_colonnes):
    '''construit et renvoie un tableau uniquement constitué de cellules mortes'''
    tab = []
    for i in range(nb_lignes):
        col = []
        for j in range(nb_colonnes):
            col.append(Cellule(0,(i,j)))
        tab.append(col)
    return tab

def places_cellules_vivantes(nb_lignes,nb_colonnes,liste_v):
    '''
    construit et renvoie un tableau dont les cellules vivantes sont données dans la liste_v'''
    tab = construire_un_tableau_cellulesmortes(nb_lignes,nb_colonnes)
    for l in range(len(liste_v)):
        tab [liste_v[l][0]][liste_v[l][1]]=Cellule(1,(liste_v[l][0],liste_v[l][1]))
    return tab

def places_alea_cellules_vivantes(nb_lignes,nb_colonnes,nb_v):
    '''
    construit et renvoie un tableau dont les cellules vivantes sont données dans la liste_v'''
    tab = construire_un_tableau_cellulesmortes(nb_lignes,nb_colonnes)
    liste_v=[]
    while len(liste_v)<nb_v:
        i=random.randint(0,nb_lignes-1)
        j=random.randint(0,nb_colonnes-1)
        if (i,j) not in liste_v:
            liste_v.append((i,j))
    return places_cellules_vivantes(nb_lignes,nb_colonnes,liste_v)

#liste_vivantes=[(15,15),(15,17),(16,15),(16,17),(17,15),(17,16),(17,17)]
#tableau = places_cellules_vivantes(30,30,liste_vivantes)

liste_vivantes=[(0,2),(1,0),(1,2),(2,1),(2,2)]

tableau = places_cellules_vivantes(10,10,liste_vivantes)
# tableau =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# 
# tableau =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


mon_jeu = JeuDeLaVie(tableau)
mon_jeu.run(100, 1)
#mon_jeu.affiche()

# On demande à Python de parser les tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
