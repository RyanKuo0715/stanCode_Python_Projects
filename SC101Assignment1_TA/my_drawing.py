"""
File: my_drawing
Name: Ryan Kuo
----------------------
Title: Taipei, My Home
Next year, I will study finance in Singapore. I believe that I will miss
Taiwan at that time, especially Taipei, my hometown. On the other hand,
I hope that I have a chance to share the beauty of my hometown to foreign
friends. So I depicted my impression of Taipei with Python, not only
providing me with memory, but also sharing the scenery internationally.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(720, 405, title='Taipei, My Home')


def main():
    """
    Draw the scenery of Taipei, including mountains, buildings,
    especially Taipei 101. This program has 3 main function: sky,
    background, and building. In the function of sky, it has 3
    sub-functions: sky_color, moon, and star. In the function of
    background, it has 3 sub-functions: mountain, bg_building, and
    Taipei 101. In the function of building, it has 2 sub-functions:
    f_building and sign.
    Reminder: The number of objects in the program is huge, so it
    takes about 3 seconds to generate the whole picture.
    """
    sky()
    background()
    building()


def sky():
    """
    Draw objects in the sky, such as a moon and stars.
    """
    sky_color()
    moon()
    star()


def background():
    """
    Draw objects as the background, including mountains,
    buildings, and the Taipei 101.
    """
    mountain()
    bg_building()
    taipei_101()


def building():
    """
    Draw builds that are closer to viewers, creating the sense
    of depth of field. On the right bottom is my name.
    """
    f_building()
    sign()


def sky_color():
    """
    Create the sky and fill it with color.
    """
    sky_rec = GRect(720, 405)
    sky_rec.filled = True
    sky_rec.color = 'cornflowerblue'
    sky_rec.fill_color = 'cornflowerblue'
    window.add(sky_rec)


def moon():
    """
    Create a moon.
    """
    moon_circle = GOval(30, 30)
    moon_circle.filled = True
    moon_circle.color = 'lemonchiffon'
    moon_circle.fill_color = 'lemonchiffon'
    window.add(moon_circle, x=45, y=45)


def star():
    """
    Create 20 stars with different sizes and colors, with positions
    of stars generated randomly by the code random.randint(a,b)
    and tuned by creator to make them scatter in better position.
    """
    # star 1
    star1 = GOval(5, 5)
    star1.filled = True
    star1.color = 'white'
    star1.fill_color = 'white'
    window.add(star1, x=216, y=69)
    # star 2
    star2 = GOval(3, 3)
    star2.filled = True
    star2.color = 'floralwhite'
    star2.fill_color = 'floralwhite'
    window.add(star2, x=442, y=82)
    # star 3
    star3 = GOval(5, 5)
    star3.filled = True
    star3.color = 'white'
    star3.fill_color = 'white'
    window.add(star3, x=346, y=65)
    # star 4
    star4 = GOval(4, 4)
    star4.filled = True
    star4.color = 'floralwhite'
    star4.fill_color = 'floralwhite'
    window.add(star4, x=8, y=120)
    # star 5
    star5 = GOval(3, 3)
    star5.filled = True
    star5.color = 'ivory'
    star5.fill_color = 'ivory'
    window.add(star5, x=253, y=134)
    # star 6
    star6 = GOval(5, 5)
    star6.filled = True
    star6.color = 'white'
    star6.fill_color = 'white'
    window.add(star6, x=533, y=19)
    # star 7
    star7 = GOval(5, 5)
    star7.filled = True
    star7.color = 'white'
    star7.fill_color = 'white'
    window.add(star7, x=284, y=37)
    # star 8
    star8 = GOval(3, 3)
    star8.filled = True
    star8.color = 'floralwhite'
    star8.fill_color = 'floralwhite'
    window.add(star8, x=170, y=66)
    # star 9
    star9 = GOval(5, 5)
    star9.filled = True
    star9.color = 'ivory'
    star9.fill_color = 'ivory'
    window.add(star9, x=36, y=125)
    # star 10
    star10 = GOval(4, 4)
    star10.filled = True
    star10.color = 'white'
    star10.fill_color = 'white'
    window.add(star10, x=120, y=166)
    # star 11
    star1 = GOval(5, 5)
    star1.filled = True
    star1.color = 'white'
    star1.fill_color = 'white'
    window.add(star1, x=26, y=34)
    # star 12
    star2 = GOval(3, 3)
    star2.filled = True
    star2.color = 'white'
    star2.fill_color = 'white'
    window.add(star2, x=592, y=112)
    # star 13
    star3 = GOval(3, 3)
    star3.filled = True
    star3.color = 'floralwhite'
    star3.fill_color = 'floralwhite'
    window.add(star3, x=646, y=30)
    # star 14
    star4 = GOval(4, 4)
    star4.filled = True
    star4.color = 'ivory'
    star4.fill_color = 'ivory'
    window.add(star4, x=318, y=190)
    # star 15
    star5 = GOval(5, 5)
    star5.filled = True
    star5.color = 'ivory'
    star5.fill_color = 'ivory'
    window.add(star5, x=682, y=129)
    # star 16
    star6 = GOval(5, 5)
    star6.filled = True
    star6.color = 'white'
    star6.fill_color = 'white'
    window.add(star6, x=502, y=123)
    # star 17
    star7 = GOval(3, 3)
    star7.filled = True
    star7.color = 'white'
    star7.fill_color = 'white'
    window.add(star7, x=563, y=79)
    # star 18
    star8 = GOval(3, 3)
    star8.filled = True
    star8.color = 'floralwhite'
    star8.fill_color = 'floralwhite'
    window.add(star8, x=197, y=176)
    # star 19
    star9 = GOval(5, 5)
    star9.filled = True
    star9.color = 'ivory'
    star9.fill_color = 'ivory'
    window.add(star9, x=146, y=90)
    # star 20
    star10 = GOval(5, 5)
    star10.filled = True
    star10.color = 'white'
    star10.fill_color = 'white'
    window.add(star10, x=388, y=126)


def mountain():
    """
    The terrain of Taipei is basin, so creating mountains
    in the background is necessary.
    """
    # the reference point of mountains
    xm = -100
    ym = 345
    color = 'darkslategray'
    # mountain 1
    mountain11 = GArc(400, 280, 90, 270)
    mountain11.filled = True
    mountain11.color = color
    mountain11.fill_color = color
    window.add(mountain11, x=xm, y=ym - 140)
    mountain12 = GArc(300, 280, 180, 270)
    mountain12.filled = True
    mountain12.color = color
    mountain12.fill_color = color
    window.add(mountain12, x=xm + 50, y=ym - 140)
    # mountain 2
    mountain21 = GArc(400, 180, 90, 270)
    mountain21.filled = True
    mountain21.color = color
    mountain21.fill_color = color
    window.add(mountain21, x=xm + 250, y=ym - 90)
    mountain22 = GArc(300, 180, 180, 270)
    mountain22.filled = True
    mountain22.color = color
    mountain22.fill_color = color
    window.add(mountain22, x=xm + 300, y=ym - 90)
    # mountain 3
    mountain31 = GArc(400, 220, 90, 270)
    mountain31.filled = True
    mountain31.color = color
    mountain31.fill_color = color
    window.add(mountain31, x=xm + 500, y=ym - 110)
    mountain32 = GArc(400, 220, 180, 270)
    mountain32.filled = True
    mountain32.color = color
    mountain32.fill_color = color
    window.add(mountain32, x=xm + 500, y=ym - 110)


def taipei_101():
    """
    Taipei 101 is the iconic building of Taipei, so drawing the
    Taipei 101 in this picture is necessary.

    widths and heights of each component of the Taipei 101:
    width of the base: 52 and 36 pixels
    width of the 8 bodies: 36 and 32 pixels each
    width of the lower tower: 14 and 18 pixels
    width of the upper tower: 4 pixels
    total height of the Taipei 101: 336 (13.5x) pixels
    height of base: 76 (3x) pixels
    height of the 8 bodies: 25 (x) pixels each
    height of lower tower: 25 (x) pixels
    height of upper tower: 35 (1.5x) pixels
    """
    # the reference point of the Taipei 101
    xt = 600
    yt = 345
    color = 'midnightblue'
    #  the base of the Taipei 101
    base = GPolygon()
    base.add_vertex((xt, yt))
    base.add_vertex((xt+8, yt-76))
    base.add_vertex((xt+44, yt-76))
    base.add_vertex((xt+52, yt))
    base.filled = True
    base.color = color
    base.fill_color = color
    window.add(base, x=0, y=0)
    # the bamboo structure of the 8 bodies of the Taipei 101
    for i in range(1, 9):
        body = GPolygon()
        body.add_vertex((xt+10, yt-76-25*(i-1)))
        body.add_vertex((xt+6, yt-76-25*i))
        body.add_vertex((xt+46, yt-76-25*i))
        body.add_vertex((xt+42, yt-76-25*(i-1)))
        body.filled = True
        body.color = color
        body.fill_color = color
        window.add(body, x=0, y=0)
    # the lower tower of the Taipei 101
    l_tower = GPolygon()
    l_tower.add_vertex((xt+19, yt-276))
    l_tower.add_vertex((xt+17, yt-276-25))
    l_tower.add_vertex((xt+35, yt-276-25))
    l_tower.add_vertex((xt+33, yt-276))
    l_tower.filled = True
    l_tower.color = color
    l_tower.fill_color = color
    window.add(l_tower, x=0, y=0)
    # the upper tower of Taipei 101
    u_tower = GPolygon()
    u_tower.add_vertex((xt+24, yt-301))
    u_tower.add_vertex((xt+24, yt-301-35))
    u_tower.add_vertex((xt+28, yt-301-35))
    u_tower.add_vertex((xt+28, yt-301))
    u_tower.filled = True
    u_tower.color = color
    u_tower.fill_color = color
    window.add(u_tower, x=0, y=0)


def bg_building():
    """
    Create background buildings, with positions and heights of buildings
    generated randomly by the code random.randint(a,b) and tuned by creator
    to make them look better.
    """
    # the reference point of the background buildings
    xt = 0
    yt = 345
    color = 'midnightblue'
    skyscraper = GPolygon()
    # building 1
    skyscraper.add_vertex((xt, yt))
    skyscraper.add_vertex((xt, yt - 158))
    skyscraper.add_vertex((xt + 17, yt - 158))
    skyscraper.add_vertex((xt + 17, yt))
    # building 2
    skyscraper.add_vertex((xt + 41, yt))
    skyscraper.add_vertex((xt + 41, yt - 181))
    skyscraper.add_vertex((xt + 60, yt - 181))
    skyscraper.add_vertex((xt + 60, yt))
    # building 3
    skyscraper.add_vertex((xt + 60, yt))
    skyscraper.add_vertex((xt + 60, yt - 115))
    skyscraper.add_vertex((xt + 83, yt - 115))
    skyscraper.add_vertex((xt + 83, yt))
    # building 4
    skyscraper.add_vertex((xt + 88, yt))
    skyscraper.add_vertex((xt + 88, yt - 172))
    skyscraper.add_vertex((xt + 110, yt - 172))
    skyscraper.add_vertex((xt + 110, yt))
    # building 5
    skyscraper.add_vertex((xt + 133, yt))
    skyscraper.add_vertex((xt + 133, yt - 70))
    skyscraper.add_vertex((xt + 157, yt - 70))
    skyscraper.add_vertex((xt + 157, yt))
    # building 6
    skyscraper.add_vertex((xt + 169, yt))
    skyscraper.add_vertex((xt + 169, yt - 130))
    skyscraper.add_vertex((xt + 187, yt - 130))
    skyscraper.add_vertex((xt + 187, yt))
    # building 7
    skyscraper.add_vertex((xt + 195, yt))
    skyscraper.add_vertex((xt + 195, yt - 85))
    skyscraper.add_vertex((xt + 230, yt - 85))
    skyscraper.add_vertex((xt + 230, yt))
    # building 8
    skyscraper.add_vertex((xt + 254, yt))
    skyscraper.add_vertex((xt + 254, yt - 102))
    skyscraper.add_vertex((xt + 285, yt - 102))
    skyscraper.add_vertex((xt + 285, yt))
    # building 9
    skyscraper.add_vertex((xt + 306, yt))
    skyscraper.add_vertex((xt + 306, yt - 102))
    skyscraper.add_vertex((xt + 327, yt - 102))
    skyscraper.add_vertex((xt + 327, yt))
    # building 10
    skyscraper.add_vertex((xt + 348, yt))
    skyscraper.add_vertex((xt + 348, yt - 20))
    skyscraper.add_vertex((xt + 381, yt - 20))
    skyscraper.add_vertex((xt + 381, yt))
    # building 11
    skyscraper.add_vertex((xt + 397, yt))
    skyscraper.add_vertex((xt + 397, yt - 107))
    skyscraper.add_vertex((xt + 414, yt - 107))
    skyscraper.add_vertex((xt + 414, yt))
    # building 12
    skyscraper.add_vertex((xt + 414, yt))
    skyscraper.add_vertex((xt + 414, yt - 172))
    skyscraper.add_vertex((xt + 434, yt - 172))
    skyscraper.add_vertex((xt + 434, yt))
    # building 13
    skyscraper.add_vertex((xt + 453, yt))
    skyscraper.add_vertex((xt + 453, yt - 59))
    skyscraper.add_vertex((xt + 471, yt - 59))
    skyscraper.add_vertex((xt + 471, yt))
    # building 14
    skyscraper.add_vertex((xt + 481, yt))
    skyscraper.add_vertex((xt + 481, yt - 110))
    skyscraper.add_vertex((xt + 508, yt - 110))
    skyscraper.add_vertex((xt + 508, yt))
    # building 15
    skyscraper.add_vertex((xt + 521, yt))
    skyscraper.add_vertex((xt + 521, yt - 60))
    skyscraper.add_vertex((xt + 544, yt - 60))
    skyscraper.add_vertex((xt + 544, yt))
    # building 16
    skyscraper.add_vertex((xt + 549, yt))
    skyscraper.add_vertex((xt + 549, yt - 155))
    skyscraper.add_vertex((xt + 569, yt - 155))
    skyscraper.add_vertex((xt + 569, yt))
    # building 17
    skyscraper.add_vertex((xt + 569, yt))
    skyscraper.add_vertex((xt + 569, yt - 83))
    skyscraper.add_vertex((xt + 590, yt - 83))
    skyscraper.add_vertex((xt + 590, yt))
    # building 18
    skyscraper.add_vertex((xt + 609, yt))
    skyscraper.add_vertex((xt + 609, yt - 95))
    skyscraper.add_vertex((xt + 640, yt - 95))
    skyscraper.add_vertex((xt + 640, yt))
    # building 19
    skyscraper.add_vertex((xt + 659, yt))
    skyscraper.add_vertex((xt + 659, yt - 84))
    skyscraper.add_vertex((xt + 681, yt - 84))
    skyscraper.add_vertex((xt + 681, yt))
    # building 20
    skyscraper.add_vertex((xt + 699, yt))
    skyscraper.add_vertex((xt + 699, yt - 64))
    skyscraper.add_vertex((xt + 720, yt - 64))
    skyscraper.add_vertex((xt + 720, yt))
    skyscraper.filled = True
    skyscraper.color = color
    skyscraper.fill_color = color
    window.add(skyscraper, x=0, y=0)
    # ground
    ground = GRect(window.width, 60)
    ground.filled = True
    ground.color = color
    ground.fill_color = color
    window.add(ground, x=0, y=yt)


def f_building():
    """
    Create buildings closer to viewers, with positions and heights
    of buildings generated randomly by the code random.randint(a,b)
    and tuned by creator to make them look better.
    """
    # the reference point of the buildings
    xt = 0
    yt = 385
    color = 'black'
    skyscraper = GPolygon()
    # building 1
    skyscraper.add_vertex((xt + 9, yt))
    skyscraper.add_vertex((xt + 9, yt - 129))
    skyscraper.add_vertex((xt + 36, yt - 129))
    skyscraper.add_vertex((xt + 36, yt))
    # building 2
    skyscraper.add_vertex((xt + 46, yt))
    skyscraper.add_vertex((xt + 46, yt - 91))
    skyscraper.add_vertex((xt + 84, yt - 91))
    skyscraper.add_vertex((xt + 84, yt))
    # building 3
    skyscraper.add_vertex((xt + 90, yt))
    skyscraper.add_vertex((xt + 90, yt - 130))
    skyscraper.add_vertex((xt + 124, yt - 130))
    skyscraper.add_vertex((xt + 124, yt))
    # building 4
    skyscraper.add_vertex((xt + 143, yt))
    skyscraper.add_vertex((xt + 143, yt - 78))
    skyscraper.add_vertex((xt + 179, yt - 78))
    skyscraper.add_vertex((xt + 179, yt))
    # building 5
    skyscraper.add_vertex((xt + 186, yt))
    skyscraper.add_vertex((xt + 186, yt - 177))
    skyscraper.add_vertex((xt + 226, yt - 177))
    skyscraper.add_vertex((xt + 226, yt))
    # building 6
    skyscraper.add_vertex((xt + 246, yt))
    skyscraper.add_vertex((xt + 246, yt - 118))
    skyscraper.add_vertex((xt + 268, yt - 118))
    skyscraper.add_vertex((xt + 268, yt))
    # building 7
    skyscraper.add_vertex((xt + 277, yt))
    skyscraper.add_vertex((xt + 277, yt - 90))
    skyscraper.add_vertex((xt + 322, yt - 90))
    skyscraper.add_vertex((xt + 322, yt))
    # building 8
    skyscraper.add_vertex((xt + 334, yt))
    skyscraper.add_vertex((xt + 334, yt - 136))
    skyscraper.add_vertex((xt + 357, yt - 136))
    skyscraper.add_vertex((xt + 357, yt))
    # building 9
    skyscraper.add_vertex((xt + 376, yt))
    skyscraper.add_vertex((xt + 376, yt - 118))
    skyscraper.add_vertex((xt + 406, yt - 118))
    skyscraper.add_vertex((xt + 406, yt))
    # building 10
    skyscraper.add_vertex((xt + 421, yt))
    skyscraper.add_vertex((xt + 421, yt - 91))
    skyscraper.add_vertex((xt + 458, yt - 91))
    skyscraper.add_vertex((xt + 458, yt))
    # building 11
    skyscraper.add_vertex((xt + 477, yt))
    skyscraper.add_vertex((xt + 477, yt - 141))
    skyscraper.add_vertex((xt + 501, yt - 141))
    skyscraper.add_vertex((xt + 501, yt))
    # building 12
    skyscraper.add_vertex((xt + 518, yt))
    skyscraper.add_vertex((xt + 518, yt - 159))
    skyscraper.add_vertex((xt + 553, yt - 159))
    skyscraper.add_vertex((xt + 553, yt))
    # building 13
    skyscraper.add_vertex((xt + 563, yt))
    skyscraper.add_vertex((xt + 563, yt - 110))
    skyscraper.add_vertex((xt + 596, yt - 110))
    skyscraper.add_vertex((xt + 596, yt))
    # building 14
    skyscraper.add_vertex((xt + 606, yt))
    skyscraper.add_vertex((xt + 606, yt - 114))
    skyscraper.add_vertex((xt + 629, yt - 114))
    skyscraper.add_vertex((xt + 629, yt))
    # building 15
    skyscraper.add_vertex((xt + 645, yt))
    skyscraper.add_vertex((xt + 645, yt - 97))
    skyscraper.add_vertex((xt + 677, yt - 97))
    skyscraper.add_vertex((xt + 677, yt))
    # building 16
    skyscraper.add_vertex((xt + 686, yt))
    skyscraper.add_vertex((xt + 686, yt - 66))
    skyscraper.add_vertex((xt + 720, yt - 66))
    skyscraper.add_vertex((xt + 720, yt))
    skyscraper.filled = True
    skyscraper.color = color
    skyscraper.fill_color = color
    window.add(skyscraper, x=0, y=0)
    # ground
    ground = GRect(window.width, 20)
    ground.filled = True
    ground.color = color
    ground.fill_color = color
    window.add(ground, x=0, y=yt)
    """
    The heights of all windows of all buildings are all 2 pixels, but
    the width of each window of each building is different, based on
    the width of each building.
    """
    # window 1
    for i in range(16):
        for j in range(4):
            window_s = GRect(2, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 13 + 6 * j, y=yt - 5 - 8 * i)
    # window 2
    for i in range(11):
        window_s = GRect(30, 2)
        window_s.filled = True
        window_s.color = 'white'
        window_s.fill_color = 'white'
        window.add(window_s, x=xt + 50, y=yt - 6 - 8 * i)
    # window 3
    for i in range(16):
        for j in range(5):
            window_s = GRect(3, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 93 + 6 * j, y=yt - 5 - 8 * i)
    # window 4
    for i in range(9):
        for j in range(2):
            window_s = GRect(12, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 147 + 16 * j, y=yt - 8 - 8 * i)
    # window 5
    for i in range(22):
        for j in range(9):
            window_s = GRect(2, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 189 + 4 * j, y=yt - 4 - 8 * i)
    # window 6
    for i in range(14):
        window_s = GRect(14, 2)
        window_s.filled = True
        window_s.color = 'white'
        window_s.fill_color = 'white'
        window.add(window_s, x=xt + 250, y=yt - 8 - 8 * i)
    # window 7
    for i in range(11):
        for j in range(4):
            window_s = GRect(6, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 282 + 10 * j, y=yt - 5 - 8 * i)
    # window 8
    for i in range(17):
        for j in range(4):
            window_s = GRect(2, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 337 + 5 * j, y=yt - 4 - 8 * i)
    # window 9
    for i in range(14):
        window_s = GRect(22, 2)
        window_s.filled = True
        window_s.color = 'white'
        window_s.fill_color = 'white'
        window.add(window_s, x=xt + 380, y=yt - 8 - 8 * i)
    # window 10
    for i in range(11):
        for j in range(4):
            window_s = GRect(3, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 426 + 8 * j, y=yt - 5 - 8 * i)
    # window 11
    for i in range(17):
        for j in range(3):
            window_s = GRect(4, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 480 + 7 * j, y=yt - 8 - 8 * i)
    # window 12
    for i in range(19):
        for j in range(8):
            window_s = GRect(2, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 521 + 4 * j, y=yt - 9 - 8 * i)
    # window 13
    for i in range(13):
        window_s = GRect(23, 2)
        window_s.filled = True
        window_s.color = 'white'
        window_s.fill_color = 'white'
        window.add(window_s, x=xt + 568, y=yt - 8 - 8 * i)
    # window 14
    for i in range(14):
        for j in range(2):
            window_s = GRect(7, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 609 + 10 * j, y=yt - 4 - 8 * i)
    # window 15
    for i in range(12):
        for j in range(4):
            window_s = GRect(3, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 649 + 7 * j, y=yt - 5 - 8 * i)
    # window 16
    for i in range(8):
        for j in range(8):
            window_s = GRect(2, 2)
            window_s.filled = True
            window_s.color = 'white'
            window_s.fill_color = 'white'
            window.add(window_s, x=xt + 688 + 4 * j, y=yt - 6 - 8 * i)


def sign():
    """
    Sign my name "Ryan Kuo" on the bottom right of the picture.
    """
    name = GLabel('Ryan Kuo')
    name.font = '-8'
    name.color = 'white'
    window.add(name, x=670, y=400)


if __name__ == '__main__':
    main()
