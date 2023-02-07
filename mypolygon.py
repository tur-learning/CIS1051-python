from svg_turtle import SvgTurtle
import math

width=500; height=500; side_length=150

# Problem 1
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# Problem 2
def square2(t, length=100):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# Problem 3
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

# Problem 4
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

# Problem 5
def arc(t, r, angle):
    radius = 2 * math.pi * r
    arc_length = radius * (angle/360)
    n_segments = int(arc_length / 3) + 1

    for i in range(n_segments):
        t.fd(arc_length / n_segments)
        t.lt(angle / n_segments)
