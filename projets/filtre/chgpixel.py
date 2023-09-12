from PIL import Image

def modif_colonne(x,couleur):
    image = Image.open("photo1.jpg")
    taille = image.size
    largeur,hauteur = taille
    for i in range(largeur):
        image.putpixel((x,i),couleur)
    image.show()