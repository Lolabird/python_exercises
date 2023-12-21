import turtle
import random


def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2, delta):
    return ( (((p1[0]+p2[0]) / 2) + random.uniform(-delta, delta)), 
            (((p1[1] + p2[1]) / 2) + random.uniform(-delta, delta)))


def fractalMnt(points,degree,myTurtle):
    colormap = ['floralwhite','brown','darkgoldenrod','olive','maroon']
    
    drawTriangle(points,colormap[degree],myTurtle)

    if degree > 0:
        mid1 = getMid(points[0], points[1], 10)
        mid2 = getMid(points[0], points[2], 10)
        mid3 = getMid(points[1], points[2], 10)

        fractalMnt([points[0], mid1, mid2], degree-1, myTurtle)
        fractalMnt([points[1], mid1, mid3], degree-1, myTurtle)
        fractalMnt([points[2], mid3, mid2], degree-1, myTurtle)
        fractalMnt([mid1, mid3, mid2], degree-1, myTurtle)
        

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   fractalMnt(myPoints,4,myTurtle)
   myWin.exitonclick()

main()
