# Runestone.Academy thinkcspy course
# Chapter 11
# Problem 5

import turtle

def getMinMax():
    #get world coordinates
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0

    with open('mystery.txt') as data:
        for line in data:
            values = line.split()
            if values[0] != "UP" and values[0] != "DOWN": 
                minx = int(values[0])
                miny = int(values[1])
                maxx = int(values[0])
                maxy = int(values[1]) 
            break
                
        for line in data:
            values = line.split()
            if values[0] != "UP" and values[0] != "DOWN":
                if int(values[0]) < minx:
                    minx = int(values[0])
                if int(values[0]) > maxx:
                    maxx = int(values[0])
                if int(values[1]) < miny:
                    miny = int(values[1])
                if int(values[1]) > maxy:
                    maxy = int(values[1])

    draw(minx, miny, maxx, maxy)
        
        
        
def draw(minx, miny, maxx, maxy):    
    turtle.setworldcoordinates(minx-10, miny-10, maxx+10, maxy+10)
    
    wn = turtle.Screen()
    wn.bgcolor("#e0e0e0")
    ella = turtle.Turtle()
    ella.color("brown")
    
    with open('mystery.txt') as data:
        for line in data:
            values = line.split()
            
            if values[0] == "UP":
                ella.up()
            elif values[0] == "DOWN":
                ella.down()
            else:
                x = int(values[0])
                y = int(values[1])
                ella.goto(x,y)

getMinMax()