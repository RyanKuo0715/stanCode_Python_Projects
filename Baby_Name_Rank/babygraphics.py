"""
File: babygraphics.py
Name: Jia-Hong GUO (Ryan Kuo)
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui
# gui = graphical user interface

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    width_per_year = (width-2*GRAPH_MARGIN_SIZE)//len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + width_per_year*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # draw 2 horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # draw vertical lines and year texts
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    y_unit = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK
    for i in range(len(lookup_names)):
        color = COLORS[i%4]
        for j in range(len(YEARS)-1):
            # get the x-coordinates of line segments
            # left-side data
            year1 = str(YEARS[j])
            x1_coordinate = get_x_coordinate(CANVAS_WIDTH, j)
            # right-side data
            year2 = str(YEARS[j+1])
            x2_coordinate = get_x_coordinate(CANVAS_WIDTH, j+1)
            # get the y-coordinates of line segments and the ranks
            # left-side data
            if year1 in name_data[lookup_names[i]]:
                # if the rank is within the maximum of the rank
                rank1 = int(name_data[lookup_names[i]][year1])
                y1_coordinate = rank1*y_unit+GRAPH_MARGIN_SIZE
            else:
                # if the rank is out of the maximum of the rank
                rank1 = '*'
                y1_coordinate = MAX_RANK*y_unit+GRAPH_MARGIN_SIZE
            # right-side data
            if year2 in name_data[lookup_names[i]]:
                # if the rank is within the maximum of the rank
                rank2 = int(name_data[lookup_names[i]][year2])
                y2_coordinate = rank2*y_unit+GRAPH_MARGIN_SIZE
            else:
                # if the rank is out of the maximum of the rank
                rank2 = '*'
                y2_coordinate = MAX_RANK*y_unit+GRAPH_MARGIN_SIZE
            # draw line segments
            canvas.create_line(x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate,
                               width=LINE_WIDTH, fill=color)
            # create texts of ranks and names for years except the last one
            canvas.create_text(x1_coordinate+TEXT_DX, y1_coordinate, text=f'{lookup_names[i]} {rank1}',
                               anchor=tkinter.SW, fill=color)
            if year2 == str(YEARS[len(YEARS)-1]):
                # create texts of ranks and names for the last year
                canvas.create_text(x2_coordinate+TEXT_DX, y2_coordinate, text=f'{lookup_names[i]} {rank2}',
                                   anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
