"""
File: curb_repair.py
Name:
-------------------------------
This program shows how to detect red pixels
of curb and change them into gray scale, making
the curb area be considered as an available parking space!
"""


from simpleimage import SimpleImage

THRESHOLD = 1.15

def main():
    img = SimpleImage("images/curb.png")
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3

        # 因為對電腦來說，葉子雖然看起來是綠的，但他其實裡面紅色也高於平均
        if pixel.red > avg * THRESHOLD:
            # curb
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    img.show()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
