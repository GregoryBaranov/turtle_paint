from turtle import *


t = Turtle()
t.color("blue")
t.width(5)
t.w = 5
t.shape("circle")
t.pendown()
t.speed(100)


def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def setGreen():
    t.color("green")
def setRed():
    t.color("red")
def erase():
    t.color("white")
    t.width(15)
def stepRight():
    t.goto(t.xcor() + 5, t.ycor())
def stepLeft():
    t.goto(t.xcor() - 5, t.ycor())
def stepUp():
    t.goto(t.xcor() , t.ycor() + 5)
def stepDown():
    t.goto(t.xcor() , t.ycor() - 5)

def setBold():
    t.w +=5
    t.width(t.w)


def setLessBold():
    t.w -=5
    t.width(t.w)

scr = t.getscreen()
scr.listen()
scr.onkey(setGreen, "g")
scr.onkey(setRed, "r")
scr.onkey(erase, "e")
scr.onkey(stepRight, "Right")
scr.onkey(stepLeft, "Left")
scr.onkey(stepUp, "Up")
scr.onkey(stepDown, "Down")
scr.onkey(setBold, "b")
scr.onkey(setLessBold, "v")
scr.onscreenclick(move)

t.ondrag(draw)
