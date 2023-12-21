import turtle
import random

def stackTowers(num): 
    A = []
    B = []
    C = []
    rounds = 0

    
    for i in range(num):
        A.insert(0, i+1)
        

    def hanoi(num, start, aux, end):
        nonlocal rounds  
        
        if num == 1:
            end += [start.pop()]
            rounds += 1
            print(rounds, A, B, C)
        else:
            hanoi(num - 1, start, end, aux)
            end += [start.pop()]
            rounds += 1
            print(rounds, A, B, C)
            hanoi(num -1, aux, start, end)
   
    hanoi(num, A, B, C) 


def createRods(t):
    for i in range(3):
        t.penup()
        t.goto(100*i, 100)
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

    for i in range(num):
        newTurt = turtle.Turtle()
        newTurt.shape("square")
        newTurt.shapesize((i+1)/2, (i+1)*2, 1)
        newTurt.color(generateColor())
        newTurt.goto(0, i*-15)
        turtles.append(newTurt)

    return(turtle)

def moveTurtles():
    pass


def main():
    num = 7
    tRod = turtle.Turtle()
    tRod.pensize(5)
    turts = createTurtles(num)
    wn = turtle.Screen()

    createRods(tRod)
    stackTowers(num)

    wn.exitonclick()

main()