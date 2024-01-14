"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.
Name: Jia-Hong Guo (Ryan Kuo)

It contains a class "BreakoutGraphics" to create elements for the game of breakout.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        """
        :param ball_radius: the radius of the ball
        :param paddle_width: the width of the paddle
        :param paddle_height: the height of the paddle
        :param paddle_offset: the distance between the paddle and the lower-side of the window
        :param brick_rows: the number of bricks in a row
        :param brick_cols: the number of bricks in a column
        :param brick_width: the width of a brick
        :param brick_height: the height of a brick
        :param brick_offset: the distance between the top bricks and the upper-side of the window
        :param brick_spacing: the distance between each brick
        :param title: the name of the window
        """

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.in_paddle = False

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.click = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.give_velocity)

        # Draw bricks
        self.count_brick = brick_rows*brick_cols
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    # create the red blocks
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif i == 2 or i == 3:
                    # create the orange blocks
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif i == 4 or i == 5:
                    # create the yellow blocks
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif i == 6 or i == 7:
                    # create the green blocks
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                elif i == 8 or i == 9:
                    # create the blue blocks
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=j*(brick_width+brick_spacing),
                                y=brick_offset+i*(brick_height+brick_spacing))

    def paddle_move(self, event):
        """
        set the position of the paddle by the movement of the mouse
        :param event: the position of the mouse
        :return: the paddle track the position of the mouse
        """
        if event.x < self.paddle.width/2:
            self.paddle.x = 0
        elif event.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x-self.paddle.width/2

    def give_velocity(self, event):
        """
        give the ball velocity if the ball is at its initial position with velocity 0
        :param event: the click of the mouse
        :return: the velocity for the ball
        """
        if not self.click:
            self.click = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def get_dx(self):
        """
        send dx to the coder
        :return: the velocity in x direction
        """
        return self.__dx

    def get_dy(self):
        """
        send dy to the coder
        :return: the velocity in y direction
        """
        return self.__dy

    def reset_ball(self):
        """
        reset the ball to its initial status if the ball falls out of the frame
        :return: the initial status of the ball
        """
        self.ball.x = self.window.width/2 - self.ball.width/2
        self.ball.y = self.window.height/2 - self.ball.width/2
        self.__dx = 0
        self.__dy = 0
        self.click = False

    def if_object(self):
        """
        react to scenarios that the ball hits the paddle or a brick
        if the ball hits the paddle, it bounces in y direction
        if the ball hits a brick, it bounces in y direction and that brick eliminated
        :return: the reaction after the ball hits object
        """
        obj_ul = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_ur = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
        obj_dl = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width)
        obj_dr = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.width)
        if obj_dl is not None:
            if obj_dl is self.paddle:
                # if down-left side of the ball touch the paddle
                if not self.in_paddle:
                    # if the ball touch the paddle firstly
                    self.in_paddle = True
                    return -1
                else:
                    # if the ball touched the paddle but has not already left it
                    return 1
            else:
                # if down-left side of the ball touch a brick
                self.window.remove(obj_dl)
                self.count_brick -= 1
                return -1
        elif obj_dr is not None:
            if obj_dr is self.paddle:
                # if down-right side of the ball touch the paddle
                if not self.in_paddle:
                    # if down-left side of the ball touch the paddle
                    self.in_paddle = True
                    return -1
                else:
                    # if the ball touched the paddle but has not already left it
                    return 1
            else:
                # if down-right side of the ball touch a brick
                self.window.remove(obj_dr)
                self.count_brick -= 1
                return -1
        elif obj_ul is not None and obj_ul is not self.paddle:
            # if up-left side of the ball touch a brick
            self.window.remove(obj_ul)
            self.count_brick -= 1
            return -1
        elif obj_ur is not None and obj_ur is not self.paddle:
            # if up-right side of the ball touch a brick
            self.window.remove(obj_ur)
            self.count_brick -= 1
            return -1
        else:
            # if the ball touches nothing (leave the paddle)
            self.in_paddle = False
            return 1
