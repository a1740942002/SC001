"""
File: mirror_lake.py
Name: Brian
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: string, the file path of the original image.
    :return: SimpleImage, a double-height, fliped up side down original image.
    """

    img = SimpleImage(filename)
    blank = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x,y) # colored pixel
            blank_u_pixel = blank.get_pixel(x, y) # up
            blank_d_pixel = blank.get_pixel(x, blank.height - y - 1) # down
            
            # fill up, just copy original pixel
            blank_u_pixel.red = img_pixel.red
            blank_u_pixel.green = img_pixel.green
            blank_u_pixel.blue = img_pixel.blue

            # fill down, just copy original pixel
            blank_d_pixel.red = img_pixel.red
            blank_d_pixel.green = img_pixel.green
            blank_d_pixel.blue = img_pixel.blue

    return blank


def main():
    """
    TODO: flip the original image up side down and combine together.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
