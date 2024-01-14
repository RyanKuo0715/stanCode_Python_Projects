"""
File: stanCodoshop.py
Name: Jia-Hong Guo (Ryan Kuo)
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    return math.sqrt((pixel.red-red)**2+(pixel.green-green)**2+(pixel.blue-blue)**2)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """

    total_r = sum(pixel.red for pixel in pixels)
    total_g = sum(pixel.green for pixel in pixels)
    total_b = sum(pixel.blue for pixel in pixels)
    return [total_r//len(pixels), total_g//len(pixels), total_b//len(pixels)]

    # # red average
    # total = 0
    # for pixel in pixels:
    #     total += pixel.red
    # avg_red = total//len(pixels)
    # # green average
    # total = 0
    # for pixel in pixels:
    #     total += pixel.green
    # avg_green = total//len(pixels)
    # # blue average
    # total = 0
    # for pixel in pixels:
    #     total += pixel.blue
    # avg_blue = total//len(pixels)
    #
    # return [avg_red, avg_green, avg_blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """

    # get the average pixel
    avg = get_average(pixels)

    # compare distance of each pixel to the average pixel
    dist_list = []
    for pixel in pixels:
        dist_pixel = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        dist_list.append((dist_pixel, pixel))
        # (dist_pixel, pixel)是tuple
    return min(dist_list, key=lambda t: t[0])[1]
    # 一定要寫key=lambda t: t[0]，因為如果t[0]的值一樣，它會比較t[1]，但那是pixel，無法比較

    # distance = get_pixel_dist(pixels[0], avg[0], avg[1], avg[2])
    # best_pixel = pixels[0]
    # for pixel in pixels:
    #     dist_pixel = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
    #     if dist_pixel < distance:
    #         distance = dist_pixel
    #         best_pixel = pixel
    # return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """

    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # # Milestone 1 Test
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # # Milestone 2 Test
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # # Milestone 3 Test
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    for i in range(width):
        for j in range(height):
            pixel_ij = []
            for image in images:
                # get pixel from each image
                pixel_ij.append(image.get_pixel(i, j))
            # find the best pixel
            best_pixel = get_best_pixel(pixel_ij)
            best = result.get_pixel(i, j)
            best.red = best_pixel.red
            best.green = best_pixel.green
            best.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        # os.listdir()會告訴你資料夾裡面有哪些資料(可以看到隱藏檔案)
        # 用法：先import os，再os.listdir()
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
            # os.path.join(dir, filename)：資料夾跟檔名合併，會變成dir/filename
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
