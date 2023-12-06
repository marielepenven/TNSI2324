# Réseaux et protocoles de routage. 



## I. Réseaux. 

#### a. Définition. 

Un réseau informatique sert à connecter des machines entre elles pour qu'elles puissent communiquer. Le mode de communication classiquement mis en place est le modèle client-serveur qui permet à des clients d'échanger des parquets d'informations avec des serveurs. 

La notion de "client" est très large. Elle peut désigner à la fois une application ou la machine sur laquelle cette application exécute. 

De même, par "serveur", on fait également référence à l'ordinateur qui héberge un service ou au logiciel qui fournit ce service. 

[(18) Le serveur informatique expliqué en dessins - YouTube: https://www.youtube.com/watch?v=CIhalbnBgA4](https://www.youtube.com/watch?v=CIhalbnBgA4)



#### b. Les différents types de réseaux. 

On utilise trois types de qualificatifs pour les réseaux. 

- **LAN** (*L*ocal *A*rea *N*etwork ou Réseau Local) : réseau local permettant de relier des ordinateurs et des périphériques situés à proximité les uns des autres.
-  *** MAN**  (*Metropolitan *A*rea *N*etwork ou Réseau Métropolitain) : série de réseaux locaux permettant de relier plusieurs LAN géographiquement à proximité.
- *** WAN** (*Wide *A*rea *N*etwork ou Réseau Etendu) : réseau étendu couvrant des vastes zones géographiques à l'échelle d'un pays ou d'un continent par exemple.

https://www.youtube.com/watch?v=CIhalbnBgA4)

## II. Protocoles de communication.



[(18) Comprendre les modèles OSI et TCP/IP - YouTube: https://www.youtube.com/watch?v=26jazyc7VNk](https://www.youtube.com/watch?v=26jazyc7VNk)

#### 1. Le modèle OSI. 

Le modèle OSI est une norme qui préconise comment les ordinateurs devraient communiquer entre eux. Il est découpé en sept morceaux appelés couches qui ont chacune un rôle défini. 


| Couche                | Role                                                         |
| --------------------- | ------------------------------------------------------------ |
| 7- Demande            | Point de contact avec les services réseaux                   |
| 6- présentation       | Elle s’occupe de tout aspect lié à la présentation des données : format, chiffrement, encodage, etc. |
| 5- session            | Elle s’occupe de tout aspect lié à la présentation des données : format, chiffrement, encodage, etc. |
| 4- Transports         | Choix du protocole de transmission et préparation de l’envoi des données. Elle spécifie le numéro de port utilisé par l’application émettrice ainsi que le numéro de port de l’application réceptrice. Elle fragmente les données en plusieurs séquences (ou segments). |
| 3- réseau             | Rôle : interconnecter les réseaux entre eux ; Rôle secondaire : fragmenter les paquets ;  Matériel associé : le **routeur** |
| 2- liaison de données | Rôle : connecte les machines entre elles sur un réseau local ; Rôle secondaire : détecter les erreurs de transmission; Matériel associé : le **switch**, ou commutateur |
| 1- physique           | Conversion des trames en bits et transmission physique des données sur le média. |






#### 2. Le protocole TCP/IP. 

TCP/IP est un protocole de liaison de données utilisé sur Internet pour permettre aux ordinateurs et autres appareils d’envoyer et de recevoir des données. L’acronyme TCP/IP signifie Transmission Control Protocol/Internet Protocol. Il permet aux appareils connectés à Internet de communiquer entre eux via les réseaux.

Le protocole TCP/IP **détermine la façon dont les ordinateurs transfèrent les données** d’un appareil à un autre. Ces données doivent rester fiables afin que le destinataire reçoive les mêmes informations que celles qu’a envoyées l’expéditeur.

Pour s’assurer que chaque communication arrive intacte jusqu’à son destinataire, le modèle TCP/IP décompose les données en *paquets* et les réassemble pour former un message complet à l’autre extrémité. Le fait d’envoyer les données sous forme de petits paquets permet une plus grande fiabilité que si toutes les données étaient envoyées en même temps.

Lorsqu’un message est décomposé en paquets, les différents paquets qui le composent peuvent prendre des voies différentes si l’un des itinéraires est encombré. C’est un peu comme envoyer par courrier plusieurs cartes d’anniversaire à la même adresse. Toutes les cartes commencent leurs parcours au même endroit, c’est-à-dire chez vous, mais vous pouvez déposer chaque carte dans une nouvelle boîte aux lettres et elles peuvent donc toutes prendre un chemin différent pour arriver jusqu’à l’adresse du destinataire.



| Etape:                                                       | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------Schéma------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Etape 1**:<br/> Le protocole TCP découpe l’information à transmettre en paquets de données. |                                                              |
| **Étape 2 :**<br/>Le protocole IP prend ensuite le relais et « encapsule » ces paquets de données : ce protocole indique la destination des données (datagrammes) grâce à un numéro (adresse IP). | ![](/Reseaux/IMG/TCP_I_img1.jpg)      |
| **Étape 3 :**<br/>Le protocole TCP s’occupe de transférer les paquets de données encapsulés (paquets IP) vers la machine réceptrice. | ![](/Reseaux/IMG/TPC_IP_img2.jpg)     |
| **Étape 4 :**<br/>Une fois que les paquets de données sont arrivées à destination, ils sont « désencapsulés » par le protocole TCP, de manière à récupérer les données TCP initialement émises. | ![](/Reseaux/IMG/TCP_IP_img3.jpg)      |
| **Étape 5 :**<br/>La machine réceptrice récupère les données TCP contenues dans les paquets ; ces dernières sont désormais dépourvues d’enveloppe. Les données contenues dans ces paquets peuvent être utilisées par la machine réceptrice. |                                                              |
| **Étape 6 :**<br/>Lorsque la machine réceptrice reçoit un paquet de données en provenance de la machine émettrice, la machine réceptrice envoie un accusé de réception à la machine émettrice. | ![](/Reseaux/IMG/TCP_IP_img4.jpg)      |



#### 3. Adressage IP. 

#### a. Les adresses IP. 

Pour permettre le transport des datagrammes, chacun des éléments d'une infrastructure (clients, serveurs, périphériques, objets connectés, switchs, routeurs....) doit posséder une adresse unique sur le réseau: c'est l'adresse IP. 

Il existe des adresses IP de version 4sur 32 bits, et de version 6 sur 128 bits. 

La version 4 est actuellement la plus utilisée : elle est généralement représentée en notation décimale avec quatre nombres compris entre 0 et 255, séparés par des points, ce qui donne par exemple « 181.174.87.53 ».

![](/Reseaux/IMG/adresse_IPV4.jpg)

Quel est le nombre d'adresse IP v4 disponible? Pourquoi est ce que cela pose un problème? 

Une **adresse IPv6** est une adresse IP de la version 6 du protocole internet (IPv6). IPv6 a été principalement développé en réponse à la demande d'adresses qu'IPv4 ne permettait plus de contenter. Une adresse IPv6 contient 128 bits , contre 32 bits pour IPv4. On dispose ainsi de $2^{128} ≈ 3,4 × 10^{38}$ d'adresses IPv6, contre $2^{32} ≈ 4$ milliards d'adresses IPv4.

![](/Reseaux/IMG/adresse_IPV6.jpg)

#### b. Masque de sous-réseau. 

Un sous -réseau est une subdivision logique d'un réseau de taille plus importante. 

Les adresses IPv4 sont composées de deux parties:

- l'identifiant du sous-réseau auquel appartient la machine,
- l'identifiant de la machine à l'intérieur du sous-réseau. 

Les masques de sous-réseau se note de deux façons différentes:

- la notation classique qui couple l'adresse IP et son masque de sous-réseau associé. 

  ![](/Reseaux/IMG/masque1.png)



- la notation CIDR avec un slash qui associe également l'adresse IP d'un hôte à son masque de sous-réseau mais on se contente cette fois de spécifier le nombre de bits à 1 en partant de la gauche (bits de poids fort). 

  ![](/Reseaux/IMG/masque2.png)

Nous distinguerons 4 modes de communication: 

- unicast: la communication a lieu entre une source et une destination,
- multicast: une source envoie le même contenu à plusieurs destinations,
- broadcast: les données sont envoyées à toutes les interfaces du réseau local,
- anycast: plusieurs destinations possèdent la même adresse IP. La communication a lieu entre une source IP et l'IP de la destination la plus proche de la source. Ce mode de communication est souvent utilisé pour équilibrer la charge sur plusieurs serveurs. 

Soit un réseau local d'adresse 10. 5. 142. 0/24. 

- l'adresse 10.5.142.0 identifie le préfixe du réseau local. 
- l'adresse 10.5.142.1 est la première adresse utile du réseau local. 
- l'adresse 10.5.142.255 est l'adresse du broadcast, pour joindre toutes les machines du réseau local. 

## II. Matériel. 

### a. La carte réseau. 

Chaque hôte du réseau (ordinateur, imprimante …) possède une carte réseau (NIC Network Interface  Card) qui permet de mettre en forme, d’envoyer et de contrôler les données sur le réseau. Celle-ci  possède une adresse physique unique (adresse MAC) et une adresse logique (adresse IP). 

Une **carte réseau** est matérialisée par un ensemble de composants électroniques soudés sur un circuit imprimé. L'ensemble constitué par le circuit imprimé et les composants soudés s'appelle une carte électronique, d'où le nom de carte réseau. La carte réseau assure l'interface entre l'équipement ou la machine dans lesquels elle est montée et les machines connectées sur le même réseau.



![](/Reseaux/IMG/carte_reseau.jpg)



### b. Le switch. 

Un switch, un commutateur ou encore un commutateur réseau en français, est un équipement qui fonctionne comme une multiprise ou si on reste sur le volet informatique un pont multiport… qui permet de relier plusieurs segments d’un réseau informatique entre eux. Dit plus simplement, il s’agit d’un boîtier doté de quatre à plusieurs dizaines de ports Ethernet, et qui sert à relier en réseau différents éléments du système informatique.



Le switch est chargé d’analyser les trames qui arrivent sur les ports d’entrée. Il opère une filtration des données afin de les orienter vers le bon port. Il a donc une double fonction de filtrage et de connectivité. Il sert de véhicule au transport de trame, comme peut également le faire le routage. Il peut au delà de le faire physiquement, créer également des circuits virtuels.

![](/Reseaux/IMG/switch.jpg)

### c. Le modem. 

Délivré par les fournisseurs d’accès à internet (SFR, Orange, Bouygues, Free…), un modem (pour modulateur-démodulateur) est un périphérique qui permet de se connecter à internet. C’est en quelque sorte la « porte d’accès » à internet : il convertit la connexion internet entrante au sein d’une maison par câble coaxial, par ligne téléphonique ou par fibre optique en connexion Ethernet, donnant ainsi accès au Web aux périphériques connectés de la maison.

### d. Le routeur. 

Un routeur relie des machines situées sur des réseaux informatiques différents. Il assure  l’acheminement des données, le contrôle et le filtrage du trafic et le routage qui consiste à trouver le  chemin optimal entre la machine émettrice et la machine réceptrice. 

Le routeur dispose pour cela d'une  **table de routage** qui lui permet de choisir selon la rapidité ou selon le nombre de routeurs à traverser le  chemin optimal. 

Un routeur est constitué de deux interfaces ou passerelles qui lui permettront de se connecter aux deux  réseaux. Chaque interface possède une adresse adresses IP dans chacun des deux réseaux. Certains routeurs intègrent un point d’accès WiFi ce qui permet la connexion au réseau d’équipements  sans-fil.

![](Reseaux/IMG/routeur.jpg)

### e. La box. 

Les « box » proposées par les FAI intègrent un modem, un routeur NAT (Network Address Translation)  et point d’accès Wifi. La box est identifiée par une adresse IP unique fournie par son fournisseur d’accès  internet. 

Le routeur NAT permet d'associer une adresse IP privée (par exemple 192.168.0.1) à une adresse IP  publique unique fournie par le FAI et de faire la traduction, dans un sens comme dans l'autre, en  modifiant l'adresse dans le paquet IP.



## III. Protocoles de routage. 

Le routage est la base du fonctionnement d’Internet. Lorsqu’il reçoit un paquet, un routeur l’analyse pour récupérer l’adresse de sa destination. 

En fonction de cette adresse, il doit choisir vers quel routeur voisin retransmettre ce paquet pour le faire progresser vers sa destination. Il choisit ce voisin à l’aide de sa table de routage, qui associe les adresses de destination à des adresses de routeurs. De cette manière, un paquet transite de routeur en routeur jusqu’au client ou au serveur à qui il est destiné.



### a. Table de routage. 

Chaque routeur possède une table de routage. Une table de routage peut être vue comme un tableau donnant pour chaque destination  connue par le routeur la «porte de sortie » à emprunter ainsi que l’efficacité de cette route (selon différents critères en fonction des algorithmes utilisés) et contient donc les informations permettant au routeur d’envoyer le paquet de données dans la « bonne direction ».

Un routeur possède plusieurs interfaces réseau (eth0, eth1, ...), par lequel il est connecté à des sous-réseaux (autre routeur, réseau local, ...) au sein desquels il possède une adresse IP.

![](/Reseaux/IMG/table_de_routage.png)



Dans la table de routage d’un routeur, on trouve les informations suivantes :

- Les adresses IP du routeur
- Les adresses IP des sous-réseaux auquel il est connecté
- Les routes (directions à prendre) qu’il faut suivre pour atteindre un réseau
  - route par défaut (il en faut bien une)
  - routes statiques (configurées explicitement par l’administrateur)
  - routes dynamiques (apprises par des protocoles de routage dynamique)

Chaque ligne de la table contient une route :

- l’adresse du réseau de destination
- la direction à prendre pour l’atteindre :
  - Interface de sortie du routeur (adresse du routeur sur le sous-réseau de sortie)
  - Passerelle (adresse de la prochaine machine sur le sous-réseau de sortie)
- la distance à parcourir (la métrique) avant de l’atteindre

Lorsqu’un routeur reçoit un paquet, il récupère l’adresse du réseau de destination :

- si cette adresse est dans sa table de routage, il envoie le paquet vers l’interface associée,
- dans le cas contraire le paquet est envoyé via l’interface par défaut.

*Exemples* :

*si le routeur reçoit un paquet à destination de l’ordinateur 192.168.7.2 / 24, sa table de routage pourra contenir la route suivante :*

| Réseau destination | Passerelle | Interface | Métrique |
| ------------------ | ---------- | --------- | -------- |
| 192.168.7.0/24     |            | eth1      | 1        |

*l’ordinateur est directement relié au routeur,*

- *il n’y a donc pas besoin de passerelle pour l’atteindre*
- *la métrique est de 1 (un seul « saut »)*

*si le routeur reçoit un paquet à destination de l’hôte 172.21.34.21 /16, sa table de routage pourra contenir la route suivante :*

| Réseau destination | Passerelle | Interface | Métrique |
| ------------------ | ---------- | --------- | -------- |
| 172.21.0.0/16      | 10.1.2.2   | eth0      | 8        |

*si le routeur reçoit un paquet à destination d’un réseau qui n’est pas dans sa table, il choisit la route par défaut :*

| Réseau destination | Passerelle | Interface | Métrique |
| ------------------ | ---------- | --------- | -------- |
| défaut             | 10.1.2.2   | eth0      | 1        |

*Remarque : en pratique une table de routage ne comporte que des adresses IP. Par conséquent :*

- *l’adresse du réseau de destination n’est pas au format CIDR mais au format IP réseau+masque réseau* 192.168.7.0 /24 → 192.168.7.0 et 255.255.255.0
- *l’interface est décrite par la propre adresse IP du routeur dans le sous-réseau auquel il est connecté avec cette interface* eth1 → 192.168.7.254
- *le réseau de destination de la route par défaut est noté 0.0.0.0*

On peut trouver dans une table de routage plusieurs lignes pour une même destination, il peut en effet, à partir d’un routeur donné, exister plusieurs chemins possibles pour atteindre la destination. Dans le cas où il existe **plusieurs chemins possibles** pour atteindre la même destination, le routeur va choisir **le « chemin le plus court«** , celui ayant la valeur de métrique la plus petite (un réseau directement lié à un routeur aura une métrique de 1). Pour les réseaux dont lamétrique est supérieure à 1, il existe 2 méthodes :

- le **routage statique** : chaque ligne doit être renseignée « à la main ». Cette solution est seulement envisageable pour des très petits réseaux ;
- le routage dynamique : tout se fait « automatiquement », on utilise des protocoles, partagés par tous les routeurs du réseau, qui vont leur permettre d’échanger des informations sur l’état du réseau afin de remplir leur table de **routage** automatiquement.

Un réseau de réseaux comportant des routeurs peut être modélisé par un **graphe** : chaque routeur est un **sommet** et chaque liaison entre les routeurs ou entre un routeur et un switch est une **arête**. Les algorithmes utilisés par les protocoles de routages sont donc des algorithmes issus de la **théorie de graphes**. (vu plus tard dans l'année).

### b. le protocole RIP. 

#### 1. Principe. 

Les protocoles de routage à vecteur de distances ou routage vectoriel sont des protocoles permettant de construire des tables de routages où aucun routeur ne possède la vision globale du réseau, la diffusion des routes se faisant de proche en proche. 

Le protocole **RIP** (**Routing Information Protocol**) est l’un des plus anciens protocoles de routage vectoriel de distance qui utilise le nombre de sauts comme  métrique de routage. RIP empêche les boucles de routage en implémentant une limite sur le nombre de sauts autorisés dans un chemin de la source à la destination. Le plus grand nombre de sauts autorisés pour RIP est de 15, ce qui limite la taille des réseaux que RIP peut prendre en charge.

Le principe du protocole RIP est le suivant: chaque routeur transmet à ses voisins les adresses de ses propres voisins ou celle qu'il a reçues par d'autres routeurs. En plus des adresses, le routeur indique la distance, exprimée en nombre de sauts, qui le sépare d'une machine donnée, c'est à dire le nombre de routeurs qu'il est nécessaire de traverser afin de rejoindre la machine cible. Ce sont donc des couples (adresse, distance), appelés vecteurs de distance qui sont échangés avec ce protocole. C'est grâce à ces indications de distance qu'un routeur va pouvoir choisir la meilleure route, c'est à dire celle qui traverse le moins de routeurs pour atteindre une machine. 

#### 2. Exemple.

Travaillons sur un exemple: 

Soit le réseau suivant:

![](/Reseaux/IMG/RIP_img1.jpg)

Au début du protocole, les tables des routeurs R1 et R3 sont initialisées avec les informations concernant leurs voisins immédiats, à savoir les adresses des sous-réseaux sur lesquels ils sont directement connectés. 

Table de routage de R1

| destination    | passerelle | interface | distance |
| -------------- | ---------- | --------- | -------- |
| 10.1.1.0/30    |            | eth0      | 1        |
| 192.168.1.0/24 |            | wifi0     | 1        |

Table de routage de R3

| destination | passerelle | interface | distance |
| ----------- | ---------- | --------- | -------- |
| 10.1.1.0/30 |            | eth1      | 1        |
| 10.1.2.0/30 |            | eth3      | 1        |
| 10.1.3.0/30 |            | eth2      | 1        |
| 10.1.4.0/30 |            | eth0      | 1        |

Après cette phase d'initialisation, un routeur poursuit le protocole RIP en échangeant des demandes RIP avec ses voisins. Ainsi, lorsqu'un de ses voisins reçoit une telle demande, il doit accuser réception en lui envoyant sa table en réponse. 

Lorsque le routeur reçoit la réponse de son voisin, il a quatre possibilités:

1. Il découvre une nouvelle route vers un sous-réseau qui lui étant jusque là inconnu. Il l'inscrit dans sa table. 
2. Il découvre une route plus courte vers un sous-réseau connu mais passant par un autre routeur. Il efface l'ancienne route de sa table et inscrit la nouvelle. 
3. Il reçoit une nouvelle route plus longue, il l'ignore. 
4. Il reçoit une route existante, mais plus longue, vers un routeur passant par le même voisin. Cela veut dire qu'un problème est apparu sur son ancienne route. Il met donc à jour sa table avec cette nouvelle route. 

Ainsi, après avoir échangé une demande RIP avec R3, la table du routeur R1 contient les informations suivantes. 

Table de routage de R1. 

| destination    | passerelle | interface | distance |
| -------------- | ---------- | --------- | -------- |
| 10.1.1.0/30    |            | eth0      | 1        |
| 192.168.1.0/24 |            | wifi0     | 1        |
| 10.1.2.0/30    | 10.1.1.2   | eth0      | 2        |
| 10.1.3.0/30    | 10.1.1.2   | eth0      | 2        |
| 10.1.4.0/30    | 10.1.1.2   | eth0      | 2        |

Compléter la table de routage du routeur R3 après une demande RIP avec R1. 

| destination | passerelle | interface | distance |
| ----------- | ---------- | --------- | -------- |
| 10.1.1.0/30 |            | eth1      | 1        |
| 10.1.2.0/30 |            | eth3      | 1        |
| 10.1.3.0/30 |            | eth2      | 1        |
| 10.1.4.0/30 |            | eth0      | 1        |
|             |            |           |          |

En répétant ces demandes RIP et en mettant à jour leurs tables de routages selon l'algorithme décrit ci-dessous, les routeurs vont finir au bout d'un certain temps par avoir la même vision du réseau et des meilleures routes à suivre pour acheminer un paquet. 

Par exemple, la table de routage finale pour le routeur R1 est la suivante:

| destination    | passerelle | interface | distance |
| -------------- | ---------- | --------- | -------- |
| 10.1.1.0/30    |            | eth0      | 1        |
| 192.168.1.0/24 |            | wifi0     | 1        |
| 10.1.2.0/30    | 10.1.1.2   | eth0      | 2        |
| 10.1.3.0/30    | 10.1.1.2   | eth0      | 2        |
| 10.1.4.0/30    | 10.1.1.2   | eth0      | 2        |
| 10.1.7.0/30    | 10.1.1.2   | eth0      | 3        |
| 192.168.6.0/24 | 10.1.1.2   | eth0      | 4        |

#### 3. Détection des pannes. 

Le protocole RIP doit également permettre de déterminer si une liaison est en panne. Pour cela, un routeur considère qu'un voisin est en panne s'il ne reçoit pas de réponse à une demande RIP après un certain laps de temps. Par défaut, ce délai est de trois minutes. Quand un routeur détecte qu'un sous-réseau devient inaccessible, il envoie à ses voisins cette information sous la forme d'une route avec une distance infinie, qui correspond pour RIP à une valeur de 16.

#### 4. Délai de convergence. 

Les distances ne pouvant pas être supérieures à 15 sauts, les routeurs ne peuvent pas connaître les plus courts chemins pour atteindre un sous-réseau qui nécessite une route trop longue. 

Cela limite de fait l'usage de RIP à des réseaux de petites tailles. Le choix de cette limite est fait pour diminuer le délai de convergence du protocole, c'est à dire le temps nécessaire pour que tous les routeurs aient la même vue de la topologie du réseau. Plus la limite est haute et plus le temps nécessaire pour converger est important. 

### c. le protocole OSPF. 

Nous avons vu que le protocole RIP permettait de configurer les tables de routage avec les routes les plus courtes en nombre de routeurs traversés. Toutefois, cette notion de distance ne garantit pas que les routes soient les plus rapides possibles. En effet, elles ne tiennent pas compte du débit puisque la nature de la liaison n'est pas intégrée. 

Pour pallier à ce défaut, le protocole **OPSF (Open shortest Path First)** a été développé dans les années 90.  C'est un algorithme dit à état de liens.

Ce protocole prend en compte la bande passante des liaisons de communications pour calculer les meilleures routes. 

La bande passante est la quantité d'information qui peut être transmise par unité de temps. 

#### 1. Coût des liaisons. 

On mesure ce débit en nombre de bits par seconde (bit/s ou bps). 

Rappel des préfixes utilisés:

kilo (kbit/s): $10^3$ bit/s

Mega (mbit/s): $10^6$ bit/s

Giga (gbit/s): $10^9$ bit/s

Contrairement au protocole RIP, le nombre de routeurs traversés par un paquet n'a plus d'importance dans le choix de la route. La notion de distance utilisée par OPSF est uniquement liée aux coûts des liaisons qu'il faut emprunter pour relier deux routeurs. 

A chaque liaison, on associe donc une métrique qui dépend du débit des connexions entre les routeurs. On appelle cette métrique coût et on la définie par la formule suivante:

coût=${10^{8}}/{d}$ où d représente la bande passante en bit/s entre les deux routeurs. Ainsi un lien avec une forte bande passante aura un coût très faible et sera donc privilégié par rapport à un lien avec une bande passante plus faible. 

Exemple:

1. Calculer le coût d'une liaison à 10Mbit/s.
2. Calculer le coût d'une liaison à 1 Gbit/s. 
3. Quelle est la bande passante d'une liaison avec un coût de 1? 

#### 2. principe. 

[Le routage à état de liens 📶 - YouTube](https://www.youtube.com/watch?v=-utHPKREZV8&t=160s)

Le fonctionnement du protocole OSPF est découpé en deux grandes étapes :

- chaque routeur, après avoir été initialisé, tente de découvrir ses voisins afin d’établir une relation de voisinage : les machines dans ce protocole sont classées en différentes zones. Les routeurs limitent leur recherche de voisins dans la zone qui leur est affectée :

  - le routeur choisit un identificateur unique, par exemple sa plus grande adresse IP parmi celles de ses sous-réseaux ;
  - le routeur poursuit en envoyant des messages de type HELLO à travers tous ses interfaces réseaux;
  - quand un autre routeur reçoit un paquet HELLO du routeur, il vérifie si son identificateur apparaît déjà dans sa liste de voisins :
    - Si c’est le cas, il envoie un accusé de réception
    - Sinon il répond en envoyant les informations dont il dispose sur la topologie du réseau. Les routeurs d’une même zone ont ainsi toute la même vision du réseau.

- l’algorithme de type **algorithme de Disjktra** pour calculer les meilleures routes (coût le plus faible) entre chaque routeur de la zone est ensuite exécuté. Les tables de routage sont ainsi mises à jour.

  [Algorithme de Dijkstra (5 min. pour comprendre) - YouTube](https://www.youtube.com/watch?v=MybdP4kice4&t=5s)

  

  

Le protocole OSPF est donc bien plus performant que RIP mais plus complexe d'utilisation et destiné aux grands réseaux. Les avantages sont par exemple :

- pas de limite de sauts
- permet à chaque routeur une connaissance complète des réseaux au sein d’une zone
- élimine le danger des boucles de routage
- les mises à jour ne sont envoyées que lors d’un changement de topologie

#### 3. Exemple. 

![](/Reseaux/IMG/opsf_exple.jpg)

En vous basant sur le protocole OSPF (métrique = somme des coûts), déterminez la table de routage du routeur A

On donne les débits suivants :

- liaison routeur A - routeur B : 1 Mbps
- liaison routeur A - routeur C : 10 Mbps
- liaison routeur C - routeur B : 10 Mbps

Quel est, d'après la table de routage construite ci-dessus, le chemin qui sera emprunté par un paquet pour aller d'une machine ayant pour adresse IP 172.18.1.1/16 à une machine ayant pour adresse IP 172.16.5.3/16 ?

 
