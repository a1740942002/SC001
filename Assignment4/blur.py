"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    # Todo: create a new blank img that is as big as the original one

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            
            pass
            
            # Todo: get pixel of new_img at x,y

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            # if x == 0 and y ==0:   
                # Get pixel at the top-left corner of the image.
           

            # elif ...:  
                # Get pixel at the top-right corner of the image.
                

            # elif ...: 
                # Get pixel at the bottom-left corner of the image
                

            # elif ...: 
                # Get pixel at the bottom-right corner of the image
                
 
            # elif ...: 
                # Get top edge's pixels (without two corners)
            

            # elif ...: 
                # Get bottom edge's pixels (without two corners)
                

            # elif ...:
                # Get left edge's pixels (without two corners)
            

            # elif ...:
                # Get right edge's pixels (without two corners)
                

            #else:
                # Inner pixels.

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
