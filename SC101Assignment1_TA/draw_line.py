"""
File: draw_line
Name: Ryan Kuo
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
circle = GOval(10, 10)
first_click = True


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global first_click
    if first_click:
        # deal with the odd click, a scenario in which a circle should be added
        window.add(circle, x=event.x-circle.width/2, y=event.y-circle.height/2)
        first_click = False
    else:
        # deal with the even click, a scenario in which a line should be added,
        # and the circle should be removed
        line = GLine(event.x, event.y, circle.x+circle.width/2, circle.y+circle.height/2)
        window.add(line)
        window.remove(circle)
        first_click = True


if __name__ == "__main__":
    main()
