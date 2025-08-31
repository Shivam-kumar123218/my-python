from turtle import *
from colorsys import *
tracer(10)
bgcolor("black")
pensize(1)
h = 0
goto(0,20)
def draw(ang, n):
    circle(5+n, 60)
    left(ang)
    circle(5+n*2, 60)
    for i in range(200):
        color(hsv_to_rgb(h, 1, 1))
        h += 0.0062
        up()
        draw(90, i)
        draw(180 , 0)
        down()
        draw(1/2,0)
        draw(180, i/2)
        draw(120,0)
        draw(1/2, 0)
        draw(120,0)
    hideturtle()
    done()    

