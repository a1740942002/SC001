"""
File: best_photoshop_award.py
Name: Brian
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


# Controls the threshold of detecting green screen pixel
SKY_THRESHOLD = 170

def combine(bg, avatar):
    """
    : param1 bg: SimpleImage, the background image
    : param2 avatar: SimpleImage, green screen figure image
    : return avatar: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            avatar_pixel = avatar.get_pixel(x, y)
            avg = (avatar_pixel.red + avatar_pixel.blue + avatar_pixel.green) // 3
            total = avatar_pixel.red + avatar_pixel.blue + avatar_pixel.green
            bg_pixel = bg.get_pixel(x, y)

            is_sky = avatar_pixel.green > SKY_THRESHOLD and avatar_pixel.red > SKY_THRESHOLD and avatar_pixel.blue > SKY_THRESHOLD

            if is_sky:
                # Replace sky with new background
                avatar_pixel.red = bg_pixel.red
                avatar_pixel.blue = bg_pixel.blue
                avatar_pixel.green = bg_pixel.green

    return avatar


def main():
    """
    創作理念：把天空變成夜晚的星空
    """
    avatar = SimpleImage('image_contest/avatar.jpeg')
    bg = SimpleImage('image_contest/bg.jpeg')
    bg.make_as_big_as(avatar)
    combined_img = combine(bg, avatar)
    combined_img.show()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
