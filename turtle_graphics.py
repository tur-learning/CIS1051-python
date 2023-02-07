import sys
from svg_turtle import SvgTurtle
import mypolygon

width=500; height=500; side_length=150

bob = SvgTurtle(width, height)

#mypolygon.square(bob)
#mypolygon.square2(bob, 150)
#mypolygon.polygon(bob, 50, 8)
#mypolygon.circle(bob, 50)
#mypolygon.circle(bob, 100)
#mypolygon.circle(bob, 150)
mypolygon.arc(bob, 50, 180)
mypolygon.arc(bob, 100, 360)



bob.save_as(sys.argv[1])

print(bob)
