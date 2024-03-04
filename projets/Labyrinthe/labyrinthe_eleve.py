# Auteurs :
# Logan Monier
# Thomas Beline
# Marie Guichard

import copy
import time
import pygame
from pygame.locals import *

def creer_liste(document):
    pass



class Labyrinthe:
    """
    Recherche d'un chemin dans un labyrinthe.
    """
    def __init__(self, labyrinthe):
        ''' création d"un labyrinthe à l'aide d'une liste de chaines de caractères'''
        self.hauteur =      #attribut donnant la hauteur du labyrinthe.
        self.largeur =      # attribut donnant la largeur du labyrinthe
        # On crée un dictionnaire vide
        self.listeAdjacence = {}
        # On génère la liste d'adjacence à partir du labyrinthe
        self.creeListeAdjacence(labyrinthe)
        self.entree = None
        self.get_entree(labyrinthe)
        self.sortie=None
        self.get_sortie(labyrinthe)

        self.trace(labyrinthe)
    
    def get_entree(self,labyrinthe):
       ''' permet d'affecter les coordonnées de l'entrée du labyrinthe à l'attribut entree'''
       pass
    
    def get_sortie(self,labyrinthe):
        ''' permet d'affecter les coordonnées de la sortie du labyrinthe à l'attribut sortie'''
       pass
    

    def creeListeAdjacence(self, labyrinthe):
        """
        Fabrique la liste d'adjcence du graphe représentant le labyrinthe.
        """
        pass


    def trace(self, labyrinthe):
        """
        Méthode principale qui gère tous les affichages.
        """
        pygame.init()
        # Taille d'un carré de base
        self.tailleCarre = 50
        # On crée une fenêtre à la taille du labyrinthe
        self.fenetre = pygame.display.set_mode((self.tailleCarre*self.largeur, self.tailleCarre*self.hauteur))
        # On dessine le labyrinthe
        self.traceLabyrinthe(labyrinthe)

        # On recherche un chemin
        chemin = self.trouveChemin()

        # On trace le chemin
        self.traceChemin(chemin)

        # On attend l'appui sur le bouton fermer de la fenêtre
        continuer = 1
        while continuer:
            for event in pygame.event.get():
                # Si appui sur le bouton fermer
                if event.type == QUIT:
                    continuer = 0

        pygame.quit()

    def traceLabyrinthe(self,labyrinthe):
        """
        Trace le labyrinthe.

        Les cases noires représentent les murs.
        """
        carre = pygame.Surface((self.tailleCarre,self.tailleCarre), pygame.SRCALPHA)
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if labyrinthe[y][x] == "#":
                    color = (0, 0, 0, 255)
                elif labyrinthe[y][x] == ".":
                    color = (255, 255, 255, 255)
                elif labyrinthe[y][x]=="s":
                    color=(0,255,0,255)
                elif labyrinthe[y][x]=="e":
                    color=(255,0,0,255)
                carre.fill(color)
                self.fenetre.blit(carre, (x*self.tailleCarre, y*self.tailleCarre))
        #modifie la fenêtre
        pygame.display.flip()



    def traceChemin(self, chemin):
        """
        Trace le chemin dans le labyrinthe.

        chemin : liste de tuples contenant les coordonnées (x, y) des cases constituant le chemin
        """
        color = (255, 0, 0, 255)
        for i in range(len(chemin)-1):
            pygame.draw.line(self.fenetre, color, (chemin[i][0]*self.tailleCarre+int(self.tailleCarre/2), chemin[i][1]*self.tailleCarre+int(self.tailleCarre/2)), (chemin[i+1][0]*self.tailleCarre+int(self.tailleCarre/2), chemin[i+1][1]*self.tailleCarre+int(self.tailleCarre/2)), 5)

        pygame.display.flip()

    def effaceChemin(self, chemin):
        """
        Efface le chemin en appliquant des carrés blancs

        chemin : liste de tuples contenant les coordonnées (x, y) des cases constituant le chemin
        """
        carre = pygame.Surface((self.tailleCarre,self.tailleCarre), pygame.SRCALPHA)
        color = (255, 255, 255, 255)
        carre.fill(color)
        for coord in chemin:
            self.fenetre.blit(carre, (coord[0]*self.tailleCarre, coord[1]*self.tailleCarre))
        pygame.display.flip()

    def apercuChemin(self, chemin):
        """
        Trace le chemin actuel et l'efface aussitôt

        chemin : liste de tuples contenant les coordonnées (x, y) des cases constituant le chemin
        """
        self.traceChemin(chemin)
        time.sleep(0.02)
        self.effaceChemin(chemin)

    def trouveChemin(self):
        """
        Retourne un chemin l'entrée et la sortie du labyrinthe
        """
        chemin = self.trouveRecursif(self.entree, self.sortie, [])
        return chemin

    def trouveRecursif(self, start, end, chaine):
        """
        Partie récursive de l'algorithme de recherche de chemin
        """
       pass

