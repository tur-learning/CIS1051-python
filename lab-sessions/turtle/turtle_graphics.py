import sys
from svg_turtle import SvgTurtle

width=500; height=500; side_length=150

bob = SvgTurtle(width, height)

def draw():
    bob.hideturtle()
    bob.pencolor("black")
    bob.speed("fastest")
    shape()
    return bob

def shape():
    bob.penup()
    bob.goto(-side_length/2, side_length/2)
    bob.pendown()
    for _ in range(2):
        bob.forward(side_length)
        bob.right(90)
        bob.forward(side_length * height / width)
        bob.right(90)

turtle = draw()
turtle.save_as(sys.argv[1])