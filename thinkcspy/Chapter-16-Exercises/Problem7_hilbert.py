# Runestone.Academy thinkcspy course
# Chapter 16
# Problem 7

import turtle

def createLSystem(numIters, axiom):
    if numIters == 0:
        return axiom
    else:
        return createLSystem(numIters - 1, processString(axiom))


def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr


def applyRules(ch):
    newstr = ""
    if ch == 'A':
        newstr = '-BF+AFA+FB-'   # Rule 1
    elif ch == 'B':
        newstr = '+AF-BFB-FA+'
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr


def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == '+':
            aTurtle.left(angle)
        elif cmd == '-':
            aTurtle.right(angle)


def main():
    inst = createLSystem(4, "A")
    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 90, 5)

    wn.exitonclick()


main()