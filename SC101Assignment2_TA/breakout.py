"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.
Name: Jia-Hong Guo (Ryan Kuo)

Introduction of the Game:
1. Players have to click to let the ball move.
2. As the ball move, players have to use paddle to make the ball bounce up to break bricks.
3. Players initially have 3 lives. If the ball falls out of the frame, lives will be reduced
    by one. If there is no live, players are lost.
4. If all bricks are eliminated, players win.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    :return: the game of breakout
    """
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    while True:
        # pause
        pause(FRAME_RATE)
        # update
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        # check
        if live == 0:
            # if there is no live
            break
        if graphics.count_brick == 0:
            # if all bricks are eliminated
            break
        while dx != 0 and dy != 0:
            # pause
            pause(FRAME_RATE)
            # update
            graphics.ball.move(dx, dy)
            # check
            if (graphics.ball.x <= 0 and dx < 0) or \
                    (graphics.ball.x >= graphics.window.width - graphics.ball.width and dx > 0):
                # check if the ball hit the wall
                dx = -dx
                graphics.set_dx(dx)
            if graphics.ball.y <= 0 and dy < 0:
                # check if the ball hit the celling
                dy = -dy
                graphics.set_dy(dy)
            # check if the ball hit the paddle or a brick
            graphics.if_object()
            # upgrade speed
            dy = graphics.get_dy()
            if graphics.ball.y >= graphics.window.height:
                # check if the ball fall out of the frame
                live -= 1
                graphics.reset_ball()
                break
            if graphics.count_brick == 0:
                # check if all bricks eliminated
                break


if __name__ == '__main__':
    main()
