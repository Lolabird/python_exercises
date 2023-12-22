import turtle
import random

def stackTowers(num, turts): 
    A = []
    B = []
    C = []
    rounds = 0
    rods = {"A":A, "B":B, "C":C}
    
    for i in range(num):
        A.insert(0, i+1)
        

    def hanoi(num, start, aux, end, turts):
        nonlocal rounds  
        
        if num == 1:
            end += [start.pop()]
            rounds += 1
            moveTurtles(turts[end[-1] - 1], rods)
        else:
            hanoi(num - 1, start, end, aux, turts)
            end += [start.pop()]
            rounds += 1
            moveTurtles(turts[end[-1] - 1], rods)
            hanoi(num -1, aux, start, end, turts)
   
    hanoi(num, A, B, C, turts) 


def createRods(t):
    for i in range(3):
        t.penup()
        t.goto(300*(i-1), 100)
        t.pendown()
        t.right(90)
        t.forward(200)
        t.left(90)

def generateColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    hexColor = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hexColor


def createTurtles(num):
    turtles = []

    totalHeight = num*15

    for i in range(num):
        newTurt = turtle.Turtle()
        newTurt.shape("square")
        newTurt.shapesize(1/2, (i+1)*2, 1)
        newTurt.color(generateColor())
        newTurt.penup()
        newTurt.goto(-300, (num*15 - 100) - i*15)
        newTurt.name = str(i+1)

        turtles.append(newTurt)

    return turtles

def moveTurtles(turt, rods):
    rodPos = {"A":-300, "B":0, "C":300}
    x = turt.xcor()
    y = turt.ycor()

    for rods, turtList in rods.items():
        if int(turt.name) in turtList:
            x = rodPos[rods]
            y = len(turtList) * 15 - 100

    turt.goto(x, y)


def main():
    num = 8
    tRod = turtle.Turtle()
    tRod.pensize(5)
    wn = turtle.Screen()

    createRods(tRod)
    turts = createTurtles(num)
    stackTowers(num, turts)

    wn.exitonclick()

main()