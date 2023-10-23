class Graphe():
    '''représentation des graphes à l'aide des listes de successeurs: utilisation d'un dictionnaire
        Les sommets sont les entiers 0,1,....,n-1'''
    
    def __init__(self,n):
        '''crée un graphe de taille n, en  n'indiquant par défaut, aucun arc'''
        self.n=n
        self.adj={}
        for i in range(n):
            self.adj[i]=[]
        
    def ajouter_arc(self,s1,s2):
        '''ajoute un arc allant de s1 à s2 dans la matrice d'adjacence'''
        self.adj[s1].append(s2)
    
    def arc(self,s1,s2):
        '''renvoie True pour dire s'il existe un arc allant de s1 à s2 dans le graphe, False sinon'''
        return s2 in self.adj[s1]
        
    def voisins(self,s):
        '''renvoie la liste des voisins du sommet s'''
        return self.adj[s]
