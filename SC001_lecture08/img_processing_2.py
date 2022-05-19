"""
File: img_processing_2.py
Name:
-------------------------------
This file contains 2 image processing algorithms:
(1.) left_half_darken
(2.) gray_scale
"""


from simpleimage import SimpleImage


def main():
    """
    This file contains 2 image processing algorithms:
    left_half_darken and gray_scale
    """
    # img = SimpleImage('images/stop.png')
    # img.show()

    # half_dark_img = left_half_darken('images/stop.png')
    # half_dark_img.show()

    gray_scale_img = gray_scale('images/stop.png')
    gray_scale_img.show()


def left_half_darken(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return img: SimpleImage, the image with half horizontal area darken
    """
    img = SimpleImage(filepath)
    width = img.width // 2
    height = img.height
    degree = 2

    for x in range(width):
        for y in range(height):
            pixel = img.get_pixel(x,y)
            pixel.red = pixel.red // degree
            pixel.green = pixel.green // degree
            pixel.blue = pixel.blue // degree
    return img


def gray_scale(filepath):
    """
    :param filepath: str, the file path of the original image (with respect to current directory)
    :return: SimpleImage, gray scaled image
    """
    img = SimpleImage(filepath)
    for pixel in img:
        avg = ( pixel.red + pixel.green + pixel.blue ) // 3
        pixel.red = avg
        pixel.green = avg
        pixel.blue = avg
    return img


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
