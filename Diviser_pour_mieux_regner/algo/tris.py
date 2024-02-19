def tri_insertion(tableau):
    j = 1
    while j < len(tableau):
        i = j-1
        temp=tableau[j]
        while i>=0 and tableau[i]>temp:
            tableau[i+1] = tableau[i]
            i = i-1
        tableau[i+1]=temp
        j = j+1
    return tableau


def tri_selection(t):

    for i in range(len(t)-1):
        min = i
        for j in range(i+1,len(t)):
            if t[j]<t[min]:
                min  = j
        if min != i:
            x = t[min]
            t[min]=t[i]
            t[i]=x
    return t            
            
def fusionner(tableau1,tableau2):
    ''' prend en paramétres deux tableaux t1 et t2 triès dans l'ordre croissant
    retourne un tableau t, composé des élèments contenus dans t1 et dans t2 et trié dans l'ordre croissant
    '''
    pass

def tri_fusion(tableau):
    pass