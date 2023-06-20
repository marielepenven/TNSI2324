class CompteBancaire():
    def __init__(self, lenom, lenumero, lesolde =0):
        '''creation d'un compte bancaire
        lenom= chaine de caractéres
        lenumero = int
        lesolde = int
        '''
        self.nom = lenom
        self.numero = lenumero
        self.solde  = lesolde
        
    def get_nom(self):
        '''permet d'accéder à l'attribut nom de l'objet compte bancaire'''
        return self.nom
    
    def get_numero(self):
         '''permet d'accéder à l'attribut numero de l'objet compte bancaire'''
         return self.numero
    
    def get_solde(self):
         '''permet d'accéder à l'attribut solde de l'objet compte bancaire'''
         return self.solde
    
    def depot(self,somme):
         '''permet de modifier le solde du compte bancaire en ajoutant de l'argent sur le compte'''
         self.solde += somme
        
    def retrait(self, somme):
         '''permet de modifier le solde du compte bancaire en retirant de l'argent sur le compte'''
         self.solde -= somme
    
    def affiche(self):
        ''' permet d'afficher les informations concernant le compte'''
        
        print("Le compte détenu par M. ou Mme. "+self.nom+" a un solde de "+str(self.solde)+"€")
        
        
        