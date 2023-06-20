class Voiture():
    def __init__(self,marque='Ford',couleur='Rouge',pilote='personne',vitesse=0):
        self.marque = marque
        self.couleur = couleur
        self.pilote = pilote
        self.vitesse = vitesse
        
    def choix_conducteur(self,pilote):
        self.pilote = pilote
        
    def accelerer(self,taux,duree):
        if self.pilote != "personne":
            self.vitesse += self.vitesse + taux*duree
        else:
            print("cette voiture n'a pas de conducteur !")
            
    def affiche_tout(self):
        print(self.marque + " "+self.couleur +  " pilotée par "+self.pilote+", vitesse = "+str(self.vitesse)+" m/s.")