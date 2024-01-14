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
        self.paddle_offset = paddle_offset

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball_radius = ball_radius
        self.in_paddle = False

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

        # Create Score Board
        self.score = 0
        self.score_board = GLabel(f'Score: {self.score}')
        self.score_board.font = '-15'
        self.window.add(self.score_board, x=10, y=window_height-10)

        # Create Live Board
        self.live = 0
        self.live_board = GLabel(f'Live: ')
        self.live_board.font = '-15'
        self.window.add(self.live_board, x=window_width-65, y=window_height-10)

        # Create Treasure
        # the lengthen-the-paddle treasure
        self.treasure1 = GRect(self.brick.width * 0.4, self.brick.width * 0.4)
        self.treasure1.filled = True
        self.treasure1.color = 'blue'
        self.treasure1.fill_color = 'blue'
        self.dty1 = 0
        # the shorten-the-paddle treasure
        self.treasure2 = GRect(self.brick.width * 0.4, self.brick.width * 0.4)
        self.treasure2.filled = True
        self.treasure2.color = 'green'
        self.treasure2.fill_color = 'green'
        self.dty2 = 0
        # the enlarge-the-ball treasure
        self.treasure3 = GRect(self.brick.width * 0.4, self.brick.width * 0.4)
        self.treasure3.filled = True
        self.treasure3.color = 'yellow'
        self.treasure3.fill_color = 'yellow'
        self.dty3 = 0
        # the speed-up treasure
        self.treasure4 = GRect(self.brick.width * 0.4, self.brick.width * 0.4)
        self.treasure4.filled = True
        self.treasure4.color = 'orange'
        self.treasure4.fill_color = 'orange'
        self.dty4 = 0
        self.speed_up = False
        # the one-more-life treasure
        self.treasure5 = GRect(self.brick.width * 0.4, self.brick.width * 0.4)
        self.treasure5.filled = True
        self.treasure5.color = 'red'
        self.treasure5.fill_color = 'red'
        self.dty5 = 0
        self.one_live = False

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
        self.live = live
        self.live_board.text = f'Live: {self.live}'

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
        self.window.remove(self.ball)
        self.ball_radius = BALL_RADIUS
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=self.window.width/2-self.ball_radius, y=self.window.height/2-self.ball_radius)
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
        obj_ur = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y)
        obj_dl = self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2)
        obj_dr = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2)
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
            elif obj_dl.width == self.brick.width:
                # if down-left side of the ball touch a brick
                self.window.remove(obj_dl)
                self.update_score(obj_dl)
                self.treasure_move(obj_dl)
                return -1
            else:
                return 1
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
            elif obj_dr.width == self.brick.width:
                # if down-right side of the ball touch a brick
                self.window.remove(obj_dr)
                self.update_score(obj_dr)
                self.treasure_move(obj_dr)
                return -1
            else:
                return 1
        elif obj_ul is not None:
            if obj_ul.width == self.brick.width:
                # if up-left side of the ball touch a brick
                self.window.remove(obj_ul)
                self.update_score(obj_ul)
                self.treasure_move(obj_ul)
                return -1
            else:
                return 1
        elif obj_ur is not None:
            if obj_ur.width == self.brick.width:
                # if up-right side of the ball touch a brick
                self.window.remove(obj_ur)
                self.update_score(obj_ur)
                self.treasure_move(obj_ur)
                return -1
            else:
                return 1
        else:
            # if the ball touches nothing (leave the paddle)
            self.in_paddle = False
            return 1

    def update_score(self, obj):
        """
        if the ball hit a brick, update the score depending on what brick was hit
        :param obj: the brick hit by the ball
        :return: the new total score
        """
        self.count_brick -= 1
        if obj.color.r == 0 and obj.color.g == 0 and obj.color.b == 255:
            # when the blue brick is hit, get 1 point
            self.score += 1
        if obj.color.r == 0 and obj.color.g == 128 and obj.color.b == 0:
            # when the green brick is hit, get 5 points
            self.score += 5
        if obj.color.r == 255 and obj.color.g == 255 and obj.color.b == 0:
            # when the yellow brick is hit, get 10 points
            self.score += 10
        if obj.color.r == 255 and obj.color.g == 200 and obj.color.b == 0:
            # when the orange brick is hit, get 50 points
            self.score += 50
        if obj.color.r == 255 and obj.color.g == 0 and obj.color.b == 0:
            # when the red brick is hit, get 100 points
            self.score += 100
        self.score_board.text = f'Score: {self.score}'

    def treasure_move(self, obj):
        """
        determine whether a treasure and what treasure should be given
        :param obj: the brick hit by the ball
        :return: a treasure generated randomly
        """
        a = random.random()
        if 0 < a <= 0.1 and self.dty1 == 0:
            # give the lengthen-the-paddle treasure (possibility: 10%)
            self.window.add(self.treasure1, x=obj.x+self.brick.width*0.3, y=obj.y)
            self.dty1 = 2
        elif 0.1 < a <= 0.2 and self.dty2 == 0:
            # give the shorten-the-paddle treasure (possibility: 10%)
            self.window.add(self.treasure2, x=obj.x+self.brick.width*0.3, y=obj.y)
            self.dty2 = 2
        elif 0.2 < a <= 0.25 and self.dty3 == 0:
            # give the enlarge-the-ball treasure (possibility: 5%)
            self.window.add(self.treasure3, x=obj.x+self.brick.width*0.3, y=obj.y)
            self.dty3 = 2
        elif 0.25 < a <= 0.3 and self.dty4 == 0:
            # give the speed-up-the-ball treasure (possibility: 5%)
            self.window.add(self.treasure4, x=obj.x+self.brick.width*0.3, y=obj.y)
            self.dty4 = 2
        elif 0.3 < a <= 0.33 and self.dty5 == 0:
            # give the one-more-live treasure (possibility: 3%)
            self.window.add(self.treasure5, x=obj.x+self.brick.width*0.3, y=obj.y)
            self.dty5 = 2

    def if_paddle(self):
        """
        determine whether the player get a treasure
        :return: the updated status of the game if the player get a treasure
        """
        if self.dty1 != 0:
            # the lengthen-the-paddle treasure
            obj_dl1 = self.window.get_object_at(self.treasure1.x-1, self.treasure1.y+self.brick.width*0.4-1)
            obj_dr1 = self.window.get_object_at(self.treasure1.x+self.brick.width*0.4+1,
                                                self.treasure1.y+self.brick.width*0.4-1)
            if obj_dl1 is self.paddle or obj_dr1 is self.paddle:
                # get the lengthen-the-paddle treasure,
                # then the paddle lengthened by 15 pixels, with the limit 120 pixels
                if self.paddle.width < 120:
                    self.paddle_width += 15
                    x = self.paddle.x
                    self.window.remove(self.paddle)
                    self.paddle = GRect(self.paddle_width, self.paddle.height)
                    self.paddle.filled = True
                    self.paddle.color = 'black'
                    self.paddle.fill_color = 'black'
                    self.window.add(self.paddle, x=x, y=self.window.height-self.paddle_offset)
                self.window.remove(self.treasure1)
                self.dty1 = 0
        if self.dty2 != 0:
            # the shorten-the-paddle treasure
            obj_dl2 = self.window.get_object_at(self.treasure2.x-1, self.treasure2.y+self.brick.width*0.4-1)
            obj_dr2 = self.window.get_object_at(self.treasure2.x+self.brick.width*0.4+1,
                                                self.treasure2.y+self.brick.width*0.4-1)
            if obj_dl2 is self.paddle or obj_dr2 is self.paddle:
                # get the shorten-the-paddle treasure,
                # then the paddle shortened by 15 pixels, with the limit 30 pixels
                if self.paddle.width > 30:
                    self.paddle_width -= 15
                    x = self.paddle.x
                    self.window.remove(self.paddle)
                    self.paddle = GRect(self.paddle_width, self.paddle.height)
                    self.paddle.filled = True
                    self.paddle.color = 'black'
                    self.paddle.fill_color = 'black'
                    self.window.add(self.paddle, x=x, y=self.window.height-self.paddle_offset)
                self.window.remove(self.treasure2)
                self.dty2 = 0
        if self.dty3 != 0:
            # the enlarge-the-ball treasure
            obj_dl3 = self.window.get_object_at(self.treasure3.x-1, self.treasure3.y+self.brick.width*0.4-1)
            obj_dr3 = self.window.get_object_at(self.treasure3.x+self.brick.width*0.4+1,
                                                self.treasure3.y+self.brick.width*0.4-1)
            if obj_dl3 is self.paddle or obj_dr3 is self.paddle:
                # get the enlarge-the-ball treasure,
                # then the radius of the ball enlarged by 1.5 times
                if self.ball_radius == BALL_RADIUS:
                    self.ball_radius *= 1.5
                    x = self.ball.x
                    y = self.ball.y
                    self.window.remove(self.ball)
                    self.ball = GOval(self.ball_radius*2, self.ball_radius*2)
                    self.ball.filled = True
                    self.ball.color = 'black'
                    self.ball.fill_color = 'black'
                    self.window.add(self.ball, x=x-self.ball_radius*0.25, y=y-self.ball_radius*0.25)
                self.window.remove(self.treasure3)
                self.dty3 = 0
        if self.dty4 != 0:
            # the speed-up-the-ball treasure
            obj_dl4 = self.window.get_object_at(self.treasure4.x-1, self.treasure4.y+self.brick.width*0.4-1)
            obj_dr4 = self.window.get_object_at(self.treasure4.x+self.brick.width*0.4+1,
                                                self.treasure4.y+self.brick.width*0.4-1)
            if obj_dl4 is self.paddle or obj_dr4 is self.paddle:
                # get the speed-up-the-ball treasure,
                # then the speed of the ball raised by 1.2 times
                self.speed_up = True
                self.window.remove(self.treasure4)
                self.dty4 = 0
            else:
                # does not get the speed-up-the-ball treasure
                self.speed_up = False
        else:
            # the speed-up-the-ball treasure has not been created
            self.speed_up = False
        if self.dty5 != 0:
            # the one-more-live treasure
            obj_dl5 = self.window.get_object_at(self.treasure5.x-1, self.treasure5.y+self.brick.width*0.4-1)
            obj_dr5 = self.window.get_object_at(self.treasure5.x+self.brick.width*0.4+1,
                                                self.treasure5.y+self.brick.width*0.4-1)
            if obj_dl5 is self.paddle or obj_dr5 is self.paddle:
                # get the one-more-live treasure,
                # then the number of lives increased by 1
                self.one_live = True
                self.window.remove(self.treasure5)
                self.dty5 = 0
            else:
                # does not get the one-more-live treasure
                self.one_live = False
        else:
            # the one-more-live treasure has not been created
            self.one_live = False

    def out_of_window(self):
        """
        determine whether the treasure falls out of frame
        :return: reset the status of the treasure if it falls out of the frame
        """
        if self.dty1 != 0:
            if self.treasure1.y >= self.window.height:
                # the lengthen-the-paddle treasure falls out of the frame
                self.dty1 = 0
        if self.dty2 != 0:
            if self.treasure2.y >= self.window.height:
                # the shorten-the-paddle treasure falls out of the frame
                self.dty2 = 0
        if self.dty3 != 0:
            if self.treasure3.y >= self.window.height:
                # the enlarge-the-ball treasure falls out of the frame
                self.dty3 = 0
        if self.dty4 != 0:
            if self.treasure4.y >= self.window.height:
                # the speed-up-the-ball treasure falls out of the frame
                self.dty4 = 0
        if self.dty5 != 0:
            if self.treasure5.y >= self.window.height:
                # the one-more-live treasure falls out of the frame
                self.dty5 = 0

    def score_frame(self, live):
        """
        create the final score frame if the game ends
        :param live: the number of lives
        :return: the word and the final score shown for the player
        """
        # create the frame for the final scene
        self.window.add(self.result_frame, x=0, y=self.window.height*0.25)
        if live == 0:
            # if there is no live remain, show the word for the loser
            self.window.add(self.lost, x=(self.result_frame.width-self.lost.width)/2,
                            y=self.result_frame.height+self.lost.height+10)
        if live > 0:
            # if there is at least one live remain, show the word for the winner
            self.window.add(self.win, x=(self.result_frame.width-self.win.width)/2,
                            y=self.result_frame.height+self.win.height+10)
        # show the final score
        self.end_score.text = f'Score: {self.score}'
        self.window.add(self.end_score, x=(self.result_frame.width-self.end_score.width)/2,
                        y=self.result_frame.height+self.end_score.height+self.win.height+50)
