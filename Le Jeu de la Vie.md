# Le Jeu de la Vie. 

Un **automate cellulaire** consiste en une grille régulière de « cellules » contenant chacune un « état » choisi parmi un ensemble fini et qui peut évoluer au cours du temps. L'état d'une cellule au temps *t+1* est fonction de l'état au temps *t* d'un nombre fini de cellules appelé son « voisinage ». À chaque nouvelle unité de temps, les mêmes règles sont appliquées simultanément à toutes les cellules de la grille, produisant une nouvelle « génération » de cellules dépendant entièrement de la génération précédente.

Le jeu de la vie est un automate cellulaire bidimensionnel où chaque cellule peut prendre deux valeurs (« 0 » ou « 1 », mais on parle plutôt de « vivante » ou « morte ») et où son état futur est déterminé par son état actuel et par le nombre de cellules vivantes parmi les huit qui l'entourent :

- Si la cellule est vivante et entourée par deux ou trois cellules vivantes, elle reste en vie à la génération suivante, sinon elle meurt.
- Si la cellule est morte et entourée par exactement trois cellules vivantes, elle naît à la génération suivante.

Cet automate cellulaire évolue sur une grille thorique de taille théoriquement infinie. 

L'objectif de ce mini projet est de coder une simulation de cet automate cellulaire. Nous partirons du principe que la grille générée est une grille carrée. 

Vous utiliserez le squelette de code que je vous propose et n'oublierez pas de commenter votre code. 

Toute forme d'amélioration est la bienvenue :-)

Barème:

| Tache                             | Barème                |
| --------------------------------- | --------------------- |
| fonction `generation_grille`      | 1 point               |
| fonction `places_cellules_v`      | 1 point               |
| fonction `places_cellules_aléa`   | 1 point               |
| fonction `compte_voisins_vivants` | 2 points              |
| fonction `grille_voisins`         | 1 point               |
| fonction `update_grille`          | 2 points              |
| `main`                            | 3 points              |
| propreté du code                  | 1 point               |
| commentaires                      | 1 point               |
| Améliorations                     | 1 à 2 points de bonus |





