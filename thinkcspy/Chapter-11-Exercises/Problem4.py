# Runestone.Academy thinkcspy course
# Chapter 11
# Problem 4

import turtle
    
def slope():
    xlist = []
    ylist = []
    sumx = 0
    sumy = 0
    sumxy = 0
    sumxsq = 0
    count = 0     #n
    meanx = 0
    meany = 0
    slope = 0     #m
        
    with open('labdata.txt') as lab:
        for line in lab:
            values = line.split()
            xlist += [int(values[0])]
            ylist += [int(values[1])]
            x = int(values[0])
            y = int(values[1])
            sumx += x
            sumy += y
            sumxy += x*y
            sumxsq += x**2
            count += 1

    meanx = sumx / count
    meany = sumy / count
    
    slope = (sumxy - count*meanx*meany) / (sumxsq - count*meanx**2)
        
    plotRegression(xlist, ylist, meanx, meany, slope)
    
    
    
def plotRegression(xlist, ylist, meanx, meany, slope):
    #set world coordinates
    minx = xlist[0]
    miny = ylist[0]
    maxx = xlist[0]
    maxy = ylist[0]
    count = len(xlist)
    num = 0
    
    while num < count:
        if xlist[num] < minx:
            minx = xlist[num]
        if xlist[num] > maxx:
            maxx = xlist[num]
        if ylist[num] < miny:
            miny = ylist[num]
        if ylist[num] > maxy:
            maxy = ylist[num]
            
        num += 1
        
    turtle.setworldcoordinates(minx-10, miny-10, maxx+10, maxy+10)
    
    #plot points
    i = 0 
    wn = turtle.Screen()
    wn.bgcolor("#222")
    ella = turtle.Turtle() #points from the labdata.txt
    ella.color("pink")
    maya = turtle.Turtle() #line of best fit (yplot)
    maya.color("lightblue")
            
    for x in xlist:
        j = 0
        yplot = meany + slope*(x - meanx)
        
        while not j:
            ella.up()
            ella.goto(x, ylist[i])
            ella.dot()
            
            if i != 0:
                maya.goto(x, yplot)
            else:
                maya.up()
                maya.goto(x, yplot)
                maya.down()
                
            j += 1
        
        i += 1   

    wn.exitonclick()
    
slope()