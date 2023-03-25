#!/usr/bin/env python3

"""Dev of the Monte-Carlo method to approximate pi.
This file is a module used for draw.py.
It can also take an input integer value to return the approximation of pi."""


import sys
from random import random


def create_point():
    """Fonction that creates a point with the coordinates x and y in [-1,1]."""
    coord_x = random()*2 - 1
    coord_y = random()*2 - 1
    return (coord_x,coord_y)


def in_the_circle(point):
    """Return True if the point is in the unity circle."""
    coord_x, coord_y = point
    return (coord_x**2 + coord_y**2) <= 1


def list_of_points(nb_points):
    """Make the list of the points with a boolean indicating if the point is in the circle."""
    list_points = []
    for _ in range(nb_points):
        point = create_point()
        list_points.append((point,in_the_circle(point)))
    return list_points


def main():
    """Main fonction that return the approximation of pi."""
    nb_points = int(sys.argv[1])
    counter = 0
    for k in list_of_points(nb_points):
        if k[1]:
            counter += 1
    print(counter * 4 / nb_points)


if __name__ == "__main__":
    main()
