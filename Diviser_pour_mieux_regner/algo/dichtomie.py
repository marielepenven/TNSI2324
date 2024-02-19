def recherche_dichotomique(tab,element):
    ''' attention, cette fonction ne s'utilise qu'avec un tableau triè dans l'ordre croissant
    Renvoie True si element est dans le tableau, False sinon'''
    gauche = 0
    droite = len(tab)-1
    milieu = (gauche+droite)//2
    while gauche < droite:
        if tab[milieu] >element:
            droite = milieu-1
        elif tab[milieu] <element:
            gauche = milieu+1
        else:
            return True
        print(gauche,droite)
        milieu = (gauche+droite)//2
    if tab[milieu] == element:
        return True
    else:
        return False
