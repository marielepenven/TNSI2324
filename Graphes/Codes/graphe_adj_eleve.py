class Graphe():
    ''' un graphe représenté par une matrice d'adjacence, où les sommets sont les entiers 0,1,....,n-1'''
    
    def __init__(self,n):
        '''crée un graphe de taille n, en indiquant par défaut aucun des arcs'''
        pass
        
    def ajouter_arc(self,s1,s2):
        '''ajoute un arc allant de s1 à s2 dans la matrice d'adjacence'''
        pass
    
    def arc(self,s1,s2):
        '''renvoie True pour dire s'il existe un arc allant de s1 à s2 dans le graphe, False sinon'''
        pass
        
    def voisins(self,s):
        '''renvoie la liste des voisins du sommet s'''
        pass
