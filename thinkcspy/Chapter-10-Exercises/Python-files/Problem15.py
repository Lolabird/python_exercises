# Runestone.Academy thinkcspy course
# Chapter 10
# Problem 15

import turtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'H':
        newstr = 'HFX[+H][-H]'   # Rule 1
    elif ch == 'X':
        newstr = 'X[-FFF][+FFF]FX'   # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            savedInfoList.append([aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()])
            print(savedInfoList)
        elif cmd == ']':
            newInfo = savedInfoList.pop()
            aTurtle.setheading(newInfo[0])
            aTurtle.setposition(newInfo[1], newInfo[2])

def main():
    inst = createLSystem(6, "H")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()
    wn.tracer(10)

    t.up()
    t.back(200)
    t.down()
    t.speed(0)
    drawLsystem(t, inst, 25.7, 5)   # draw the picture
                                  # angle 2, segment length 5
    wn.exitonclick()

main()