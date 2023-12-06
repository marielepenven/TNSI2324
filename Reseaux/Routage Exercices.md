# Routage: Exercices. 



## Exercice 1: Les adresses iPv4

1. Soit l'adresse 192.16.5.133/29. Combien de bits sont utilisés pour identifier la partie réseau? Combien de bits sont utilisés pour identifier la partie hôte? 

2. Soit l'adresse 172.16.5.10/28. Quel est le masque réseau correspondant? 

3. On attribue le réseau 132.45.0.0/16. Il faut redécouper ce réseau en huit sous-réseaux. 

   a. Combien de bits supplémentaires sont nécessaires pour définir huit sous-réseaux? 

   b. Quel est le masque réseau qui permet la création de chacun des huit sous-réseaux ainsi définis? 

   c. Quelle est l'adresse réseau de chacun des huit sous -réseaux ainsi définis? 

   d. Quelle est la plage des adresses utilisables du sous réseau numéro-3? 

   e. Quelle est l'adresse de diffusion du sous réseau numéro 4? 



## Exercice 2: Bac

Cet exercice comporte trois parties A, B et C. 

Un extrait de l'architecture réseau d'un centre hospitalier est présenté sur le schéma ci-dessous. Celui-ci met en évidence le réseau local du service de radiologie, nommé RL R et le serveur de données des patients inscrits à la sécurité sociale nommé SP. 

Dans ce réseau, R0, R1, R2, R3, R4 et R 5 représentent des routeurs. 

![](/Reseaux/IMG/ex1img1.jpg)

Les adresses et les masques réseau sont indiqués à côté de chacune des connexions sous la forme X1.X2.X3.X4/n où X1, X2, X3 et X4 représentent les 4 octets de l'adresse IP et n le nombre de bits à 1 dans le masque. On rappelle qu'un masque est constitué de 32 bits dont les n premiers bits sont à 1 et les autres à 0. Celui-ci définit avec l'adresse réseau une plage d'adresses IP dont:

- les n premiers bits, appelés "partie réseau", sont fixes;
- les bits restants, formant la "partie machine", peuvent prendre toutes les valeurs possibles. 

Les adresses IP de toutes les machines connectées à un même réseau ont donc la même partie réseau. Enfin, deux adresses IP ne peuvent être attribuées à une machine:

- celle dont tous les bits de la machine sont à 0 (adresse réseau),
- celle dont tous les bits de la partie machine sont à 1 (adresse de diffusion). 

Le repérage au niveau des interfaces de connexion des différents routeurs permet de connaitre l'adresse utilisée par routeur (passerelle) en fonction de l'adresse réseau. 

Exemples pour la liaison entre le routeur R0 et R1:

- Adresse de l'interface de R0 qui permet de communiquer avec Rz1: 58.187.10.254
- Adresse de l'interface de R1 qui permet de communiquer avec R0: 58.187.10.1

#### A. Adressage. 

1. Quels sont l'adresse et le masque du réseau local du service de radiologie (RLR)? 

2. Donner les adresses des trois interfaces du routeur R5 permettant de transmettre ou de recevoir des données. 

3. a. Donner la première et la dernière adresse IP pouvant être attribuée à une machine sur le réseau RL R. 

   b. En déduire le nombre de machines pouvant être connectées sur ce réseau. 

L'administrateur réseau du centre hospitalier souhaite statuer sur les performances de deux protocoles de routage. Il étudie donc la transmission de l'information depuis le serveur patients (SP) vers le service de radiologie (RL R). 

L'étude portera donc sur les chemins entre les routeurs R5 et R0. 

#### B. Etude du protocole RIP (Routing Information Protocol). 

Dans cette partie, tous les routeurs utilisent le protocole RIP (distance en nombre de sauts). 

1. Le serveur SP doit transmettre des données au service de radiologie (via le routeur R0) en effectuant le moins de sauts possibles. Citer les routeurs parcourus par le paquet. 

2. Suite à une opération de maintenance, le serveur R1 est déconnecté. Plus aucune paquet ne peut transiter par ce routeur. 

   Déterminer une nouvelle route empruntée par les paquets en citant les routeurs dans l'ordre. 

#### C. Protocole OSPF (Open Shortest Path First). 

Le serveur R1 est reconnecté au réseau et est fonctionnel. 

Maintenant, pour tenir compte du débit des liaisons, l'administrateur réseau décide d'étudier le protocole OSPF (distance liée au coûts des liaisons) pour effectuer le routage.

![](/Reseaux/IMG/ex1img2.jpg)

Les bandes passantes (BP) ainsi que le coût des différentes liaisons sont données dans les tableaux suivants:

![](/Reseaux/IMG/ex1img3.jpg)

Pour calculer le coût d'une liaison, on utilise la formule:

$C=\frac{Bande passante de référence}{Bande passante de la liaison}=\frac{10^{9}}{BP}$

où BP est la bande passante de la connexion en b/s (bit par seconde). 

Si le résultat du calcul n'est pas un entier, le coût est la valeur entière immédiatement supérieure. 

Exemple de calcul du coût entre R1 et R2: $\frac{10^9}{10\times10^9}=0.1$ donc le coût est de 1. 

1. Calculer  le coût de la liaison entre R2 et R3. 
2. Donner une bande passante possible de la connexion entre R3 et R4. 
3. Déterminer le chemin parcouru par un paquet partant du serveur patients (SP) vers le service de radiologie (RLR) en utilisant le procole OSPF. On précisera également le coût de ce chemin. 
4. Suite à une opération de maintenance, la liaison R0-R1 est déconnectée: plus aucun paquet ne peut transiter par cette liaison. Déterminer une nouvelle route empruntée par les paquets en citant les routeurs dans l'ordre. 

## Exercice 3 (Bac):

On considère le réseau suivant composé de sept routeurs.

![](/Reseaux/IMG/ex2img1.jpg)

On donne les tables de routage préalablement construites ci-dessous avec le protocole RIP (Routing Information Protocole). Le protocole RIP permet de construire les tables de routages des différents routeurs, en indiquant pour chaque routeur, la distance, en nombre de sauts, qui le sépare d'un autre routeur. 

![](/Reseaux/IMG/ex2img2.jpg)

1. Le routeur R2 doit envoyer un paquet de données au routeur R7 qui en accuse réception. 

   Déterminer le chemin parcouru par le paquet de données ainsi que celui parcouru par l'accusé de réception. 

2. a. Indiquer la faiblesse que présente ce réseau en cas de panne du routeur R4. 

   b. Proposer une solution pour y remédier. 

3.  Dans cette question uniquement, on décide de rajouter un routeur R8 qui sera relié aux routeurs R2 et R6. 

   a. Donner une table de routage pour R8 qui minimise le nombre de saut. 

   b. Donner une nouvelle table de routage de R2. 

4. Pour la suite de cet exercice, on considérera le réseau sans le protocole R8. 

   Il a été décidé de modifier les régles de routage de ce réseau en appliquant dorénavant le protocole de routage OSPF qui prend en compte la bande passante. 

   Ce protocole attribue un coût à chaque liaison afin de privilégier le choix de certaines routes plus rapides. Plus le coût est faible, plus le lien est intéressant. 

   Le coût d'une liaison est calculé par la formule:

   $coût = \frac{10^8bit/s}{bande passante du lien en bit/s}$

   Voici le tableau référençant les coûts des liaisons en fonction du type de liaison  entre deux routeurs:

   | Type de liaison  | bande passante | Coût |
   | ---------------- | -------------- | ---- |
   | FastEthernet(FE) | ?              | 1    |
   | Ethernet(E)      | 10 Mb/s        | ?    |
   | (E1)             | 2.048 Mb/s     | 49   |
   | (T1)             | 1,544 Mb/s     | 65   |

   On rappelle que 1 Mb/s=1000 kb/s= $10^6$ bit/s.

   a. Déterminer la bande passante du FastEthernet(FE) et justifier que le coût du réseau de type Ethernet (E) est de 10. 

   b. On précise sur le graphe ci-dessous les types de liaison dans notre réseau:

   ![](/Reseaux/IMG/ex2img3.jpg)

​				Le coût d'une chemin est la somme des coûts des liaisons rencontrées. Donner, 				en justifiant, le chemin le moins coûteux pour relier R2 à R3. Préciser le coût. 



### Exercice 4 (bac): 

1. Une adresse IPv4 est représentée sous la forme de 4 nombres séparés par des points. Chacun de ces quatre nombres peut être représenté sur un octet. 

   a. Donner en écriture décimale l'adresse IPv4 correspondant à l'écriture binaire:

   11000000.10101000.10000000.10000011 

   b. Tous les ordinateurs du réseau A ont une adresse IPv4 de la forme :  

   192.168.128._ _ _ , où seul le dernier octet (représenté par _ _ _ ) diffère.  Donner le nombre d’adresses différentes possibles du réseau A. 

2. On rappelle que le protocole RIP cherche à minimiser le nombre de routeurs  traversés (qui correspond à la métrique). On donne les tables de routage d’un  réseau informatique composé de 5 routeurs (appelés A, B, C, D et E), chacun  associé directement à un réseau du même nom obtenues avec le protocole RIP :

   ![](/Reseaux/IMG/ex3img1.jpg)

​		a. Donner la liste des routeurs avec lesquels le routeur A est directement  relié.

​	    b. Représenter graphiquement et de manière sommaire les 5 routeurs  ainsi que les 		liaisons existantes entre ceux-ci.

3. Le protocole OSPF est un protocole de routage qui cherche à minimiser la  somme des métriques des liaisons entre routeurs.  Dans le protocole de routage OSPF le débit des liaisons entre routeurs agit  sur la métrique via la relation: $métrique = \frac{10^8}{débit}$ dans laquelle le débit est exprimé en bit par seconde (bps). 

   On rappelle qu'un kbps est égal à $10^3$ bps et qu'un Mbps est égal à $10^6$ bps. 

   Recopier et compléter le tableau suivant:

   | Débit             | 100 kbps | 500 kbps | ?    | 100 Mbps |
   | ----------------- | -------- | -------- | ---- | -------- |
   | Métrique associée | 1 000    | ?        | 10   | 1        |

4. Voici la représentation d'un réseau et la table de routage incompléte du routeur F obtenue avec le protocole OSPF:

   ![](/Reseaux/IMG/ex3img2.jpg)

​	Les nombres présents sur les liaisons représentent les coûts des routes avec le  			protocole OSPF.  

​		a. Indiquer le chemin emprunté par un message d’un ordinateur du réseau F à  			   		destination d’un ordinateur du réseau I.  Justifier votre réponse.  

​		b. Recopier et compléter la table de routage du routeur F. 

​		 c. Citer une unique panne qui suffirait à ce que toutes les données des échanges  de 		tout autre réseau à destination du réseau F transitent par le routeur G.  Expliquer en 		détail votre réponse. 
