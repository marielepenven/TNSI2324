from PIL import Image


img = Image.open("smiley.jpeg")
# Affiche l'image originale
img.show()

def echangePixels(image,pixel_a,pixel_b):
    """ echange la couleur des deux pixels pixel_a et pixel_b
    pixel_a: tuple de coordonnées,
    pixle_b: tuple de coordonnées
    """
    pass

    

def echangeQuadrant(image,coinHautGauche_a,coinHautGauche_b,n):
    """
Échange les pixels entre les deux quadrants de taille n
définis par leur coin haut gauche.

coinHautGauche_a : tuple des coordonnées du coin supérieur gauche du quadrant a
coinHautGauche_b : tuple des coordonnées du coin supérieur gauche du quadrant b
n : taille des deux quadrants

"""
    
    pass

def tourneRecursif(image,coinHautGauche,taille):
   """
    Applique une rotation du quadrant de l'image défini par
    son coin supérieur gauche et sa taille.

    coinHautGauche : tuple des coordonnées du coin supérieur gauche du quadrant
    taille : taille du quadrant à faire tourner

    """



def tourne(image):
    """
Lance la fonction récursive sur l'image originale.

"""
    tourneRecursif(image,(0,0),image.size[0])
    
# Lance le programme
tourne(img)
# Affiche l'image
img.show()


