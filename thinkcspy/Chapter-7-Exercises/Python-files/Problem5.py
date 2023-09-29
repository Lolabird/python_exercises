# Runestone.Academy thinkcspy course
# Chapter 7
# Problem 5	

import turtle

def getColor(tf, tw, height):
    if height >= 200:
        tf.fillcolor("red")
    elif height >= 100:
        tf.fillcolor("yellow")
    else:
        tf.fillcolor("green")

def writeData(tt, height):
    if height < 0:
        writeHeight = 0
    else:
        writeHeight = height
  
    tt.up()
    tt.left(90)
    tt.forward(writeHeight+10)
    tt.right(90)
    tt.forward(10)
    tt.write(str(height))
    tt.forward(30)
    tt.right(90)
    tt.forward(writeHeight+10)
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



xs = [48, 117, -200, 240, 160, -260, 220]  # here is the data
maxheight = max(xs)+10
minheight = min(xs)-10
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0+minheight, 40*numbars+border, maxheight+border)
wn.bgcolor("lightblue")
wn.tracer(100)

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("black")
tess.pensize(3)

alex = turtle.Turtle()

for a in xs:
    getColor(tess, alex, a)
    drawBar(tess, a)
    writeData(alex, a)
    

wn.exitonclick()