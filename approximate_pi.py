#!/usr/bin/env python3

"""Implémentation de la méthode de Monte-Carlo pour approximer la valeur de pi.
Le programme sera utilisé en tant que module pour utiliser certaines fonctions par draw.py,
mais il sera aussi executable pour afficher dans la sortie standard l'approximation de pi,
en prenant en argument le nombre de points à tester."""


import sys
from random import random


def tire_point():
    """Fonction qui tire les coordonnées d'un point en renvoyant x et y dans [-1,1]."""
    coord_x = random()*2 - 1
    coord_y = random()*2 - 1
    return (coord_x,coord_y)


def est_dans_cercle(point):
    """Renvoie vrai si le point est dans le cercle unité."""
    coord_x, coord_y = point
    return (coord_x**2 + coord_y**2) <= 1


def liste_points(nb_points):
    """Crée la liste de couple, des points tirés
    et d'un booléen indiquant si le point est dans le cercle unité."""
    liste_des_points = []
    for _ in range(nb_points):
        point = tire_point()
        liste_des_points.append((point,est_dans_cercle(point)))
    return liste_des_points


def main():
    """Fonction principal qui renvoie sur la sortie standard l'approximation de pi."""
    nb_points = int(sys.argv[1])
    compteur = 0
    for k in liste_points(nb_points):
        if k[1]:
            compteur += 1
    print(compteur * 4 / nb_points)


if __name__ == "__main__":
    main()
