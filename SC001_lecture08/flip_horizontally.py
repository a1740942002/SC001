"""
File: flip_horizontally.py
Name: 
------------------------------------
This program shows how to create an empty SimpleImage
as well as making a mirrored image of poppy.png by
replacing pixels on blank new canvas by ones on poppy.png
"""


from simpleimage import SimpleImage


def main():
    img = SimpleImage("images/poppy.png")
    b_img = SimpleImage.blank(img.width * 2, img.height)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x,y) # 彩色
            b_img_l_pixel = b_img.get_pixel(x,y) # 空白
            b_img_r_pixel = b_img.get_pixel(b_img.width -1 -x, y) # 空白

            b_img_l_pixel.red = img_pixel.red
            b_img_l_pixel.green = img_pixel.green
            b_img_l_pixel.blue = img_pixel.blue

            b_img_r_pixel.red = img_pixel.red
            b_img_r_pixel.green = img_pixel.green
            b_img_r_pixel.blue = img_pixel.blue
            


    img.show()
    b_img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
