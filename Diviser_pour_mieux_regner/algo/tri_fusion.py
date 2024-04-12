def fusionner(tableau1,tableau2):
    ''' prend en paramétres deux tableaux t1 et t2 triès dans l'ordre croissant
    retourne un tableau t, composé des élèments contenus dans t1 et dans t2 et trié dans l'ordre croissant
    '''
    tableau = []
    debut1=0
    debut2=0
    while debut1<len(tableau1) and debut2<len(tableau2):
        if tableau1[debut1]<tableau2[debut2]:
            tableau.append(tableau1[debut1])
            debut1 += 1
        else:
            tableau.append(tableau2[debut2])
            debut2 += 1
    if debut1<len(tableau1):
        for i in range(debut1,len(tableau1)):
            tableau.append(tableau1[i])
    if debut2<len(tableau2):
        for j in range(debut2,len(tableau2)):
            tableau.append(tableau2[j])
    return tableau

def tri_fusion(tableau):
    if len(tableau)<=1:
        return tableau
    else:
        n = len(tableau)
        tableau1=tableau[0:n//2]
        print(tableau1)
        tableau2=tableau[n//2:len(tableau)]
        print(tableau2)
        return fusionner(tri_fusion(tableau1),tri_fusion(tableau2))