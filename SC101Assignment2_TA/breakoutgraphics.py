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

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.click = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.give_velocity)

        # Draw bricks
        self.count_brick = brick_rows*brick_cols
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.color = color[i//2]
                self.brick.fill_color = color[i//2]
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
        send dx to the user
        :return: the velocity in x direction
        """
        return self.__dx

    def get_dy(self):
        """
        send dy to the user
        :return: the velocity in y direction
        """
        return self.__dy

    def set_dx(self, dx):
        """
        get dx from the user
        :param dx: the velocity in x direction
        :return: the updated velocity in x direction in coder
        """
        self.__dx = dx

    def set_dy(self, dy):
        """
        get dy from the user
        :param dy: the velocity in y direction
        :return: the updated velocity in y direction in coder
        """
        self.__dy = dy

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
        for x in [self.ball.x, self.ball.x+self.ball.width]:
            for y in [self.ball.y, self.ball.y+self.ball.width]:
                obj = self.window.get_object_at(x, y)
                if obj is not None and obj is not self.paddle:
                    # the ball hits a brick
                    self.window.remove(obj)
                    self.count_brick -= 1
                    self.__dy = -self.__dy
                    return
                elif obj is not None and obj is self.paddle:
                    # the ball hits the paddle
                    if y == self.ball.y+self.ball.width and self.__dy > 0:
                        self.__dy = -self.__dy
                        return
