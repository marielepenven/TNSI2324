def maxi(tab):
    i_max=0
    maximum=tab[i_max]
    for i in range(len(tab)):
        if tab[i]>tab[i_max]:
            i_max = i
            maximum = tab[i]
    return (i_max,maximum)


def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n-g+1 and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i+=1
    return trouve
