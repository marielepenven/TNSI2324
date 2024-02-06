def correspond(mot,mot_a_trous):
    if len(mot)!=len(mot_a_trous):
        return False
    else:
        for i in range(len(mot)):
            if mot[i]!= mot_a_trous[i] and mot_a_trous[i] != "*":
                return False
        return True
    
            

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant 
    à un plan d'envoi de messages entre `N` personnes A, B, C, 
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon. 
    '''
    personne = 'A'
    N = len(plan)                          
    for i in range(N-1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True
