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
    img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
