"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.
Name: Jia-Hong Guo (Ryan Kuo)

It contains a class "BreakoutGraphics" to create elements for the game of breakout.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
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
TREASURE_SPEED = 2     # Speed for the treasure


class BreakoutGraphicsExt:
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
        self.paddle_width = paddle_width

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.start_click = False
        self.click = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.give_velocity)

        # Draw bricks
        self.count_brick = brick_rows*brick_cols
        self.bricks = [('red', (0, 0, 255), 1),
                       ('orange', (0, 128, 0), 5),
                       ('yellow', (255, 255, 0), 10),
                       ('green', (255, 200, 0), 50),
                       ('blue', (255, 0, 0), 100)]
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.color = self.bricks[i//2][0]
                self.brick.fill_color = self.bricks[i//2][0]
                self.window.add(self.brick, x=j*(brick_width+brick_spacing),
                                y=brick_offset+i*(brick_height+brick_spacing))

        # Create Score Board
        self.score = 0
        self.score_board = GLabel(f'Score: {self.score}')
        self.score_board.font = 'Calibri-15'
        self.window.add(self.score_board, x=10, y=window_height-10)

        # Create Board
        self.lives = 0
        self.live_board = GLabel(f'Live: ')
        self.live_board.font = 'Calibri-15'
        self.window.add(self.live_board, x=window_width-65, y=window_height-10)

        # Create Treasure
        self.treasure_width = self.brick.width * 0.4
        self.treasure1 = GRect(self.treasure_width, self.treasure_width)
        self.treasure2 = GRect(self.treasure_width, self.treasure_width)
        self.treasure3 = GRect(self.treasure_width, self.treasure_width)
        self.treasure4 = GRect(self.treasure_width, self.treasure_width)
        self.treasure5 = GRect(self.treasure_width, self.treasure_width)
        self.dty = [0, 0, 0, 0, 0]
        self.treasures = [(self.treasure1, 'blue', 0, (0.0, 0.1)),
                          (self.treasure2, 'green', 1, (0.1, 0.2)),
                          (self.treasure3, 'yellow', 2, (0.2, 0.25)),
                          (self.treasure4, 'orange', 3, (0.25, 0.3)),
                          (self.treasure5, 'red', 4, (0.3, 0.33))]
        for treasure in self.treasures:
            treasure[0].filled = True
            treasure[0].color = treasure[1]
            treasure[0].fill_color = treasure[1]

        # Create Welcome Frame
        # create the title of the game
        self.game_name = GLabel('Ryan\'s Breakout')
        self.game_name.font = 'Helvetica-43'
        self.window.add(self.game_name, x=(window_width-self.game_name.width)/2, y=window_height*0.7)
        # create the button
        self.button = GRect(window_width*0.3, window_height*0.05)
        self.button.filled = True
        self.button.color = 'gold'
        self.button.fill_color = 'gold'
        self.window.add(self.button, x=(window_width-self.button.width)/2, y=window_height*0.8)
        # create the START indication on the button
        self.start = GLabel('START')
        self.start.font = 'Helvetica-15'
        self.window.add(self.start, x=(window_width-self.start.width)/2+2,
                        y=self.button.y+(self.button.height+self.start.height)/2+2)

        # Create Score Frame
        # create the word for the winner of the game
        self.win = GLabel('You Pass SC101')
        self.win.font = 'Helvetica-40'
        # create the word for the loser of the game
        self.lost = GLabel('You Failed :(')
        self.lost.font = 'Helvetica-40'
        # show the final score
        self.end_score = GLabel(f'Score: {self.score}')
        self.end_score.font = 'Helvetica-30'
        # create the frame for the final scene
        self.result_frame = GRect(window_width, window_height*0.3)
        self.result_frame.filled = True
        self.result_frame.color = 'lightsage'
        self.result_frame.fill_color = 'lightsage'

    def set_live(self, live):
        """
        get the information of the number of lives from the coder
        :param live: the number of lives
        :return: the number of lives shown in the frame
        """
        self.lives = live
        self.live_board.text = f'Live: {self.lives}'

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
        start the game and close the welcome frame
        give the ball velocity if the ball is at its initial position with velocity 0
        :param event: the click of the mouse
        :return: the start of the game and the velocity for the ball
        """
        if not self.start_click:
            # if the game has not started, click the button to start the game
            obj_button = self.window.get_object_at(event.x, event.y)
            if obj_button is self.button or obj_button is self.start:
                self.window.remove(self.game_name)
                self.window.remove(self.button)
                self.window.remove(self.start)
                self.start_click = True
        if self.start_click:
            # if the game has started, click to make the ball move
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

    def set_dx(self, vx):
        """
        get dx from the user
        :param vx: the velocity in x direction
        :return: the updated velocity in x direction in coder
        """
        self.__dx = vx

    def set_dy(self, vy):
        """
        get dy from the user
        :param vy: the velocity in y direction
        :return: the updated velocity in y direction in coder
        """
        self.__dy = vy

    def reset_ball(self, radius=BALL_RADIUS):
        """
        reset the ball if the ball falls out of the frame or players get the
        enlarge-the-ball treasure
        :param radius: the updated radius of the ball
        :return: the updated status of the ball
        """
        x, y = self.ball.x, self.ball.y
        self.window.remove(self.ball)
        self.ball = GOval(radius*2, radius*2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        if radius == BALL_RADIUS:
            # if the ball falls out of the frame
            self.window.add(self.ball, x=self.window.width/2-radius, y=self.window.height/2-radius)
            self.ball_radius = BALL_RADIUS
            self.__dx = 0
            self.__dy = 0
            self.click = False
        elif radius == int(BALL_RADIUS*1.5):
            # if players get the enlarge-the-ball treasure
            self.window.add(self.ball, x=x-radius*0.25, y=y-radius*0.25)

    def reset_paddle(self, width=PADDLE_WIDTH):
        """
        reset the paddle if the ball falls out of the frame or players get the
        enlarge-the-paddle or the shorten-the-paddle treasure
        :param width: the updated width of the paddle
        :return: the updated status of the paddle
        """
        x = self.paddle.x+self.paddle.width//2
        self.window.remove(self.paddle)
        self.paddle = GRect(width, self.paddle.height)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=x-(width//2), y=self.window.height-PADDLE_OFFSET)
        if width == PADDLE_WIDTH:
            self.paddle_width = width

    def reset_treasures(self, mode=None):
        """
        remove all treasures if the ball falls out of the frame,
        or remove the certain treasure that falls out of the frame
        :return: remove treasure(s) and reset its/their status
        """
        for treasure in self.treasures:
            if self.dty[treasure[2]] != 0:
                if mode == 'all_reset' or treasure[0].y >= self.window.height:
                    self.window.remove(treasure[0])
                    self.dty[treasure[2]] = 0

    def if_object(self):
        """
        react to scenarios that the ball hits the paddle or a brick
        if the ball hits the paddle, it bounces in y direction
        if the ball hits a brick, it bounces in y direction and that brick eliminated
        :return: the reaction after the ball hits object
        """
        for x in [self.ball.x, self.ball.x+self.ball_radius*2]:
            for y in [self.ball.y, self.ball.y+self.ball_radius*2]:
                obj = self.window.get_object_at(x, y)
                if obj is not None and obj.width == self.brick.width:
                    # the ball hits a brick
                    self.window.remove(obj)
                    self.update_score(obj)
                    self.treasure_move(obj)
                    self.__dy = -self.__dy
                    return
                elif obj is not None and obj is self.paddle:
                    # the ball hits the paddle
                    if y == self.ball.y+self.ball_radius*2 and self.__dy > 0:
                        self.__dy = -self.__dy
                        return

    def update_score(self, obj):
        """
        if the ball hit a brick, update the score depending on what brick was hit
        :param obj: the brick hit by the ball
        :return: the new total score
        """
        self.count_brick -= 1
        for brick in self.bricks:
            if obj.color.r == brick[1][0] and obj.color.g == brick[1][1] and obj.color.b == brick[1][2]:
                self.score += brick[2]
                break
        self.score_board.text = f'Score: {self.score}'

    def treasure_move(self, obj):
        """
        determine whether a treasure and what treasure should be given
        :param obj: the brick hit by the ball
        :return: a treasure generated randomly
        """
        a = random.random()
        for treasure in self.treasures:
            if float(treasure[3][0]) < a <= float(treasure[3][1]) and self.dty[treasure[2]] == 0:
                self.window.add(treasure[0], x=obj.x+self.brick.width*0.3, y=obj.y)
                self.dty[treasure[2]] = TREASURE_SPEED
                break

    def if_paddle(self):
        """
        determine whether the player get a treasure
        :return: the updated status of the game if the player get a treasure
        """
        for treasure in self.treasures:
            if_break = False
            if self.dty[treasure[2]] != 0:
                for x in [treasure[0].x-1, treasure[0].x+self.treasure_width+1]:
                    for y in [treasure[0].y-1, treasure[0].y+self.treasure_width+1]:
                        obj = self.window.get_object_at(x, y)
                        if obj is self.paddle:
                            if treasure[0] == self.treasure1:
                                # get the lengthen-the-paddle treasure,
                                # then the paddle lengthened by 15 pixels, with the limit 120 pixels
                                if self.paddle_width < 120:
                                    self.paddle_width += 15
                                    self.reset_paddle(self.paddle_width)
                            elif treasure[0] == self.treasure2:
                                # get the shorten-the-paddle treasure,
                                # then the paddle shortened by 15 pixels, with the limit 30 pixels
                                if self.paddle_width > 30:
                                    self.paddle_width -= 15
                                    self.reset_paddle(self.paddle_width)
                            elif treasure[0] == self.treasure3:
                                # get the enlarge-the-ball treasure,
                                # then the radius of the ball enlarged by 1.5 times
                                if self.ball_radius == BALL_RADIUS:
                                    self.ball_radius = int(self.ball_radius*1.5)
                                    self.reset_ball(self.ball_radius)
                            elif treasure[0] == self.treasure4:
                                # get the speed-up-the-ball treasure,
                                # then the speed of the ball raised by 1.2 times
                                self.__dx = self.__dx * 1.2
                                self.__dy = self.__dy * 1.2
                            elif treasure[0] == self.treasure5:
                                # get the one-more-live treasure,
                                # then the number of lives increased by 1
                                self.set_live(self.lives+1)
                            self.window.remove(treasure[0])
                            self.dty[treasure[2]] = 0
                            if_break = True
                            break
                    if if_break:
                        break

    def score_frame(self):
        """
        create the final score frame if the game ends
        :return: the word and the final score shown for the player
        """
        # create the frame for the final scene
        self.window.add(self.result_frame, x=0, y=self.window.height*0.25)
        if self.lives == 0:
            # if there is no live remain, show the word for the loser
            self.window.add(self.lost, x=(self.result_frame.width-self.lost.width)/2,
                            y=self.result_frame.height+self.lost.height+10)
        if self.lives > 0:
            # if there is at least one live remain, show the word for the winner
            self.window.add(self.win, x=(self.result_frame.width-self.win.width)/2,
                            y=self.result_frame.height+self.win.height+10)
        # show the final score
        self.end_score.text = f'Score: {self.score}'
        self.window.add(self.end_score, x=(self.result_frame.width-self.end_score.width)/2,
                        y=self.result_frame.height+self.end_score.height+self.win.height+50)
