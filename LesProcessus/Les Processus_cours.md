# Les Processus. 

Considérons une activité simple sur un ordinateur: Klara programme en python son jeu vidéo préféré. 

Elle a donc ouvert un IDle. Son navigateur web est aussi ouvert avec divers onglets. Elle utilise, de plus, un logiciel de dessin afin de concevoir l'environnement graphique de son jeu. 

De plus, elle a mis un casque et écoute de la musique grâce au lecteur de musique de son ordinateur. 

Tous ces programmes s'exécutent "en même temps". Pourtant, l'ordinateur de Klara ne dispose que d'un nombre limité de processeurs, et comme nous le savons, un programme n'est qu'une suite d'instruction en langage binaire, ces dernières étant exécutées une à une par le processeur. 

Comment le processeur peut-il exécuter "en même temps" toutes ces tâches? 

## I. Quelques rappels. 



#### a. L'architecture Von Neumann. 

​	L'architecture des ordinateurs actuels repose sur le modèle de Von Neumann. 

​	L'architecture de von Neumann décompose l’ordinateur en 4 parties distinctes :

- l’unité arithmétique et logique (UAL ou ALU en anglais) ou unité de traitement : son rôle est d’effectuer les opérations de base ;
- ​	l’unité de contrôle, chargée du « séquençage » des opérations : elle joue un rôle de coordonnateur ;
- ​	la mémoire qui contient à la fois les données et le programme qui indiquera à l’unité de contrôle quels sont les calculs à faire sur ces données. La mémoire se divise entre mémoire volatile (programmes et données en cours de fonctionnement) et mémoire permanente (programmes et données de base de la machine) ;
- ​	les dispositifs d’entrée-sortie, qui permettent de communiquer avec le monde extérieur.



​	L'idée essentielle de Von Neumann est que la mémoire doit servir non seulement à stocker des données  mais aussi les programmes. 

​	Une machine doit s'organiser avec une mémoire, une unité arithmétique et logique (dite 	UAL), une unité de contrôle, des systèmes d’entrées sorties et une horloge pour synchroniser 	le fonctionnement. Les différents éléments échangent des informations à l'aide de bus. 

![](/LesProcessus/IMG/vonneumann.jpg)

L'UAL et l'unité de contrôle sont regroupés dans le processeur qui communiquent avec la 	mémoire par un bus. Ces composants constituent l'unité centrale, située sur la carte mère d'un ordinateur.  Le tout est rythmé par une horloge interne qui détermine la fréquence du processeur. 

#### b. Système d'exploitation. 

Un système d'exploitation, OS pour Opérating System, est un programme exécuté au démarrage d'une machine. Il permet de gérer les fichiers, les répertoires, les processus, les périphériques en proposant des outils pour cela.  Ces outils sont des gestionnaires de fichiers, d'applications, de périphériques. Il fait le lien entre les applications (la partie software) et le matériel (la partie Hardware).  

Les OS les plus répandus sont Windows, MacOS, (GNU/)Linux, Android et iOS.  

Le système d'exploitation va gérer :

-  les processus,

- ​	la mémoire,
- ​	Les fichiers
- ​	les entrées/sorties
- ​	les communications-réseaux.
- ​	Les interfaces graphiques, interaction avec les humains.  



Pour cela, parmi les différents composants logiciels que l'on retrouve dans les systèmes d'exploitation modernes, on retrouve :

- l'ordonnanceur qui décide quel programme s'exécute à un instant donné sur le processeur.

- ​	Le gestionnaire de mémoires, qui répartit la mémoire vive entre les différents programmes en cours d’exécution ;
- ​	les différents systèmes de fichiers, qui définissent la manière de stocker les fichiers sur les supports physiques (disques, clés USB, …) ;
- ​	la pile réseau qui implémente entre autres des protocoles tels que TCP/IP.  
- ​	Les pilotes de périphériques (mieux connu sous le nom de drivers en anglais) dont le but est de gérer les périphériques matériels (carte graphique, disques durs, clavier...).  



## II. Les processus. 

#### a. Définition. 

Il ne faut pas confondre les deux notions suivantes:

**Un programme (exécutable)** est un fichier contenant des instructions machines. 

**Un processus** est le phénomène dynamique qui correspond à l'exécution d'un programme particulier. Il entraîne des échanges de données. 

Si on exécute deux fois le même programme, on crée alors deux processus différents. 

Pour s'exécuter, chaque processus a besoin d'utiliser des ressources: une certaine quantité de mémoire, des entrées comme le clavier ou la souris ou des sorties comme l'écran ou l'imprimante. 

Un processeur ne pouvant exécuter qu'une seule instruction à la fois, il doit basculer constamment d'un processus à l'autre. 

L'Os gère les ressources et l'exécution des processus. On dit que le système d'exploitation gère l'ordonnancement des processus. 

#### b. Etats. 

Il existe différents états dans lequel un processus peut être:

- **initialisation**: c est l'état dans lequel se trouve le processus lors de sa création. Cela peut être au lancement d'une application, par exemple. 
- **prêt**: le processus peut être le prochain à s'exécuter. Il est dans la "file d'attente" des processus. 
- **Elu**: Le processus est choisi par l'OS pour être exécuté. Il peut alors demander d'accéder à une ressource. On dit que le processus est actif. 
- **Bloqué**: le processus attend que les ressources dont il a besoins soient disponibles et le ordonnanceur l'élise, c'est à dire, le repasse à l'état prêt. 
- **Terminé**: le processus a achevé son travail ou a été forcé de s'arrêter. 

L'OS choisit un processus parmi les processus prêts:

- si les ressources dont il a question sont disponibles, un temps lui est attribué pendant lequel il est exécuté, puis il est mis à l'état bloqué. 
- sinon, il passe à l'état bloqué et l'OS élit un autre processus. 



![](/LesProcessus/IMG/image1processus.jpg)

#### c. PID et PPID. 

Chaque processus possède un code unique appelé **identifiant de processus (PID)**. Ce PID est un nombre entier. Le système d'exploitation utilise un compteur qui est incrémenté de 1 à chaque création de processus, il utilise ce compteur pour attribuer les PID aux processus.

De plus, chaque processus (mis à part le premier) a lui-même été lancé par un processus parent, identifié par un **identifiant de processus parent (PPID)**. 

Sous Linux, le premier processus démarré s'appelle `init `(ou `systemd`). Il a le PID 1 et le PPID 0. 

### d. Les threads. 

Un processus est constitué d'une suite d'instructions traitées par le processeur. Ces instructions sont regroupées en petites séquences. Une séquence s'appelle un **thread**. On parle aussi de tâche ou de fil d'exécution. 

Un thread est donc une partie du processus qui s'exécute indépendamment des autres parties et possède son propre contexte. 

Chaque processus possède sa propre mémoire virtuelle, les threads d'un même processus se partagent sa mémoire virtuelle. Tous les threads possèdent leur propre pile d'exécution. 



## III. Ordonnancement. 

### a. L'ordonnanceur. 

Dans les systèmes d'exploitation, l’**ordonnanceur** est le composant du noyau du système d'exploitation choisissant l'ordre d'exécution des processus sur les processeurs d'un ordinateur. 

Un processeur ne peut effectuer qu'une tâche à la fois. Avec plusieurs processeurs ou cœurs, il est possible d'effectuer plusieurs tâche simultanément, mais il y aura en général plus de processus que de processeurs ou cœurs. Il faut donc choisir à chaque instant quel processus va utiliser tel processeur. 

L'ordonnanceur doit donc permettre à tous les processeurs de s'exécuter à un moment ou un autre et d'utiliser au mieux le processeur pour l'utilisateur. 

L'ordonnanceur permet:

- de minimiser le temps de traitement du processus d'un utilisateur,
- de garantir l'équité entre les différents utilisateurs,
- d'optimiser l'utilisation de la ressource,
- d'éviter les blocages. 

### b. Algorithmes. 

Le système dispose d'une table des processus, d'une file d'attente des processus prêts et de différentes files d'attente des processus bloqués.

![](/LesProcessus/IMG/trois_processus.jpg)

Plusieurs algorithmes d'ordonnancement sont possibles. Parmi les plus répandus, nous pouvons citer:

#### 	1. Premier arrivé, premier servi.

​	Chaque processus créé et placé dans une file et les processus s'exécutent les uns après les autres. C'est celui qu'on utilise, par exemple, pour gérer la file d'impressions d'une imprimante.  

​	![](/LesProcessus/IMG/file_processus.jpg)

#### 2. Le tourniquet. 

​	Pour donner l'illusion que les différents programmes tournent en même temps, un temps très court est 	alloué à tour de rôle aux processus. C'est un algorithme simple et facile à mettre en œuvre. La rapidité 		avec laquelle on passe d'un processus au suivant donne l'illusion d'une exécution simultanée.

![](/LesProcessus/IMG/tourniquet.jpg)

#### 	3. Le plus court d'abord. 



​	Le processus qui se terminera le plus vite passera en priorité. c'est un algorithme très efficace pour 		satisfaire l'utilisateur, mais il est compliquer de déterminer si un processus sera rapidement terminé ou pas avant qu'il ne s'exécute.

![](/LesProcessus/IMG/plus_court.jpg)





## IV. Interblocage. 



Comme nous l'avons vu, les processus d'un système peuvent exécuter de manière concurrente: leurs exécutions sont entrelacées. De plus, l'ordre dans lequel ils s'exécutent est hors de leur contrôle, car il est décidé par l'ordonnanceur. Si cette façon de fonctionner à de nombreux avantages comme celui de permettre l'exécution de nombreux programmes de manière simultanée, elle peut aussi conduire à des situations d'interblocage. 

Prenons un exemple: soit un système possédant une instance unique de chacun des deux types de ressources R1 et R2. Un processus P1 détient l'instance de la ressource R1 et un autre processus P2 détient l'instance de la ressource R2. Pour poursuivre son exécution, P1 a besoin de la ressource R2 et inversement P2 a besoin de la ressource R1.Une telle situation est une situation d'interblocage. 

![](/LesProcessus/IMG/interblocage.jpg)

Plus généralement, on dit qu'un ensemble de processus est dans une situation d'interblocage si chaque processus attend un événement qui ne peut être produit que par un autre processus de l'ensemble. 

Les interblocages sont évidemment indésirables. Dans un interblocage, les processus ne terminent jamais leur exécution et les ressources du système sont immobilisés, empêchant ainsi d’autres travaux de commencer.
 Une situation d’interblocage peut survenir si les quatre conditions suivantes se produisent simultanément (Habermann) :

1. Accès exclusif : Les ressources ne peuvent être exploitées que par un seul processus à la fois.
2. Attente et occupation : Les processus qui demandent de nouvelles ressources gardent celles qu'ils ont déjà acquises et attendent la satisfaction de leur demande
3. Pas de réquisition : Les ressources déjà allouées ne peuvent pas être réquisitionnées.
4. Attente circulaire : Les processus en attente des ressources déjà allouées forment une chaîne circulaire d'attente.



