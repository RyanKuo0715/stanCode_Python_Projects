"""
File: bouncing_ball
Name: Jia-Hong Guo (Ryan Kuo)
-------------------------
TODO: simulate the motion of a ball hitting ground and bouncing
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

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 1
click = False
bounce_out = True


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global count, click, bounce_out
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    while count <= 3:
        pause(DELAY)
        onmouseclicked(bounce)
        if click:
            vy = 0
            while count <= 3:
                # make sure the ball only moves after the first 3 clicks
                ball.move(VX, vy)
                if ball.x > window.width:
                    # if the ball moves out of the frame, resume the initial status
                    # of the ball
                    count += 1
                    window.add(ball, x=START_X, y=START_Y)
                    bounce_out = True
                    click = False
                    break
                else:
                    # if the ball is in the frame, keeps bouncing
                    if ball.y >= window.height - ball.height and bounce_out:
                        # scenario 1: if the location of the ball is firstly under the
                        # ground, bounces
                        vy = -vy * REDUCE
                        bounce_out = False
                    else:
                        if vy > -0.1 and not bounce_out:
                            # scenario 2: if the vertical velocity of the ball is too small,
                            # make it 0 to avoid the bug of the program
                            vy = 0
                        else:
                            # scenario 3: if not scenario 1 and 2, make physics dominate the
                            # motion of the ball
                            vy += GRAVITY
                            if ball.y < window.height - ball.height:
                                bounce_out = True
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
