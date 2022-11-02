import random
from turtle import *
import colorgram


def line_of_dots(thing, length, number, colors):
    for x in range(length):
        y = random.randint(1, number - 1)
        # randint starting at 1 because first color is usually off white
        thing.pencolor(colors[y])
        thing.forward(0)
        thing.penup()
        thing.forward(50)
        thing.pendown()


def turn(thing, l_or_r, number, colors):
    thing.seth(90)
    y = random.randint(1, number - 1)
    thing.pencolor(colors[y])
    thing.forward(0)
    thing.penup()
    thing.forward(50)
    thing.pendown()
    if l_or_r % 2 == 0:
        thing.seth(180)
    else:
        thing.seth(0)


number_of_colors = 12
colors2 = []

for _ in range(number_of_colors):
    colors1 = colorgram.extract('kirby.png', number_of_colors)
    # you can change the picture the colors are being extracted from here
    colors2.append(colors1[_].rgb)
    # converting whatever colorgram gives into a list of tuples in the (r, g, b) format

timmy = Turtle()
my_screen = Screen()
my_screen.colormode(255)

timmy.speed(0)
timmy.ht()
# hides the cursor
timmy.pensize(20)
# size of dot
timmy.penup()
timmy.setpos(-400, -360)
# starting position
timmy.pendown()

dots_per_line = 16

for i in range(dots_per_line):
    line_of_dots(timmy, dots_per_line, number_of_colors, colors2)
    turn(timmy, i, number_of_colors, colors2)

my_screen.exitonclick()
