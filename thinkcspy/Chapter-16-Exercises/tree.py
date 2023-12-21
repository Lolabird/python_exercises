import turtle
import random

def color(branchlen, t):
    t.pensize(branchlen/5)
    if branchlen < 15:
        t.color("green")
    else:
        t.color("brown")


def getAngle():
    return random.randrange(15, 46)


def getLen(t):
    return random.randrange(5, 15)
  

def tree(branchLen,t):
    if branchLen > 5:
        color(branchLen, t)
        t.forward(branchLen)
        angle = getAngle()
        t.right(angle)
        tree(branchLen-getLen(t),t)
        t.left(angle * 2)
        tree(branchLen-getLen(t),t)
        t.right(angle)
        t.backward(branchLen)
        t.color("brown")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.speed(10)
    t.pensize(5)
    tree(75,t)
    myWin.exitonclick()

main()


