"""
File: bouncing_ball_extension
Name: Jia-Hong Guo (Ryan Kuo)
-------------------------
TODO: Simulate the motion of a ball hitting ground and bouncing, with
air resistance and frictional force. The intensity of air resistance
is proportional to the speed of the ball, and that of frictional
force is constant.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
import math

VX = 3
DELAY = 10
GRAVITY = 1
AIR_RESISTANCE = 0.025
FRICTION = 0.05
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball_extension.py')
ball = GOval(SIZE, SIZE)
count = 1
click = False
bounce_out = True


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself. Air resistance force reduces sqrt(x**2+y**2)
    velocity with the intensity proportional to AIR_RESISTANCE, and
    frictional force reduces x velocity in a constant rate of FRICTION.
    """
    global count, click, bounce_out
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    while count <= 3:
        pause(DELAY)
        onmouseclicked(bounce)
        if click:
            vx = VX
            vy = 0
            while count <= 3:
                # make sure the ball only moves after the first 3 clicks
                ball.move(vx, vy)
                if ball.x > window.width or (not bounce_out and vy == 0 and vx <= 0):
                    # if the ball moves out of the frame or it stops on the ground with
                    # the velocity of 0, resume the initial status of the ball
                    count += 1
                    window.add(ball, x=START_X, y=START_Y)
                    bounce_out = True
                    click = False
                    break
                else:
                    # if the ball is in the frame and moves, keeps bouncing
                    if vx != 0:
                        # scenario x1: if vx is greater than 0, air resistance force
                        # drags it down
                        """
                        because the intensity of air force is proportional to its
                        velocity: sqrt(vx**2+vy**2), and because velocity belongs
                        to vector, so the effect of air resistance on vx should
                        be vx/sqrt(vx**2+vy**2)*AIR_RESISTANCE
                        """
                        vx = vx * (1 - 1 / math.sqrt(vx ** 2 + vy ** 2) * AIR_RESISTANCE)
                        if vy == 0 and not bounce_out:
                            # scenario x2: if the ball is on the ground and stops bouncing,
                            # frictional force from the ground also drags it down
                            vx -= FRICTION
                    if ball.y >= window.height - ball.height and bounce_out:
                        # scenario y1: if the location of the ball is firstly under the
                        # ground, bounces
                        vy = -vy * REDUCE
                        bounce_out = False
                    else:
                        if vy > -0.1 and not bounce_out:
                            # scenario y2: if the vertical velocity of the ball is too small,
                            # make it 0 to avoid the bug of the program
                            vy = 0
                        else:
                            # scenario y3: if not scenario y1 and y2, make physics dominate
                            # the vertical motion of the ball
                            if vy == 0:
                                # to avoid the bug when both vx and vy are 0, creating the
                                # error in the value of 1/sqrt(vx**2+vy**2)
                                vy = vy + GRAVITY
                            else:
                                """
                                because the intensity of air force is proportional to its
                                velocity: sqrt(vx**2+vy**2), and because velocity belongs
                                to vector, so the effect of air resistance on vy should
                                be vy/sqrt(vx**2+vy**2)*AIR_RESISTANCE
                                """
                                vy = vy * (1 - 1 / math.sqrt(vx ** 2 + vy ** 2) * AIR_RESISTANCE) + GRAVITY
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
