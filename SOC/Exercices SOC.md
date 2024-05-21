# Exercices: SOC

Exercice 1: 

Si dans les années 1970, on pouvait placer 2000 transistors sur une surface de 10 mm², quelle surface aurait été nécessaire pour placer deux milliards de transistors ? 



Exercice 2: Sur l'image d'un SoC, on peut lire Adreno 630, Hexagon 685, Kryo 385, X20 LTE, Spectra 280. A quels composants du SoC correspondent ces dénominations? 

Exercice 3:

## Smartphone

Trouvez pour votre smartphone les informations suivantes concernant le SoC utilisé..

| Critère                                   | Valeur |
| ----------------------------------------- | ------ |
| Nom, référence                            |        |
| Architecture (ARM, x86, autres)           |        |
| Taille (8, 16, 32, 64, 128 bits)          |        |
| Taille héliogravure transistors (en nm)   |        |
| Nombre de transistors                     |        |
| Fréquences de travail (en Hz)             |        |
| Nombre de cœurs                           |        |
| Puissance électrique consommée (en Watts) |        |
| Type de mémoire utilisée                  |        |
| Taille de la mémoire utilisée (en octets) |        |
| Puissance de calcul du GPU (en FLOPS)     |        |
| Benchmark de score GeekBench 5            |        |
| Benchmark de score AnTuTu 8               |        |

Comparez vos valeurs avec celles de vos camarades de classe.

Exercice 4: Jusqu'à une certaine finesse de gravue, il est possible de modéliser la consommation d'une puce à transistors comme étant principalement due aux charges et décharge de condensateurs, l'énergie étant dissipée dans des résistances. La consommation peut s'écrire  $P = C \times V² \times F$  avec V la tension d'alimentation et F la fréquence de la puce. La constante C est homogène avec une capacité de condensateur mais se trouve être une caractéristique du processeur qui peut être mesurée expérimentalement. 

1. a. Pour le téléphone Nokia 3310, l'expression $C \times V² $ vaut 0.19 mW/Mhz et pour le premier iphone la même expression vaut 0.4mW/mhz. En supposant une tension de fonctionnement de 2.8 V pour la puce du Nokia et une tension de 1.2V pour la puce de l'Iphone, trouver les constantes C pour les deux puces. 

   b. La puce du Nokia comporte de l'ordre de 70 000 transistors et celle de l'iphone de l'ordre de 137 500 000 transistors. Le rapport du nombre de transistors est-il cohérent avec le rapport des constantes C? Comment expliquer que C ne soit pas linéaire en le nombre de transistors? 

2. Nous savons de plus que la puce du Nokia 3310 est cadencée à 13 Mhz et celle de l'iPhone à 142 Mhz. 

   a. Calculer les consommations des puces des deux téléphones. 

   b. Le calcul précédent s'entend si le processeur est actif. En considérant que les deux puces ont juste à traiter une tâche de 10000 cycles, combien d'énergie (en Joules) est dépensée par la puce du Nokia et par celle de l'iPhone? En combien de temps, la tâche est-elle réalisée? 

   c. Par rapport à la question précédente, est ce qu'une puce plus rapide va être plus souvent inactive qu'une puce moins rapide? Que va-t-il se passer en terme d'usage du téléphone? 

3. Nous savons de plus que :

   - batterie du Nokia 3310: 3.7V et 1000 mAh, autonomie d'un mois. 
   - batterie de l'iPhone: 3.7V et 1400 mAh, autonomie d'un jour. 

   a. Que peut-on dire des puissances des batteries? 

   b. Comparer le rapport de l'autonomie des deux téléphones et celui de la consommation de leur deux puces. 

   c. Comment expliquer que les deux rapports de la question précédente sont assez différents? 

   







