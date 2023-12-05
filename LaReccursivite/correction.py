def syracuse(u,n=0):
    if u == 1:
        print(u)
        return n
    else:
        if u%2==0:
            print(u)
            return syracuse(u//2,n+1)
        else:
            print(u)
            return syracuse(3*u+1,n+1)

def nb_diviseurs(j,n):
    if j==1:
        return 1
    else:
        if n%j==0:
            return nb_diviseurs(j-1,n)+1
        else:
            return nb_diviseurs(j-1,n)
def somme_div(j,n):
    if j == 1:
        return j
    else:
        if n%j == 0:
            return somme_div(j-1,n)+j
        else:
            return somme_div(j-1,n)

def est_parfait(n):
    if somme_div(n,n)==2*n:
        return True
    else:
        return False

def moyenne_ite(t):
    res = 0
    for i in range(len(t)):
        res += t[i]
    return res/len(t)

def moyenne_rec(t):
    if len(t) == 1:
        return t[0]
    else:
        return (t[0]+moyenne_rec(t[1:len(t)])*(len(t)-1))/(len(t))
    
def nombre_de_chiffres(n):
    if n<10:
        return 1
    else:
        return nombre_de_chiffres(n//10)+1
    
def nombre_de_bits(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n %2 == 0:
            return nombre_de_bits(n//2)
        else:
            return nombre_de_bits(n//2) +1
        
def pgcd(a,b):
    if a<b:
        c=b
        b=a
        a=c
    if b == 0:
        return a
    else:
        return pgcd(b,a%b)
    
from turtle import *
from math import sqrt
from random import *

def carres(longueur, nombre):
    pensize(5)
    couleur=['red','blue','purple','green','pink','brown']
    
    macouleur = choice(couleur)
    color(macouleur)
    forward(longueur)
    right(90)
    forward(longueur)
    right(90)
    forward(longueur)
    right(90)
    forward(longueur/2)
    if nombre > 1:
        right(45)
        carres(longueur / sqrt(2), nombre - 1)
    color(macouleur)
    forward(longueur/2)
    right(45)



