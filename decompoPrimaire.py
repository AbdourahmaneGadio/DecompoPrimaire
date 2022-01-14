# coding:utf-8

from __future__ import division

def decompo(nombre):
    """
    Fonction qui donne la décomposition
    primaire d'un entier naturel

    ENTREE : Un entier
    SORTIE : Une liste
    """

    division = 2
    liste = []

    while nombre != 1:

        if nombre%division==0:
            nombre = nombre/division  
            liste.append(division)

        else:
            division +=1

    return liste                         


nombre = input("Entrez un nombre: ")

print "Décomposition primaire de", nombre, "=", decompo(nombre)
