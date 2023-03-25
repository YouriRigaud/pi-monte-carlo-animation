#!/usr/bin/env python3

"""Make the .ppm files and the gif"""


import sys
import subprocess
import approximate_pi


def init_image(image_size):
    """Fonction that creates a white image, each pixel is represented
    by a cell of a matrix with its rgb value."""
    image = [[(1, 1, 1) for _ in range(image_size)] for _ in range(image_size)]
    return image


def display_segment(coordinate, direction, image_size):
    """Display a segment where the pixel on the bottom left is at coordinate,
    with a boolean for the direction :
    True -> horizontal
    False -> vertical"""
    segment_size = image_size // 20
    line_width = segment_size // 10
    list_pixel = []
    if direction:
        for i in range(line_width):
            for j in range(segment_size):
                list_pixel.append((coordinate[0] - i, coordinate[1] + j))
    else:
        for i in range(segment_size):
            for j in range(line_width):
                list_pixel.append((coordinate[0] - i, coordinate[1] + j))
    return list_pixel


def display_point(coordonne, image_size):
    """Display a point where the pixel on the bottom left is at coordinate"""
    point_size = image_size // 100
    list_pixel = []
    for i in range(point_size):
        for j in range(point_size):
            list_pixel.append((coordonne[0] - i, coordonne[1] + image_size//50 + j))
    return list_pixel


def segment_bottom(coordinate, image_size):
    """Display the segment of the bottom"""
    return display_segment(coordinate, True, image_size)


def segment_middle(coordinate, image_size):
    """Display the segment of the middle"""
    coord_x, coord_y = coordinate
    segment_size = image_size // 20
    return display_segment((coord_x - segment_size, coord_y), True, image_size)


def segment_top(coordinate, image_size):
    """Display the segment of the top"""
    coord_x, coord_y = coordinate
    segment_size = image_size // 20
    return display_segment((coord_x - 2*segment_size, coord_y), True, image_size)


def segment_bottom_left(coordinate, image_size):
    """Display the segment of the bottom left"""
    return display_segment(coordinate, False, image_size)


def segment_top_left(coordinate, image_size):
    """Display the segment of the top left"""
    coord_x, coord_y = coordinate
    segment_size = image_size // 20
    return display_segment((coord_x - segment_size, coord_y), False, image_size)


def segment_bottom_right(coordinate, image_size):
    """Display the segment of the bottom right"""
    coord_x, coord_y = coordinate
    segment_size = image_size // 20
    return display_segment((coord_x, coord_y + segment_size), False, image_size)


def segment_top_right(coordinate, image_size):
    """Display the segment of the top right"""
    coord_x, coord_y = coordinate
    segment_size = image_size // 20
    return display_segment((coord_x - segment_size, coord_y + segment_size),
    False, image_size)


def display_digit(digit, coordinate, image_size):
    """Fonction that displays the right digit.
    Warning, digit could be a point.
    Input digit is a string.
    Return the list of the digits."""
    list_digit = []
    if digit == ".":
        return display_point(coordinate, image_size)
    if digit == "0":
        list_digit += segment_bottom(coordinate, image_size)
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
        list_digit += segment_bottom_left(coordinate, image_size)
        list_digit += segment_top_right(coordinate, image_size)
        list_digit += segment_top_left(coordinate, image_size)
    elif digit == "1":
        list_digit += segment_top_right(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
    elif digit == "2":
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_top_right(coordinate, image_size)
        list_digit += segment_middle(coordinate, image_size)
        list_digit += segment_bottom_left(coordinate, image_size)
        list_digit += segment_bottom(coordinate, image_size)
    elif digit == "3":
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_top_right(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
        list_digit += segment_middle(coordinate, image_size)
        list_digit += segment_bottom(coordinate, image_size)
    elif digit == "4":
        list_digit += segment_top_left(coordinate, image_size)
        list_digit += segment_top_right(coordinate, image_size)
        list_digit += segment_middle(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
    elif digit == "5":
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_top_left(coordinate, image_size)
        list_digit += segment_middle(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
        list_digit += segment_bottom(coordinate, image_size)
    elif digit == "6":
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_top_left(coordinate, image_size)
        list_digit += segment_bottom_left(coordinate, image_size)
        list_digit += segment_bottom(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
        list_digit += segment_middle(coordinate, image_size)
    elif digit == "7":
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_top_right(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
    elif digit == "8":
        list_digit += segment_top_left(coordinate, image_size)
        list_digit += segment_bottom_left(coordinate, image_size)
        list_digit += segment_bottom(coordinate, image_size)
        list_digit += segment_middle(coordinate, image_size)
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
        list_digit += segment_top_right(coordinate, image_size)
    elif digit == "9":
        list_digit += segment_top_left(coordinate, image_size)
        list_digit += segment_bottom(coordinate, image_size)
        list_digit += segment_middle(coordinate, image_size)
        list_digit += segment_top(coordinate, image_size)
        list_digit += segment_bottom_right(coordinate, image_size)
        list_digit += segment_top_right(coordinate, image_size)
    return list_digit


def calcul_coordinate(significant_figures, image_size):
    """According to the significant figures, return the first digit's coordinate."""
    nb_of_char = significant_figures + 2
    digit_height = image_size // 10
    coord_x = (image_size + digit_height) // 2
    digit_widht = image_size // 20
    between_digit = digit_widht // 5
    coord_y = image_size//2 - round(nb_of_char/2*(digit_widht + between_digit))
    return (coord_x, coord_y)


def display_pi(approx_pi, significant_figures, image_size):
    """Return the list of points that will be black to display pi."""
    coord_display = []
    coordinate = calcul_coordinate(significant_figures, image_size)
    for k in approx_pi:
        liste_new_coord = display_digit(k, coordinate, image_size)
        coord_display += liste_new_coord
        coordinate = (coordinate[0], coordinate[1] + round(image_size/20 + image_size/100))
    return coord_display


def color_image(list_points, image, significant_figures, num_image, counter):
    """Color the points, in blue if the point is inside, in red if not.
    Color in black the pi display."""
    image_size = len(image)
    for k in list_points:
        coord_x, coord_y = k[0]
        if k[1]:
            counter += 1
            image[
                round((coord_x+1) * (image_size-1)/2)][
                    round((coord_y+1) * (image_size-1)/2)] = (0, 0, 1)
        else:
            image[
                round((coord_x+1) * (image_size-1)/2)][
                    round((coord_y+1) * (image_size-1)/2)] = (1, 0, 0)
    approx_pi = str(round(counter * 4 / (len(list_points)*(num_image+1)), significant_figures))
    while len(approx_pi) != significant_figures + 2:
        approx_pi += "0"
    list_display = display_pi(approx_pi, significant_figures, image_size)
    list_swap_blue = []
    list_swap_red = []
    list_swap_white = []
    for k in list_display:
        if image[k[0]][k[1]] == (0, 0, 1):
            list_swap_blue += [k]
            image[k[0]][k[1]] = (0, 0, 0)
        elif image[k[0]][k[1]] == (1, 0, 0):
            list_swap_red += [k]
            image[k[0]][k[1]] = (0, 0, 0)
        else:
            list_swap_white += [k]
            image[k[0]][k[1]] = (0, 0, 0)
    list_swap = (list_swap_blue, list_swap_red, list_swap_white)
    return (approx_pi, counter, list_swap)


def discolor_pi(image, list_swap):
    """Remove black pixels."""
    for k in list_swap[0]:
        image[k[0]][k[1]] = (0, 0, 1)
    for k in list_swap[1]:
        image[k[0]][k[1]] = (1, 0, 0)
    for k in list_swap[2]:
        image[k[0]][k[1]] = (1, 1, 1)


def generate_ppm_file(list_points, image_size, significant_figures, num_image, image, counter):
    """Make the ppm files."""
    (approx_pi, counter, list_swap) = color_image(
        list_points, image, significant_figures, num_image, counter
    )
    image_name = f"img{num_image}_{approx_pi[0]}-"
    for i in range(2, len(approx_pi)):
        image_name += f"{approx_pi[i]}"
    image_name += ".ppm"
    ppm_file = open(image_name, "w", encoding = "UTF_8")
    print("P3", file = ppm_file)
    print(f"{image_size} {image_size}", file = ppm_file)
    print("1", file = ppm_file)
    for i in range(image_size):
        for j in range(image_size):
            print(
                f"{image[i][j][0]} {image[i][j][1]} {image[i][j][2]} ", end = "", file = ppm_file
            )
    ppm_file.close()
    discolor_pi(image, list_swap)
    return counter


def check_parameters(parameters):
    """Fonction that check if the input parameters are good."""
    if (
        len(parameters) != 3 or int(parameters[0]) < 100 or
        int(parameters[1]) < 100 or int(parameters[2]) not in range(1,6)
    ):
        raise ValueError


def convert_ppm_to_gif():
    """Make the gif file."""
    subprocess.run(["convert", "-delay", "100", "*.ppm", "pi.gif"], check = True)


def main():
    """Main fonction."""
    parameters = sys.argv
    parameters.pop(0)
    check_parameters(parameters)
    image_size = int(parameters[0])
    nb_points = int(parameters[1])
    significant_figures = int(parameters[2])
    image = init_image(image_size)
    counter = 0
    for num_image in range(10):
        list_points = approximate_pi.list_of_points(nb_points//10)
        counter = generate_ppm_file(
            list_points, image_size, significant_figures, num_image, image, counter
        )
    convert_ppm_to_gif()


if __name__ == "__main__":
    main()
