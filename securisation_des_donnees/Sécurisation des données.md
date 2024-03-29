# Sécurisation des données


Avec la démocratisation d'internet, du web et la diversification des usages, des problèmes de sécurisation sont apparus. 

En effet, les données transmises par le protocole de la couche d'application sont découpés en paquet TCP, eux-même encapsulés dans des paquets IP. Ces paquets IP sont envoyés par la source au prochain routeur de son sous-réseaux. Ce routeur retransmet ensuite le paquet au routeur suivant et ainsi de suite jusqu'à l'arrivée à destination. Chaque routeur peut donc inspecter les paquets pour en connaître le contenu. Cette situation n'est clairement pas idéale. En effet, si l'on utilise un site web pour effectuer des transactions bancaires ou pour transmettre des informations personnelles, on ne souhaite alors que les données transmises ne soient connues que par la source et la destination. 

Ce simple constat nous permet de mettre en avant trois aspects liés à la sécurisation des données:

- comment chiffrer le contenu des communications, afin qu'elles ne soient lisibles que par la source et la destination? 
- comment garantir que le serveur auquel on se connecte est bien celui de la personne ou de l'entité auquel on pense se connecter? 
- comment garantir les deux propriétés ci-dessus en réutilisant l'infrastructure d'Internet, à savoir le protocole TCP/IP? 



## I. Chiffrement symétrique des données. 

### a. Principe. 

La **cryptographie symétrique**, également dite **à clé secrète **est la plus ancienne forme de chiffrement. Elle permet à la fois de chiffrer et de déchiffrer des messages à l'aide d'une même clé. On a des traces de son utilisation par les égyptiens vers 2000 av. J.-C.

![](/securisation_des_donnees/IMG/chiffrement_symétrique.jpg)

Le terme de symétrique vient du fait que la même clé est utilisée pour chiffrer et déchiffrer le message. 

### b. Le code de César. 

Le **chiffrement par décalage**, aussi connu comme  le **code de César**, est une méthode de chiffrement symétrique très simple utilisée par Jules César dans ses correspondances secrètes. 

Le texte chiffré s'obtient en remplaçant chaque lettre du texte clair original par une lettre à distance fixe, toujours du même côté, dans l'ordre de l'alphabet. Pour les dernières lettres (dans le cas d'un décalage à droite), on reprend au début. 

Par exemple avec un décalage de 3 vers la droite, `A` est remplacé par `D`, `B` devient `E`, et ainsi jusqu'à `W` qui devient `Z`, puis `X` devient `A` etc. Il s'agit d'une permutation circulaire de l'alphabet. La longueur du décalage, 3 dans l'exemple évoqué, constitue la *clé* du chiffrement qu'il suffit de transmettre au destinataire — s'il sait déjà qu'il s'agit d'un chiffrement de César — pour que celui-ci puisse déchiffrer le message. Dans le cas de l'alphabet latin, le chiffre de César n'a que 26 clés possibles (y compris la clé nulle, qui ne modifie pas le texte).

![](/securisation_des_donnees/IMG/cesar.jpg)



Cette méthode de chiffrement est très facilement crackable, en effet, une analyse des fréquences des lettres permet de trouver aisément la clé. 

### c. Le chiffre de Vigenère. 

Le chiffre de Vigenère est un système de chiffrement inventé par "Blaise Vigenère" (1523-1596) qui mit en échec les cryptanalystes durant trois siècles. 

Cette méthode de chiffrement est utilisable grâce à la table de Vigenère qui est un tableau carré permettant de chiffrer le mot ou la phrase selon la clé choisie. Blaise Vigenère décrit sa méthode de chiffrement dans un ouvrage intitulé *Traité des chiffres* paru en 1586.

Il a été découvert par le major prussien Friedrich Kasiski qui publie sa méthode en 1863.

![](/securisation_des_donnees/IMG/vigenere.jpg)

Pour utiliser le chiffre de Vigenère, il faut avoir en sa possession : la table de Vigenère (représentée ci-dessus), une phrase à modifier pour lui donner un sens incompréhensible et un mot clé :

- phrase : je suis en vacances en Espagne.
- mot clé : balais.

#### 1. Chiffrement. 

Pour que ça marche il faudra qu'il y ait le même nombre de lettres dans le mot clé que dans la phrase, pour ça il faudra répéter les lettres qu'il y a dans le mot *balais* pour qu'il y en ait autant que dans la phrase ce qui donne :

- phrase: je suis en vacances en Espagne
- mot clé: ba lais ba laisbala is balaisb

Maintenant qu'on a autant de lettres dans la phrase que dans le mot clé, voyons comment transformer cette phrase banale en une phrase chiffrée, incompréhensible pour les personnes ne connaissant pas cette méthode de chiffrement.

Pour cela il suffit de prendre la colonne correspondant à la première lettre de la phrase et la rangée (ligne horizontale) de la première lettre de la clé, et au croisement de ces lignes vous trouverez une lettre étant la première lettre de votre phrase chiffrée.

Ce qui donne avec notre exemple au croisement de la colonne J (première lettre du mot *je*) et de la rangée B (première lettre du mot-clé *balais* la lettre K pour chiffrer la lettre J de *je*. Pour chiffrer le E(seconde lettre du mot *je*) de *je* on croise la colonne E avec la rangée A (seconde lettre de balais) ce qui donne un E; pour chiffrer le S du mot *suis* (troisième lettre de la phrase à chiffrer) on croise la colonne S avec la rangée L (troisième lettre de balais) ce qui correspond à la lettre D et ainsi de suite: la phrase à chiffer donnera la suite suivante de lettres : *KeduqkfngaksocpsmfFsaaoff.* 

#### 2. Déchiffrement

Pour déchiffrer il suffit de prendre la colonne correspondant à la première lettre de la clé et de chercher dans cette colonne la lettre correspondant à la première lettre de la phrase codée, elle sera sur la ligne de la première lettre de la phrase normale (lettre qui se trouve dans la colonne la plus à gauche). Ainsi dans l'exemple choisi: dans la colonne de B la première lettre de *balais* le K correspond à la lettre J dans la colonne de gauche, donc il s'agit de la première lettre du mot *je*. La lettre A seconde lettre du mot-clé *balais* croisé avec la lettre E seconde lettre du mot à déchiffrer donne E dans la colonne de gauche., ce qui correspond au E seconde lettre de la phrase d'origine: la lettre L troisième lettre du mot-clé *balais* croisé avec la lettre D troisième lettre du mot chiffré correspond au S dans la colonne de gauche soit la troisième lettre du mot de la phrase d'origine (le premier S du mot *suis*). Il n'y a plus qu'à reproduire cette étape pour toutes les lettres.

Si cette méthode est beaucoup plus difficile à cracker, il demeure tout de même la question de la transmission de la clé qui peut s'avérer délicate. Comment est sur que celle-ci ne soit pas interceptée ? 



## II. Chiffrement asymétrique. 

### a. Principe. 

La **cryptographie asymétrique**, ou **cryptographie à clé publique** est un domaine relativement récent de la cryptographie. Elle permet d'assurer la confidentialité d'une communication, ou d'authentifier les participants, sans que cela repose sur une donnée secrète partagée entre ceux-ci.

La cryptographie asymétrique peut être illustrée avec l'exemple du chiffrement à clé publique et privée, dont le but, comme tout chiffrement, est de garantir la confidentialité d'une donnée lors d'une transmission de celle-ci. Le terme asymétrique s'explique par le fait qu'il utilise deux clés différentes, l'une, la **clé publique**, pour chiffrer, l'autre, la **clé privée**, pour déchiffrer. L'utilisateur qui souhaite recevoir des messages engendre un tel couple de clés. Il ne transmet à personne la clé privée alors que la clé publique est transmissible sans restriction.  Quiconque souhaite lui envoyer un message confidentiel utilise la clé publique pour chiffrer celui-ci. Le message chiffré obtenu ne peut être déchiffré que connaissant la clé privée. Il peut donc être communiqué publiquement : la confidentialité du message original est garantie. Le destinataire, qui n'a communiqué à personne sa clé privée, est le seul à pouvoir, à l'aide de celle-ci, déchiffrer le message transmis pour reconstituer le message original. 

Ce système a deux utilisations majeures :

- la  confidentialité des messages reçus : c'est celle qu'on vient de décrire, l'expéditeur utilise la clé publique du destinataire pour chiffrer son message. Le destinataire utilise sa clé privée pour déchiffrer le message de l'expéditeur, garantissant la confidentialité du contenu ;
- l'authentification de l'expéditeur d'un message (pas nécessairement confidentiel) : l'expéditeur utilise sa clé privée pour chiffrer un message que n'importe qui peut déchiffrer avec la clé publique de l'expéditeur, ce qui garantit que le message a été chiffré par l'expéditeur, seul à posséder la clé privée ; c'est le mécanisme utilisé par la signature numérique pour authentifier l'auteur d'un message. 

![](/securisation_des_donnees/IMG/Chiffrement_asymétrique.png)

### b. RSA. 



Le **chiffrement RSA** (nommé par les initiales de ses trois inventeurs) est un algorithme de cryptographie très utilisé dans le  commerce et plus généralement pour échanger des données confidentielles sur Internet. 

Cet algorithme a été décrit en 1977 par Ronald Rivest, Adi Shamir et Leonard Adleman. RSA a été breveté par le Massachussets Institute of Technology en 1983 aux Etats Unis. Le brevet a expiré le 21 septembre 2000.

Le chiffrement RSA est *asymétrique* : il utilise une paire de clés (des nombres entiers) composée d'une *clé publique* pour chiffrer et d'une *clé privée* pour déchiffrer des données confidentielles.

 Les deux clés sont créées par une personne, souvent nommée par convention *Alice*, qui souhaite que lui soient envoyées des données confidentielles. Alice rend la clé publique accessible. Cette clé est utilisée par ses correspondants (*Bob*, etc.) pour chiffrer les données qui lui sont envoyées. La clé privée est quant à elle réservée à Alice, et lui permet de déchiffrer ces données. La clé privée peut aussi être utilisée par Alice pour signer une donnée qu'elle envoie, la clé publique permettant à n'importe lequel de ses correspondants de vérifier la signature.

Une condition indispensable est qu'il soit « calculatoirement impossible » de déchiffrer à l'aide de la seule clé publique, en particulier de reconstituer la clé privée à partir de la clé publique, c'est-à-dire que les moyens de calcul disponibles et les méthodes connues au moment de l'échange (et le temps que le secret doit être conservé) ne le permettent pas.

![](/securisation_des_donnees/IMG/rsaalicebob.jpg)

Si vous faites Maths expertes, vous pouvez vous pencher sur le cryptage RSA (ce qui fait un bon sujet de grand oral) !

Je vous conseille la lecture de cet article: [Nombres premiers et cryptologie : l’algorithme RSA - Interstices](https://interstices.info/nombres-premiers-et-cryptologie-lalgorithme-rsa/)



## III. Authentification des participants. 

Nous avons vu que, lorsqu'une entité (entreprise, association, individu, service public, etc.) veut sécuriser ses communications (entrantes et sortantes) auprès d'un large public, le chiffrement le plus simple et le plus sécurisé est l'asymétrique à clé publique : l'entité n'a qu'à diffuser sa clé publique à l'ensemble de son audience.

Toutefois, des difficultés demeurent. En effet, un problème vient de la transmission de la clé publique. Si celle-ci n'est pas sécurisée, un attaquant peut se positionner entre l'entité et son public en diffusant de fausses clés publiques (par le biais d'un faux site web par exemple) puis intercepter toutes les communications, lui permettant d'usurper l'identité du diffuseur de clés publique et de créer une attaque de l'homme du milieu (ou de la femme parce qu'il n'y pas de raison ). 

![](/securisation_des_donnees/IMG/attaquehommedumilieu.jpg)

Dans un cadre fermé et relativement restreint (entreprise, service public…) la diffusion de clés sécurisées est relativement simple et peut prendre de nombreuses formes, mais quand le diffuseur souhaite s'adresser à un public plus large avec lequel il n'a pas eu de contact préalable (grand public, public international), elle nécessite un cadre normalisé.

Les certificats résolvent le problème du canal sécurisé grâce à la signature de tiers de confiance qui émet un certificat électronique. 

Un **certificat électronique** est un ensemble de données contenant :

- au moins une clé publique ;
- des informations d'identification, par exemple : nom, localisation, adresse électronique.
- au moins une signature (construite à partir de la clé privée) ; de fait quand il n'y en a qu'une, l'entité signataire est la seule autorité permettant de prêter confiance (ou non) à l'exactitude des informations du certificat.

Les certificats électroniques et leur cycle de vie peuvent être gérés au sein d'infrastructures à clés publiques. 

![](securisation_des_donnees/IMG/certificatelectronique.jpg)

## IV. Le protocole HTTPS

Nous avons étudié en classe de première le protocole HTTP (HyperText Transfer Protocol). Les données échangées par ce protocole ne sont pas cryptées et cela présente un sérieux problème de sécurité tant dans la communication des données que dans l'authentification des serveurs.

Pour combler ces failles, les protocoles SSL (Secure Socket Layer) , puis TLS(Transport Laye Security) apportent une couche supplémentaire au niveau de la couche 5 du modèle OSI.

L'association des protocoles HTTP et TLS porte le nom de HTTPS. 

Décrivons le protocole HTTPS en considérant un échange entre un client et un serveur:

- Le client envoie une demande de connexion sécurisée au serveur. 
- Le serveur envoie alors sa clé publique (asymétrique) au serveur. 
- Le client vérifie la signature en faisant appel à des autorités de certification extérieures. 
- Après vérification que le serveur n'est pas frauduleux, le client génère une clé de chiffrement symétrique , sa clé de session, et la chiffre avec la clé publique du serveur. Elle transite donc en toute sécurité. 
- Le serveur reçoit donc la clé symétrique en toute sécurité. C'est la fin de la phase de "poignée de main" entre client et serveur. 
- Client et serveur peuvent maintenant s'échanger des données cryptées en utilisant la clé de session qu'ils sont les seuls à connaître. 

![](/securisation_des_donnees/IMG/protocolehttps.jpg)
