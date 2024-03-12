class Graphe():
    ''' un graphe représenté par une matrice d'adjacence, où les sommets sont les entiers 0,1,....,n-1'''
    
    def __init__(self,n):
        '''crée un graphe de taille n, en indiquant par défaut aucun des arcs'''

        self.n=n
        self.adj = [[0]*n for i in range(n)]
        
    def ajouter_arc(self,s1,s2):
        '''ajoute un arc allant de s1 à s2 dans la matrice d'adjacence'''
        self.adj[s1][s2]=1
    
    def arc(self,s1,s2):
        '''renvoie True pour dire s'il existe un arc allant de s1 à s2 dans le graphe, False sinon'''
        if self.adj[s1][s2] == 1:
            return True
        else:
            return False
        
    def voisins(self,s):
        '''renvoie la liste des voisins du sommet s'''
        v=[]
        for i in range(self.n):
            if self.adj[s][i]==1:
                v.append(i)
        return v