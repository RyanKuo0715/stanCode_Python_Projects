"""
File: blur.py
Name: Ryan Kuo
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, image intended to be blurred
    :return: blurred image
    """
    blur_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel_r = pixel_g = pixel_b = count = 0
            for i in range(max(0, x-1), min(img.width, x+2)):
                for j in range(max(0, y-1), min(img.height, y+2)):
                    pixel_r += img.get_pixel(i, j).red
                    pixel_g += img.get_pixel(i, j).green
                    pixel_b += img.get_pixel(i, j).blue
                    count += 1
            blur_img.get_pixel(x, y).red = pixel_r // count
            blur_img.get_pixel(x, y).green = pixel_g // count
            blur_img.get_pixel(x, y).blue = pixel_b // count
    return blur_img


def main():
    """
    blur an image by SimpleImage
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
