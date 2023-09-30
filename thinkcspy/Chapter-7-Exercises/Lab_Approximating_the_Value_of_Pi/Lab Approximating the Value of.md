# Lab: Approximating the Value of Pi
In this lab, our task was to simulate throwing darts at a 2x2 board, count how many landed in the circle out of the total amount and then approximate pi based on that. 

This is the code they started me off with:

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 7
# Lab

import turtle
import math
import random

fred = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

fred.up()

numdarts = 10
for i in range(numdarts):
    randx = random.random()
    randy = random.random()

    x =
    y =

wn.exitonclick()
```

My additions and changes to the above code:

```text-x-python
# Runestone.Academy thinkcspy course
# Chapter 7
# Lab

import turtle
#import math
import random


fred = turtle.Turtle()
clara = turtle.Turtle()

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)
wn.bgcolor("tan")
wn.tracer(100)

clara.dot()
print(clara.pos())
clara.up()
clara.goto(0,1)
clara.down()
clara.circle(-1)
print(clara.pos())
print(clara.distance(0.0,0.0))

fred.up()

numdarts = 100000
insideCount = 0

for i in range(numdarts):
    randx = random.random()*2-1
    randy = random.random()*2-1
    
    fred.goto(randx,randy)
    dist = fred.distance(0.0, 0.0)
        
    if dist < 1:
        color = "red"
        insideCount += 1
        place = "in"
    else:
        color = "blue"
        place = "out"
   
    fred.down()
    fred.dot(10,color)
    fred.up()


mypi = 4 * (insideCount / numdarts)
print(insideCount,"out of", numdarts, "darts made it into the circle.")    
print("The value of Pi based on the numbers number of darts that made it into the circle is", mypi, ".")

wn.exitonclick()
```

Result:

![](Lab%20Approximating%20the%20Value%20of%20Pi/image.png)

Order really does matter.. My first solution to this lab was mostly fine, except that the dots were being colored wrong. Some dots inside the circle were blue and some outside the circle were red. It was supposed to be the other way around. 

Initially I had fred go to his position after the if else block, but the problem was, the distance was being measured _before_ he moved. So distance was based on the previous loop's coordinates and coloring the darts based on those rather than the current loop's points. It took me a minute but I finally figured out that I needed to position fred _before_ measuring the distance between fred's current position and the center.