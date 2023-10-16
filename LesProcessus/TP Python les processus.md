# TP Python: les processus. 

## A. Processus concurrents. 

1. Voici un programme python. 

   ```python
   
   from os import getpid
   
   pid = str(getpid())
   with open("test.txt", "w") as fichier:
       for i in range(1000):
           fichier.write(pid +":"+str(i)+"\n")
           fichier.flush()
   ```

   

​		a. A quoi sert la fonction `getpid`? 

​		b. A quoi sert la fonction `flush`? 

​		c. Que devrait contenir le fichier `test.txt`? 

​		d. Implémenter le programme, enregistrer le sous le nom `pid.py` et vérifier que ce que vous aviez prévu à la question c est correct. 

​		e. Modifier le programme afin d'insérer le ppid du processus. 

2. Depuis `Tilix`, lancer trois fois le programme en une commande, en plaçant l'exécution de ces programmes en arrière plan (c'est le rôle de l'esperluette). 

   ```
   python3 pid.py & python3 pid.py & python3 pid.py &
   ```

   Relever les PID des processus. 

3. Examiner le contenu du fichier `test.txt`et recommencer plusieurs fois l'opération. Quelles remarques peut-on faire? Comment pourriez vous expliquer les résultats obtenus? 



## B. Interblocage. 

1. a. Qu'est ce qu'un thread? Que font les deux dernières lignes du programme ci-dessous? 

```python
import threading

def hello(n):
    for i in range(5):
        print("Je suis le thread",n, " et ma valeur est",i)
    print("Fin du Thread ",n)

for n in range(4):
    t = threading.Thread(target=hello, args=[n])
    t.start()
```

​	  b. Implémenter et exécuter ce programme. Que se passe-t-il? 

2. a. Que signifie l'instruction `global COMPTEUR` dans le programme ci-dessous? 

```python
import threading
COMPTEUR = 0

def incr():
    global COMPTEUR
    for c in range(100000):
        v = COMPTEUR
        COMPTEUR = v + 1

th = []
for n in range(4):
    t = threading.Thread(target=incr, args=[])
    t.start()
    th.append(t)

for t in th:
    t.join()
print("Valeur finale", compteur)
```

​	b. Expliquer le rôle de l'instruction `t.join()`. 

​	c. Quel affichage peut-on s'attendre à avoir après avoir lancé ce programme? 

​	d. Exécuter au moins dix fois ce programme? Que se passe-t-il? 

​	e. Expliquer la valeur finale obtenue? 



## C. Verrou. 

Pour corriger le problème rencontré précédemment, il nous faut donc garantir l'accès exclusif à la variable compteur entre sa lecture et son écriture. On peut, pour cela utiliser un verrou. 

Un verrou est un objet que l'on peut essayer d'acquérir. 

Si on est le premier à faire cette demande, on acquiert le verrou. On peut le rendre à tout moment. 

Si, en revanche, quelqu'un d'autre tient le verrou, alors on est bloqué jusqu'à ce qu'il soit libéré. 

Reprendre le code précédent et en utilisant un verrou afin de corriger le problème précèdent. 

Vous utiliserez la classe 'Lock()' et les méthodes qui vont avec. 

## D. Interblocage. 

L'utilisation de plusieurs verrous rend les interblocages possibles. 

```python
import threading

verrou1 = threading.Lock()
verrou2 = threading.Lock()

def f1():
    verrou1.acquire()
    print("Section critique 1.1")
    verrou2.acquire()
    print("Section critique 1.2")
    verrou2.release()
    verrou1.release()

def f2():
    verrou2.acquire()
    print("Section critique 2.1")
    verrou1.acquire()
    print("Section critique 2.2")
    verrou1.release()
    verrou2.release()

t1 = threading.Thread(target=f1, args=[])
t2 = threading.Thread(target=f2, args=[])
t1.start()
t2.start()
```

1. Quelle situation le programme ci-dessus essaie-t-il d'illustrer? Justifier la réponse. 
2. Exécuter le programme plusieurs fois. La situation prévue à la question précédente intervient-elle vraiment ? Pourquoi? 

