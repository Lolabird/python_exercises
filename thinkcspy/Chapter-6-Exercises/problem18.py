# Runestone.Academy thinkcspy course
# Chapter 6
# Problem 18	

import turtle

def writeData(tt, height):
    tt.up()
    tt.left(90)
    tt.forward(height+10)
    tt.right(90)
    tt.forward(10)
    tt.write(str(height))
    tt.forward(30)
    tt.right(90)
    tt.forward(height+10)
    tt.left(90)
    

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)+10
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightblue")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("purple")
tess.fillcolor("magenta")
tess.pensize(3)

alex = turtle.Turtle()
alex.color("magenta")


for a in xs:
    drawBar(tess, a)
    writeData(alex, a)

wn.exitonclick()
