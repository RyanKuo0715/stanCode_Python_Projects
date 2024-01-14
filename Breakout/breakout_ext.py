"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.
Name: Jia-Hong Guo (Ryan Kuo)

Introduction of the Game:
1. Players have to click the START button to start game.
2. As game starts, player have to click to let the ball move.
3. As the ball move, players have to use paddle to make the ball bounce up to break bricks.
4. If a brick is broken, players will get score, depending on the type of brick.
    Blue: 1
    Green: 5
    Yellow: 10
    Orange: 50
    Red: 100
5. If a brick is broken, a treasure is possibly sent. There are 5 types of treasures.
    Blue Treasure: enlarge the paddle
    Green Treasure: shorten the paddle
    Yellow Treasure: enlarge the ball
    Orange Treasure: speed up to ball
    Red Treasure: get one more live
6. Players initially have 3 lives. If the ball falls out of the frame, lives will be reduced
    by one. If there is no lives, players are lost.
7. If all bricks are eliminated, players win.
8. The final scores of players will be shown.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphicsExt

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3           # Number of attempts


def main():
    """
    :return: the game of breakout
    """
    graphics = BreakoutGraphicsExt()
    live = NUM_LIVES
    graphics.set_live(live)
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
            # update ball
            graphics.ball.move(dx, dy)
            # check ball
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                # check if the ball hit the wall
                dx = -dx
            if graphics.ball.y <= 0:
                # check if the ball hit the celling
                dy = -dy
            # check if the ball hit the paddle or a brick
            change_vy = graphics.if_object()
            dy *= change_vy
            if graphics.ball.y >= graphics.window.height:
                # check if the ball fall out of the frame
                live -= 1
                graphics.set_live(live)
                graphics.reset_ball()
                break
            if graphics.count_brick == 0:
                # check if all bricks eliminated
                break
            # update treasure
            graphics.treasure1.move(0, graphics.dty1)
            graphics.treasure2.move(0, graphics.dty2)
            graphics.treasure3.move(0, graphics.dty3)
            graphics.treasure4.move(0, graphics.dty4)
            graphics.treasure5.move(0, graphics.dty5)
            # check treasure
            # check if player gets the treasure
            graphics.if_paddle()
            if graphics.speed_up:
                # get the speed-up treasure
                dx *= 1.2
                dy *= 1.2
            if graphics.one_live:
                # get the one-more-live treasure
                live += 1
                graphics.set_live(live)
            # check if the treasure fall out of the frame
            graphics.out_of_window()
    # show the final score
    graphics.score_frame(live)


if __name__ == '__main__':
    main()
