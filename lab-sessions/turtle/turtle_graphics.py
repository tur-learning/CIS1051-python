from random import randint
from svg_turtle import SvgTurtle

def draw_rectangle(bob, width, height, side_length):
    bob.penup()
    bob.goto(-side_length/2, side_length/2)
    bob.pendown()
    for _ in range(2):
        bob.forward(side_length)
        bob.right(90)
        bob.forward(side_length * height / width)
        bob.right(90)

def rectangle(bob, width, height, side_length):
    bob.hideturtle()
    bob.pencolor("black")
    bob.speed("fastest")
    draw_rectangle(bob, width, height, side_length)

def write_file(rectangle, filename, width, height, side_length):
    bob = SvgTurtle(width, height)
    rectangle(bob, width, height, side_length)
    bob.save_as(filename)
