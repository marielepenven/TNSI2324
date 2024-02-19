# TP: La rotation d'une image. 

L'objectif de ce TP est de pivoter d'un quart de tour une image carré dans le sens inverse des aiguilles d'une montre. 

| ![](D:\DISQUE ESSB\lycee\T NSI\algorithme\FichiersJoints\Rotation\Tux128.png) | ![](D:\DISQUE ESSB\lycee\T NSI\algorithme\FichiersJoints\Rotation\Tux128_pivoté.png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: |

Nous utiliserons pour cela la bibliothèque PIL dont vous trouverez la documentation en ligne [ici](https://he-arc.github.io/livre-python/pillow/index.html)

Voici les différentes fonctions qui vous seront utiles:

| Syntaxe                           | Fonction                                                     |
| --------------------------------- | ------------------------------------------------------------ |
| `from PIL import Image`           | Permet d’importer la classe` Image` de PIL qui contient tout ce dont on aura besoin  pour ce TP |
| `img = Image.open(nomFichier)`    | Ouvre le fichier dont on spécifie le nom (sous forme d’une chaîne de caractère) et  renvoie un objet `Image` qui permet de manipuler l’image et ses pixels. PIL peut  ouvrir de nombreux formats d’image. |
| `img.show()`                      | Affiche l’image `img` en utilisant le programme d’affichage d’image par défaut du  système d’exploitation. |
| `img.save(nomimage,format`)       | Sauvegarde l'image dans le format spécifié                   |
| `largeur,hauteur = img.size`      | `size` est un attribut de la classe ` Image `contenant un tuple de deux entiers  représentant respectivement la largeur et la hauteur de l’image en nombre de pixels |
| `img2 = Image.new("RGB", (l, h))` | Crée une image vide de taille` l×h` pixels en couleur  ("RGB"). |
| `couleur = img.getpixel((x,y)) `  | Récupère la couleur du pixel aux coordonnées ` x,y `dans l’image ` img `. |
| `img.putpixel((x,y),couleur) `    | Fixe la couleur du pixel de coordonnées `x, y` de l’image` img` à la valeur `couleur`. |



## Version A: une version naïve. 

1. Ouvrir et exécuter le fichier `image.py`. 

   Que fait ce code? 

2. Ecrire une fonction `tourne(img)` qui renvoie une version tournée à 90° vers la gauche de l'image `img` . 

3. Tester la fonction `tourne`avec l'image`smiley.jpeg`, puis avec l'image `paysage1carre.jpg`. Que se passe-t-il avec la seconde image? 

## Version B: Diviser pour régner. 

Il est possible d'appliquer la méthode "diviser pour régner" à la rotation de 90° d'une image carrée. 

On procède alors par étapes:

1. Diviser: on coupe l'image en quatre quadrants. 
2. Régner: On effectue une rotation récursive de chacun des quadrants. 
3. Combiner: On applique une permutation circulaire des quadrants. 

![](D:\DISQUE ESSB\lycee\T NSI\algorithme\photo1.jpg)

Voyons ce que cela donne avec une image élèmentaire de $8 \times 8$ pixels:

![](D:\DISQUE ESSB\lycee\T NSI\algorithme\photo2.jpg) 

1. Compléter le script `rotation_e.py`afin qu'il effectue la rotation d'une image en utilisant la méthode diviser pour régner. 

2. Tester sur les images `smiley.jpeg`et `paysage1carre.jpg`.

   Comparer la vitesse d'exécution de votre programme avec celui vu dans la méthode naïve. Que pouvez vous dire ? 

   
