"""
File: fire.py
Name: Brian
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: string, the file path of the original image.
    :return: SimpleImage, highlight fire and grey-scaled image.
    """
    img = SimpleImage(filename)

    for pixel in img:
        rbg_avg = ( pixel.red + pixel.green + pixel.blue ) // 3
        is_fire = pixel.red > rbg_avg * HURDLE_FACTOR

        if is_fire :
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = rbg_avg
            pixel.green = rbg_avg
            pixel.blue = rbg_avg
    return img


def main():
    """
    TODO: Detect Where is firing and Highligt the firing area.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
