"""
File: bouncing_ball
Name: Ryan Kuo
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

click = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    window = GWindow(800, 500, title='bouncing_ball.py')
    window.add(ball, x=START_X, y=START_Y)

    count = 1
    global click

    while True:
        if count > 3:
            # make sure the ball only moves after the first 3 clicks
            break
        pause(DELAY)
        onmouseclicked(bounce)
        if click:
            vy = 0
            while True:
                ball.move(VX, vy)
                if ball.x > window.width:
                    # if the ball moves out of the frame, resume the initial status of the ball
                    count += 1
                    window.add(ball, x=START_X, y=START_Y)
                    click = False
                    break
                else:
                    # if the ball is in the frame, keeps bouncing
                    if ball.y >= window.height - ball.height and vy > 0:
                        # the ball touches the ground and bounces
                        vy = -vy * REDUCE
                    else:
                        # the ball is in the air, and gravity determines its motion
                        vy += GRAVITY
                pause(DELAY)


def bounce(event):
    """
    make sure the ball moves after a click, and any click during the motion
    has no effect on the ball
    """
    global click
    if not click:
        click = True


if __name__ == "__main__":
    main()
