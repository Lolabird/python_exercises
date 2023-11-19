import turtle

def countAll(text):
    wordDict = {}
    text = text.lower()

    for char in text:
        if char not in wordDict and char.isalpha():
            wordDict[char] = text.count(char)
    
    return wordDict

def sortList(text):
    wordDict = countAll(text)
    alphaList = list(wordDict.items())
    alphaList.sort()
    
    return alphaList
    
    
def writeData(tt, letter, height):
    tt.up()
    tt.left(90)
    tt.forward(height+1)
    tt.right(90)
    tt.forward(10)
    tt.write(letter + ": " + str(height), font=("arial",20))
    tt.forward(30)
    tt.right(90)
    tt.forward(height+1)
    tt.left(90)
    

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def getMaxheight(htList):
    maxht = 0

    for item in htList:
        if item[1] > maxht:
            maxht = item[1]
    
    return maxht


xs = sortList(input("What word(s) would you like sorted?"))
maxheight = getMaxheight(xs)
numbars = len(xs)
border = 2

wn = turtle.Screen()
wn.setworldcoordinates(0, 0, 40*numbars+border, maxheight+border)
wn.bgcolor("darkslategrey")

tess = turtle.Turtle()
tess.color("thistle")
tess.fillcolor("maroon")

alex = turtle.Turtle()
alex.color("thistle")


for a in xs:
    drawBar(tess, a[1])
    writeData(alex, a[0], a[1])

wn.exitonclick()

