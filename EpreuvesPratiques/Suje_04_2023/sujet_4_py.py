def voisinage(n,ligne,colonne):
    """ Renvoie la liste des coordonnées des voisins de la case
    (ligne,colonne) en gérant les cases sur les bords """
    voisins=[]
    for l in range(max(0,ligne-1),min(n,ligne+2)):
        for c in range(max(0,colonne-1),min(n,colonne+2)):
            if (l,c) != (ligne,colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille,ligne,colonne):
    """Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins=...
    for l,c in voisins:
        if grille[l][c]!=...:#sicen'estpasunebombe
            ...               #onajoute1àsavaleur
    return .....

def genere_grille(bombes):
    """Renvoie une grille de démineur de taille nxn où n est
        le nombre de bombes,en plaçant les bombes à l'aide de
        la liste bombes de coordonnées(tuples) passée en paramètre."""
    n=len(bombes)
    #Initialisationd'unegrillenxnrempliede0
    grille=[[0 for colonne in range(n)] for ligne in range(n)]
    #Placelesbombesetcalculelesvaleursdesautrescases
    for ligne,colonne in bombes:
        grille[ligne][colonne]=...#placelabombe
        ...                       #incrémentesesvoisins
    return grille