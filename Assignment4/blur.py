"""
File: blur.py
Name: Brian
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image.
    :return: SimpleImage, blurred version image.
    """
    # Create a blank img file
    blank = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x,y) # original pixel

            # Copy img to a blank canva
            blank_pixel = blank.get_pixel(x, y)
            red = 0
            green = 0
            blue = 0

            # Corner Case
            is_top_left_corner = x == 0 and y == 0
            is_top_right_corner = x == ( blank.width - 1 ) and y == 0
            is_bottom_left_corner = x == 0 and y == ( blank.height - 1)
            is_bottom_right_corner = x == ( blank.width -1 ) and y == ( blank.height - 1)

            # Edge Case
            is_edge_top = y == 0
            is_edge_bottom = y == blank.height - 1
            is_edge_left = x == 0
            is_edge_right = x == blank.width - 1

            # Neighbor
            up = 0
            down = 0
            left = 0
            right = 0
            right_up = 0
            right_down = 0
            left_down = 0
            left_up = 0

            # When in edge, will casing error: ex. on the most left, x cannot be -1, so you cannot do x - 1
            if y > 0 :
                up = img.get_pixel(x, y - 1)
            if x > 0 :
                left = img.get_pixel(x - 1, y)
            if x > 0 and y > 0:
                left_up = img.get_pixel( x - 1, y - 1)

            if y < blank.height - 1:
                down = img.get_pixel(x, y + 1)
            
            if x < blank.width - 1:
                right = img.get_pixel(x + 1, y)
            
            if x < blank.width - 1 and y < blank.height - 1 :
                right_down = img.get_pixel(x + 1, y + 1)

            if x < blank.width - 1 and y > 0:
                right_up = img.get_pixel( x + 1, y - 1)

            if x > 0 and y < blank.height -1 :
                left_down = img.get_pixel(x - 1, y + 1)

            # Neighbor Count
            corner_neighbor_count = 4
            edge_neighbor_count = 6
            neighbor_count = 9


            # Copy old image and get a blur one
            if is_top_left_corner:   
                # Get pixel at the top-left corner of the image.
                red = get_avg(img_pixel.red + right.red + down.red + right_down.red, corner_neighbor_count)
                green = get_avg(img_pixel.green + right.green + down.green + right_down.green, corner_neighbor_count)
                blue = get_avg(img_pixel.blue + right.blue + down.blue + right_down.blue, corner_neighbor_count)

            elif is_top_right_corner:  
                # Get pixel at the top-right corner of the image.
                red = get_avg(img_pixel.red + left.red + down.red + left_down.red, corner_neighbor_count)
                green = get_avg(img_pixel.green +left.green + down.green + left_down.green, corner_neighbor_count)
                blue = get_avg(img_pixel.blue +left.blue + down.blue + left_down.blue, corner_neighbor_count)
                
            elif is_bottom_left_corner: 
                # Get pixel at the bottom-left corner of the image
                red = get_avg(img_pixel.red + right.red + up.red + right_up.red, corner_neighbor_count)
                green = get_avg(img_pixel.green + right.green + up.green + right_up.green, corner_neighbor_count)
                blue = get_avg(img_pixel.blue + right.blue + up.blue + right_up.blue, corner_neighbor_count)
                
            elif is_bottom_right_corner: 
                # Get pixel at the bottom-right corner of the image
                red = get_avg(img_pixel.red + left.red + up.red + left_up.red, corner_neighbor_count)
                green = get_avg(img_pixel.green + left.green + up.green + left_up.green, corner_neighbor_count)
                blue = get_avg(img_pixel.blue + left.blue + up.blue + left_up.blue, corner_neighbor_count)
 
            elif is_edge_top: 
                # Get top edge's pixels (without two corners)
                red = get_avg( img_pixel.red + left.red + left_down.red + down.red + right.red + right_down.red, edge_neighbor_count)
                green = get_avg( img_pixel.green + left.green + left_down.green + down.green + right.green + right_down.green, edge_neighbor_count)
                blue = get_avg( img_pixel.blue + left.blue + left_down.blue + down.blue + right.blue + right_down.blue, edge_neighbor_count)
            
            elif is_edge_bottom: 
                # Get bottom edge's pixels (without two corners)
                red = get_avg( img_pixel.red + left.red + left_up.red + up.red + right.red + right_up.red, edge_neighbor_count)
                green = get_avg( img_pixel.green + left.green + left_up.green + up.green + right.green + right_up.green, edge_neighbor_count)
                blue = get_avg( img_pixel.blue + left.blue + left_up.blue + up.blue + right.blue + right_up.blue, edge_neighbor_count)
                
            elif is_edge_left:
                # Get left edge's pixels (without two corners)
                red = get_avg( img_pixel.red + up.red + right_up.red + right.red + right_down.red + down.red, edge_neighbor_count)
                green = get_avg( img_pixel.green + up.green + right_up.green + right.green + right_down.green + down.green, edge_neighbor_count)
                blue = get_avg( img_pixel.blue + up.blue + right_up.blue + right.blue + right_down.blue + down.blue, edge_neighbor_count)
            
            elif is_edge_right:
                # Get right edge's pixels (without two corners)
                red = get_avg( img_pixel.red + up.red + left_up.red + left.red + left_down.red + down.red, edge_neighbor_count)
                green = get_avg( img_pixel.green + up.green + left_up.green + left.green + left_down.green + down.green, edge_neighbor_count)
                blue = get_avg( img_pixel.blue + up.blue + left_up.blue + left.blue + left_down.blue + down.blue, edge_neighbor_count)
                
            else:
                # Inner pixels.
                red = get_avg(img_pixel.red + left_up.red + up.red + right_up.red + left.red + right.red + right_down.red + down.red + right_down.red, neighbor_count)
                green = get_avg(img_pixel.green + left_up.green + up.green + right_up.green + left.green + right.green + right_down.green + down.green + right_down.green, neighbor_count)
                blue = get_avg(img_pixel.blue + left_up.blue + up.blue + right_up.blue + left.blue + right.blue + right_down.blue + down.blue + right_down.blue, neighbor_count)


            blank_pixel.red = red
            blank_pixel.green = green
            blank_pixel.blue = blue

    return blank


def main():
    """
    TODO: Blur a image and show.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def get_avg(total, number):
    """
    :param total: int, divided number
    :param number: int, divide number
    :return: int, average.
    """
    return total // number

if __name__ == '__main__':
    main()
