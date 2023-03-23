# pi-monte-carlo-animation
This project aims to create a gif that represents an animation of the Monte-Carlo method to approximate pi.

approximate.py is used by draw.py, but it can be used alone to approximate pi.
Use "./approximate.py nb" with nb the number of points used for the simulation.

draw.py creates 10 .ppm files and a gif file representating the animation of the Monte-Carlo method.
Use "./draw.py size nb sign", size is the size of the image, nb the number of points and sign the significant figures used for the animation.

Warning : to use draw.py you need ImageMagick.
