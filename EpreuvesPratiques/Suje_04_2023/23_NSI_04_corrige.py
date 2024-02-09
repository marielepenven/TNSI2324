def a_doublon(ma_liste):
    contenu=[]
    for elt in ma_liste:
        if elt in contenu:
            return True
        else:
            contenu.append(elt)
    return False

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
    voisins=voisinage(len(grille),ligne,colonne)
    for l,c in voisins:
        if grille[l][c]!=-1:#sicen'estpasunebombe
            grille[l][c] += 1 #onajoute1àsavaleur
    return grille

def genere_grille(bombes):
    """Renvoie une grille de démineur de taille nxn où n est
        le nombre de bombes,en plaçant les bombes à l'aide de
        la liste bombes de coordonnées(tuples) passée en paramètre."""
    n=len(bombes)
    #Initialisationd'unegrillenxnrempliede0
    grille=[[0 for colonne in range(n)] for ligne in range(n)]
    print(grille)
    #Placelesbombesetcalculelesvaleursdesautrescases
    for ligne,colonne in bombes:
        print(ligne, colonne)
        grille[ligne][colonne]=-1 #placelabombe
        grille = incremente_voisins(grille,ligne,colonne)
        print(grille)
        #incrémentesesvoisins
    return grille
