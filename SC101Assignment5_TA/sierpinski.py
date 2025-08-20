"""
File: sierpinski.py
Name: Ryan Kuo
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	draw Sierpinski Triangles with order given as a constant
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the order of Sierpinski Triangles
	:param length: int, the length of the Sierpinski Triangle of the first order
	:param upper_left_x: int, the x position of the upper-left-most vertices
	:param upper_left_y: int, the y position of the upper-left-most vertices
	:return: Sierpinski Triangles with a certain order
	"""
	if order == 0:
		pass
	else:
		pause(30)

		# upper line of a triangle
		line_up = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		# left line of a triangle
		line_left = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		# right line of a triangle
		line_right = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		window.add(line_up)
		window.add(line_left)
		window.add(line_right)

		# upper-left triangle created by recursion
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# upper-right triangle created by recursion
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		# lower triangle created by recursion
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length * 0.866 / 2)


if __name__ == '__main__':
	main()
