#!/usr/bin/env python3

"""Programme qui créé les images demandées"""


import sys
import subprocess
import approximate_pi


def init_image(taille_image):
    """Fonction qui créée une image vide, çad que du blanc.
    On représente l'image par une matrice où chaque coefficient
    est une couleur rgb."""
    image = [[(1, 1, 1) for _ in range(taille_image)] for _ in range(taille_image)]
    return image


def affiche_segment(coordonnee, direction, taille_image):
    """Affiche un segment dont le pixel en bas à gauche se trouve au point coordonnee
    et dont la direction est un booléen.
    True -> horizontal
    False -> vertical"""
    longueur_segment = taille_image // 20
    largeur_trait = longueur_segment // 10
    liste_pixel = []
    if direction:
        for i in range(largeur_trait):
            for j in range(longueur_segment):
                liste_pixel.append((coordonnee[0] - i, coordonnee[1] + j))
    else:
        for i in range(longueur_segment):
            for j in range(largeur_trait):
                liste_pixel.append((coordonnee[0] - i, coordonnee[1] + j))
    return liste_pixel


def affiche_point(coordonne, taille_image):
    """Affiche un point dont le pixel en bas à gauche se trouve au point coordonnee."""
    taille_point = taille_image // 100
    liste_pixel = []
    for i in range(taille_point):
        for j in range(taille_point):
            liste_pixel.append((coordonne[0] - i, coordonne[1] + taille_image//50 + j))
    return liste_pixel


def segment_bas(coordonnee, taille_image):
    """Affiche le segment du bas"""
    return affiche_segment(coordonnee, True, taille_image)


def segment_mileu(coordonnee, taille_image):
    """Affiche le segment du milieu"""
    coord_x, coord_y = coordonnee
    longueur_segment = taille_image // 20
    return affiche_segment((coord_x - longueur_segment, coord_y), True, taille_image)


def segment_haut(coordonnee, taille_image):
    """Affiche le segment du haut"""
    coord_x, coord_y = coordonnee
    longueur_segment = taille_image // 20
    return affiche_segment((coord_x - 2*longueur_segment, coord_y), True, taille_image)


def segment_bas_gauche(coordonnee, taille_image):
    """Affiche le segment du bas gauche"""
    return affiche_segment(coordonnee, False, taille_image)


def segment_haut_gauche(coordonnee, taille_image):
    """Affiche le segment du haut gauche"""
    coord_x, coord_y = coordonnee
    longueur_segment = taille_image // 20
    return affiche_segment((coord_x - longueur_segment, coord_y), False, taille_image)


def segment_bas_droite(coordonnee, taille_image):
    """Affiche le segment du bas droite"""
    coord_x, coord_y = coordonnee
    longueur_segment = taille_image // 20
    return affiche_segment((coord_x, coord_y + longueur_segment), False, taille_image)


def segment_haut_droite(coordonnee, taille_image):
    """Affiche le segment du haut droite"""
    coord_x, coord_y = coordonnee
    longueur_segment = taille_image // 20
    return affiche_segment((coord_x - longueur_segment, coord_y + longueur_segment),
    False, taille_image)


def affiche_chiffre(chiffre, coordonnee, taille_image):
    """Fonction qui affiche le chiffre correspondant.
    Attention, l'entrée chiffre peut aussi être un point.
    L'entrée chiffre est un string.
    Coordonnee est un point de l'image.
    Renvoie la liste des nouveau points"""
    liste_chiffre = []
    if chiffre == ".":
        return affiche_point(coordonnee, taille_image)
    if chiffre == "0":
        liste_chiffre += segment_bas(coordonnee, taille_image)
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
        liste_chiffre += segment_bas_gauche(coordonnee, taille_image)
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
        liste_chiffre += segment_haut_gauche(coordonnee, taille_image)
    elif chiffre == "1":
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
    elif chiffre == "2":
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
        liste_chiffre += segment_mileu(coordonnee, taille_image)
        liste_chiffre += segment_bas_gauche(coordonnee, taille_image)
        liste_chiffre += segment_bas(coordonnee, taille_image)
    elif chiffre == "3":
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
        liste_chiffre += segment_mileu(coordonnee, taille_image)
        liste_chiffre += segment_bas(coordonnee, taille_image)
    elif chiffre == "4":
        liste_chiffre += segment_haut_gauche(coordonnee, taille_image)
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
        liste_chiffre += segment_mileu(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
    elif chiffre == "5":
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_haut_gauche(coordonnee, taille_image)
        liste_chiffre += segment_mileu(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
        liste_chiffre += segment_bas(coordonnee, taille_image)
    elif chiffre == "6":
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_haut_gauche(coordonnee, taille_image)
        liste_chiffre += segment_bas_gauche(coordonnee, taille_image)
        liste_chiffre += segment_bas(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
        liste_chiffre += segment_mileu(coordonnee, taille_image)
    elif chiffre == "7":
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
    elif chiffre == "8":
        liste_chiffre += segment_haut_gauche(coordonnee, taille_image)
        liste_chiffre += segment_bas_gauche(coordonnee, taille_image)
        liste_chiffre += segment_bas(coordonnee, taille_image)
        liste_chiffre += segment_mileu(coordonnee, taille_image)
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
    elif chiffre == "9":
        liste_chiffre += segment_haut_gauche(coordonnee, taille_image)
        liste_chiffre += segment_bas(coordonnee, taille_image)
        liste_chiffre += segment_mileu(coordonnee, taille_image)
        liste_chiffre += segment_haut(coordonnee, taille_image)
        liste_chiffre += segment_bas_droite(coordonnee, taille_image)
        liste_chiffre += segment_haut_droite(coordonnee, taille_image)
    return liste_chiffre


def calcul_coordonnee(chiffre_significatif, taille_image):
    """En fonction du chiffre significatif,
    la fonction renvoie la coordonnee du premier chiffre à afficher."""
    nombre_caracteres = chiffre_significatif + 2
    hauteur_chiffre = taille_image // 10
    coord_x = (taille_image + hauteur_chiffre) // 2
    largeur_chiffre = taille_image // 20
    entre_chiffre = largeur_chiffre // 5
    coord_y = taille_image//2 - round(nombre_caracteres/2*(largeur_chiffre + entre_chiffre))
    return (coord_x, coord_y)


def afficheur_pi(approx_pi, chiffre_significatif, taille_image):
    """Fonction qui renvoie une liste pour afficher le nombre approx_pi sur l'image.
    Pour cela utilisons un afficheur 7 segments que l'on modélise par
    une liste des coordonées des points à mettre ne noir."""
    coord_afficheur = []
    coordonnee = calcul_coordonnee(chiffre_significatif, taille_image)
    for k in approx_pi:
        liste_new_coord = affiche_chiffre(k, coordonnee, taille_image)
        coord_afficheur += liste_new_coord
        coordonnee = (coordonnee[0], coordonnee[1] + round(taille_image/20 + taille_image/100))
    return coord_afficheur


def color_image(liste_points, image, chiffre_significatif, num_image, compteur):
    """Fonction qui colorie l'image quand un point est tiré,
    le colorie en bleu si le point est dans le cercle, en rouge sinon.
    Colorie en noir le compteur pour afficher l'approximation de pi.
    Renvoie aussi l'approximation de pi associée à l'image et le compteur."""
    taille_image = len(image)
    for k in liste_points:
        coord_x, coord_y = k[0]
        if k[1]:
            compteur += 1
            image[
                round((coord_x+1) * (taille_image-1)/2)][
                    round((coord_y+1) * (taille_image-1)/2)] = (0, 0, 1)
        else:
            image[
                round((coord_x+1) * (taille_image-1)/2)][
                    round((coord_y+1) * (taille_image-1)/2)] = (1, 0, 0)
    approx_pi = str(round(compteur * 4 / (len(liste_points)*(num_image+1)), chiffre_significatif))
    while len(approx_pi) != chiffre_significatif + 2:
        approx_pi += "0"
    liste_afficheur = afficheur_pi(approx_pi, chiffre_significatif, taille_image)
    liste_echange_bleu = []
    liste_echange_rouge = []
    liste_echange_blanc = []
    for k in liste_afficheur:
        if image[k[0]][k[1]] == (0, 0, 1):
            liste_echange_bleu += [k]
            image[k[0]][k[1]] = (0, 0, 0)
        elif image[k[0]][k[1]] == (1, 0, 0):
            liste_echange_rouge += [k]
            image[k[0]][k[1]] = (0, 0, 0)
        else:
            liste_echange_blanc += [k]
            image[k[0]][k[1]] = (0, 0, 0)
    liste_echange = (liste_echange_bleu, liste_echange_rouge, liste_echange_blanc)
    return (approx_pi, compteur, liste_echange)


def decolorie_compteur(image, liste_echange):
    """Enlève les pixel noir du compteur et remet ceux d'avant."""
    for k in liste_echange[0]:
        image[k[0]][k[1]] = (0, 0, 1)
    for k in liste_echange[1]:
        image[k[0]][k[1]] = (1, 0, 0)
    for k in liste_echange[2]:
        image[k[0]][k[1]] = (1, 1, 1)


def generate_ppm_file(liste_points, taille_image, chiffre_significatif, num_image, image, compteur):
    """Génère une image au format ppm,
    les points à l'interieur du cercle sont en bleus, ceux à l'exterieur en rouge,
    les points non coloriés sont blancs et ceux de l'afficheur de pi sont en noirs.
    La fonction prend en argument la liste des couples (points_tirés, booléen),
    le booléen étant vrai, si le point est dans le cercle unité.
    Renvoie le compteur."""
    (approx_pi, compteur, liste_echange) = color_image(
        liste_points, image, chiffre_significatif, num_image, compteur
    )
    nom_image = f"img{num_image}_{approx_pi[0]}-"
    for i in range(2, len(approx_pi)):
        nom_image += f"{approx_pi[i]}"
    nom_image += ".ppm"
    fichier_ppm = open(nom_image, "w", encoding = "UTF_8")
    print("P3", file = fichier_ppm)
    print(f"{taille_image} {taille_image}", file = fichier_ppm)
    print("1", file = fichier_ppm)
    for i in range(taille_image):
        for j in range(taille_image):
            print(
                f"{image[i][j][0]} {image[i][j][1]} {image[i][j][2]} ", end = "", file = fichier_ppm
            )
    fichier_ppm.close()
    decolorie_compteur(image, liste_echange)
    return compteur


def verifie_parametres(parametres):
    """Fonction qui vérifie que les paramètres d'entrés sont valides.
    Renvoie une exception si ce n'est pas le cas."""
    if (
        len(parametres) != 3 or int(parametres[0]) < 100 or
        int(parametres[1]) < 100 or int(parametres[2]) not in range(1,6)
    ):
        raise ValueError


def convert_ppm_to_gif():
    """Renvoie dans le terminal l'action à effectuer pour convertir
    les images ppm en gif."""
    subprocess.run(["convert", "-delay", "100", "*.ppm", "pi.gif"], check = True)


def main():
    """Fonction principal du programme, prends les paramètres d'entrés du programme
    et renvoie l'image gif voulue."""
    parametres = sys.argv
    parametres.pop(0)
    verifie_parametres(parametres)
    taille_image = int(parametres[0])
    nb_points = int(parametres[1])
    chiffre_significatif = int(parametres[2])
    image = init_image(taille_image)
    compteur = 0
    for num_image in range(10):
        liste_points = approximate_pi.liste_points(nb_points//10)
        compteur = generate_ppm_file(
            liste_points, taille_image, chiffre_significatif, num_image, image, compteur
        )
    convert_ppm_to_gif()


if __name__ == "__main__":
    main()
