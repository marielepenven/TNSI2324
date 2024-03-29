# TP: Chiffrer, déchiffrer. 

### I. Le code de césar. 

1. Chiffrer le message suivant "LA NSI, C'EST FORMIDABLE", en utilisant avec une clé égale à 8. 
2. Sachant que le message suivant " T'KSWO VO MRYMYVKD" a été chiffré avec une clé de 16, quel est le message en clair? 
3. Compléter le script `cesar_élève.py`que vous avez reçu via l'ent (ou demandez le à votre enseignante si elle a encore oublié de l'envoyer). 

### II. Le Chiffre de Vigenère. 

![](/securisation_des_donnees/IMG/vigenere.jpg)

1. en utilisant la table de Vigenère ci-dessus, chiffrer le message suivant "DEMAIN, TOUT IRA BIEN", avec la clé "CIEL". 
2. en utilisant la table de Vigenère ci-dessus, déchiffrer le message suivant "ZT IFK BIZGA H NCTIE JM GBLKLRI", avec la clé "RIEN".
3. Reprendre la structure du code `cesar_élève.py`et implémenter les fonctions permettant de coder et de décoder un message à l'aide de la table de Vigenére. Est-il possible d'écrire une fonction `trouver_la_clé`? Justifier votre réponse. 



