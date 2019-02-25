import turtle
import random


def colorGen():
    return "#{:06x}".format(random.randint(0, 9999999))


def starGen(turtObj):
    turtObj.forward(300)
    turtObj.right(136)


turtle.bgcolor('black')
twinkle = turtle.Turtle()
twinkle.penup()
for i in range(100):
    color = colorGen()
    twinkle.pencolor(color)
    twinkle.width(i/100 + 1)
    twinkle.pendown()
    starGen(twinkle)
    twinkle.penup()
    twinkle.forward(i)
