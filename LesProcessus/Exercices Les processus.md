# Exercices: Les processus. 

**Exercice 1:** Bac. 

Les parties A et B peuvent être traitées indépendamment.

A. Ordonnancement des processus. 

Dans le laboratoire d'analyse médicale d'un hôpital, plusieurs processus peuvent demander l'allocation du processeur simultanément. 

Le tableau ci-dessous donne les demandes d'exécution de quatre processus et indique:

- le temps d'exécution du processus (en unité de temps);
- l'instant d'arrivée du processus sur le processeur (en unité de temps);
- le numéro de priorité du processus (classé de 1 à 10). 

Plus la priorité est grande, plus le numéro de priorité est petit. 

Ainsi, le processus P3,du tableau ci-dessous, est  plus prioritaire que le processus P1. 

L'ordonnancement est de type préemptif, ce qui signifie qu'à chaque unité de temps, le processeur choisit d'exécuter le processus ayant le plus petit numéro de priorité (un seul processus à la fois). Ceci peut provoquer la suspension d'un autre processus qui reprendra lorsqu'il deviendra la plus prioritaire dans la file d'attente. 

| Processus | Temps d'exécution | Instant d'arrivée | Numéro de priorité |
| --------- | ----------------- | ----------------- | ------------------ |
| P1        | 3                 | 0                 | 4                  |
| P2        | 4                 | 2                 | 2                  |
| P3        | 3                 | 3                 | 1                  |
| P4        | 4                 | 5                 | 3                  |

1. Reproduire le diagramme ci-dessous, sur votre copie, et indiquer dans chacune des cases le processus exécuté par le processeur entre deux unités de temps (il peut y avoir des cases vides). 

   ![](/LesProcessus/IMG/ex1img1.jpg)

2. Recopier et compléter les temps de séjour ainsi que les temps d'attente de chacun des processus (toujours en unités de temps). 

   ```
   Temps de séjour = instant de terminaison - instant d'arrivée
   Temps d'attente = temps de séjour - temps d'exécution
   ```

   

| Processus | Temps d'exécution | Instant d'arrivée | Temps de séjour | Temps d'attente |
| --------- | ----------------- | ----------------- | --------------- | --------------- |
| P1        | 3                 | 0                 | 14-0 = 14       | 14-3=11         |
| P2        | 4                 | 2                 |                 |                 |
| P3        | 3                 | 3                 |                 |                 |
| P4        | 4                 | 5                 |                 |                 |

3. A quelles conditions le temps d'attente d'un processus peut-il être nul? 

B. Processus et ressources. 

Dans ce laboratoire d'analyse médicale de l'hôpital, le laborantin en charge du traitement des différents prélèvements (sanguins, urinaires et biopsiques) utilise simultanément quatre logiciels:

- Logiciel d'analyse d'échantillons (connecté à l'analyseur). 
- Logiciel d'accès à la base de données des patients (SGBD). 
- Traitement de texte. 
- Tableur

Le tableau ci-dessous donne l'état à un instant donné des différents processus (instance des programmes) qui peuvent soit mobiliser (M) des données (D1, D2, D3, D4 et D5), soit être en attente des données (A) ou ne pas les solliciter (-). 

Une donnée ne peut être mobilisée que par un seul processus à la fois. Si un autre processus demande une donnée déjà mobilisée, il passe en attente. 

Exemple: le SGBD mobilise la donnée D4 et est en attente de la donnée D5. 

|                       | D1   | D2   | D3   | D4   | D5   |
| --------------------- | ---- | ---- | ---- | ---- | ---- |
| Analyseur échantillon | M    | -    | -    | A    | -    |
| SGBD                  | -    | -    | -    | M    | A    |
| Traitement de texte   | -    | M    | A    |      | -    |
| Tableur               | A    | -    | M    | -    | M    |

1. A partir du tableau ci-dessus, démontrer que, à cet instant, les processus s'attendent mutuellement. 
2. Comment s'appelle cette situation? 
3. On suppose que l'analyseur d'échantillon libère la ressource D1. Donner un ordre possible d'exécution des processus. 



**Exercice 2:** Bac

Cet exercice pourra utiliser des commandes de systèmes d'exploitation de type UNIX telles que `cd, ls, mkdir,rm,rmd,mv,cat`

1. Dans un système d'exploitation de type UNIX, on considère l'arborescence des fichiers suivante dans laquelle les noms de dossiers sont en italique et ceux des fichiers en gras: 

   ![](/LesProcessus/IMG/img1ex2.jpg)

On souhaite, grâce à l'utilisation du terminal de commande, explorer et modifier les répertoires et fichiers présents. 

On suppose qu'on se trouve actuellement à l'emplacement  `/home/morgane`

a. Parmi les quatre propositions suivantes, donner celle correspondant à l'affichage obtenu lors de l'utilisation de la commande `ls`

Proposition 1: lycee francais NSI info.txt image1.jpg perso

Proposition 2: lycee perso

Proposition 3: morgane

Proposition 4: bin etc home tmp

b. Ecrire la commande qui permet, à partir  de cet emplacement, d'atteindre le repértoire `lycee`

On suppose maintenant qu'on se trouve dans le répertoire `/home/morgane/lycee/NSI`

c. Ecrire la commande qui permet de créer à cet emplacement un répertoire nommé `algorithmique`. 

d. Ecrire la commande qui permet, à partir de cet emplacement, de supprimer le fichier `image1.jpg`. 

2. On rappelle qu'un processus est une instance d'application. Un processus peut être démarré par l'utilisateur, par un périphérique ou par un autre processus appelé parent. 

   La commande UNIX `ps`présente un cliché instantané des processus en cours d'exécution. 

   On a exécuté la commande `ps` (avec quelques options qu'il n'est pas nécessaire de connaître pour la réussite de cet exercice). Un extrait du résultat de la commande est présenté ci-dessous:

   ![](LesProcessus/IMG/psimage2.jpg)

   

On rappelle que:

- l'UID est l'identifiant de l'utilisateur propriétaire du processus;
- le PID est l'identifiant du processus;
- le PPID est l'identifiant du processus parent;
- C indique l'utilisation processeur;
- STIME est l'heure de démarrage du processus;
- TTY est le nom du terminal de commande auquel le processus est attaché;
- TIME est la durée d'utilisation du processeur par le processus;
- MCD est le nom de la commande utilisé pour démarrer le processus. 

a. Donner le PID du parent du processus démarré par la commande `vi`. 

b. Donner le PID d'un processus enfant du processus démarré par la commande `xfce4-terminal`. 

c. Citer le PID de deux processus qui ont le même parent. 

d. Parmi tous les processus affichés, citer le PID des deux qui ont consommé le plus de temps du processeur. 

3. On considère les trois processus P1, P2 et P3, tous soumis à l'instant 0 dans l'ordre 1,2,3. 

   | Nom du processus | Durée d'exécution en unité de temps | Ordre de soumission |
   | ---------------- | ----------------------------------- | ------------------- |
   | P1               | 3                                   | 1                   |
   | P2               | 1                                   | 2                   |
   | P3               | 4                                   | 3                   |

   a. Dans cette question, on considère que les processus sont exécutés de manière concurrente selon la politique du tourniquet : le temps est découpé en tranches nommées quantums de temps. 

   Les processsus prêts à être exécutés sont placés dans une file d'attente selon leur ordre de soumission. 

   Lorsqu'un processus est élu, il s'exécute au plus durant un quantum de temps. Si le processus n'a pas terminé son exécution à l'issue du quantum de temps, il réintègre la file des processus prêts (côté entrée). Un autre processus, désormais en tête de la file (côté sortie) des processus prêts, est alors à son tour élu pour une durée égale à un quantum de temps maximum. 

   ![](/LesProcessus/IMG/img3ex2.jpg)

​	Reproduire le tableau ci-dessous sur la copie et indiquer dans chacune des cases le processus exécuté à chaque cycle. Le quantum correspond à une unité de temps. 

![](/LesProcessus/IMG/img4ex2.jpg)

​	b. Dans cette question, on considère que les processus sont exécutés en appliquant la politique du " plus court d'abord": les processus sont exécutés complètement dans l'ordre croissant de leurs temps d'exécution, le plus court étant exécuté en premier. 

Reproduire le tableau ci-dessous sur la copie et indiquer dans chacune des cases le processus exécuté à chaque cycle. 

![](/LesProcessus/IMG/imag5ex2.jpg)

4. On considère trois ressources R1, R2, et R3 et trois processus P1, P2, et P3 dont les files d'exécution des instructions élémentaires sont indiquées ci-dessous. 

   ![](/LesProcessus/IMG/img6ex2.jpg)

​	a. Rappeler les différents états d'un processus et expliquer pourquoi il y a ici risque d'interblocage, en proposant un ordre d'exécution des instructions élémentaires le provoquant. 

b. Proposer un ordre d'exécution des instructions élémentaires sans interblocage. 

#### Exercice 3: bac

Les parties A et B peuvent être traitées indépendamment.  

##### Partie A : 

 Dans un bureau d’architectes, on dispose de certaines ressources qui ne peuvent être utilisées  simultanément par plus d’un processus, comme l’imprimante, la table traçante, le modem. 

Chaque programme, lorsqu’il s’exécute, demande l’allocation des ressources qui lui sont  nécessaires. Lorsqu’il a fini de s’exécuter, il libère ses ressources.  

| Programme 1                  demander (table traçante)  demander (modem)  exécution                               libérer (modem)                       libérer (table traçante) | Programme 2                    demander (modem)  demander (imprimante)  exécution                            libérer (imprimante)             libérer (modem) | Programme 3                   demander (imprimante)  demander (table traçante)  exécution                            libérer (table traçante)   libérer (imprimante) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |

On appelle p1, p2 et p3 les processus associés respectivement aux programmes 1, 2 et 3.  

1. Les processus s'exécutent de manière concurrente.

    Justifier qu'une situation d'interblocage peut se produire. 

2. Modifier l'ordre des instructions du programme 3 pour qu'une telle situation ne puisse pas se  produire. Aucune justification n'est attendue. 

3.  Supposons que le processus p1 demande la table traçante alors qu'elle est en cours  d'utilisation par le processus p3. Parmi les états suivants, quel sera l'état du processus p1  tant que la table traçante n'est pas disponible :  

   a) élu		 b) bloqué			 c) prêt 		d) terminé  

##### Partie B :  

Avec une ligne de commande dans un terminal sous Linux, on obtient l'affichage suivant : 

![](/LesProcessus/IMG/img1ex3.jpg)

La documentation Linux donne la signification des différents champs : 

- UID : identifiant utilisateur effectif ; 

-   PID : identifiant de processus ;

-    PPID : PID du processus parent ; 

-   C : partie entière du pourcentage d'utilisation du processeur par rapport au temps de vie  des processus ;  

-  STIME : l'heure de lancement du processus ;  

- TTY : terminal de contrôle  

- TIME : temps d'exécution  

-  CMD : nom de la commande du processus 

  

  1. Parmi les quatre commandes suivantes, laquelle a permis cet affichage ? 

      a) ls -l  		b) ps –ef  		c) cd .. 		 d) chmod 741 processus.txt  

  2. Quel est l'identifiant du processus parent à l'origine de tous les processus concernant le  navigateur Web (chromium-browser) ?

  3. Quel est l'identifiant du processus dont le temps d'exécution est le plus long ?
