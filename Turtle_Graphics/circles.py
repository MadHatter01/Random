import turtle
import random


def colorGen():
    return "#{:06x}".format(random.randint(0, 9999999))


def concentricCircles(turtObj):
    turtObj.right(90)
    turtObj.forward(i)
    turtObj.right(270)
    turtObj.pendown()
    turtObj.circle(i)


dodo = turtle.Turtle()
dodo.penup()
turtle.bgcolor('black')
dodo.setpos(0, 0)

for i in range(200, 0, -20):
    color = colorGen()
    dodo.color(color)
    dodo.begin_fill()
    concentricCircles(dodo)
    dodo.end_fill()
    dodo.penup()
    dodo.home()
