from points import Point

class Rectangle:
    def __init__(self, pos, width, height):
        self.pos = pos
        if width < 0:
            width = 0
        if height < 0:
            height = 0

        self.width = width
        self.height = height

        self.lowerX = self.pos.getX()
        self.upperX = self.lowerX + self.width
        self.lowerY = self.pos.getY()
        self.upperY = self.lowerY + self.height

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getCoords(self):
        return [self.lowerX, self.lowerY, self.upperX, self.upperY]
    
    def __str__(self):
        return "Lower Left Coordinates: {}; Width: {}; Height: {}".format(self.pos, self.width, self.height)
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width * 2 + self.height * 2

    def transpose(self):
        width = self.width
        self.width = self.height
        self.height = width

        return self
    
    def contains(self, pnt):
        pntX = pnt.getX()
        pntY = pnt.getY()

        if pntX > self.lowerX and pntX < self.upperX and pntY > self.lowerY and pntY < self.upperY:
            return True

        return False
    
    def diagonal(self):
        pnt = Point(self.width, self.height)
        return pnt.distanceFromOrigin()
    
    
def collission(r1, r2):
    conditionW = False
    conditionH = False
    bigR = r1
    lilR = r2

    if r1.area() < r2.area():
        bigR = r2
        lilR = r1

    lilArr = lilR.getCoords()
    bigArr = bigR.getCoords()

    # Compare widths and heights
    if lilR.width > bigR.width:
        if bigArr[0] in range(lilArr[0], lilArr[2] + 1) or bigArr[2] in range(lilArr[0], lilArr[2] + 1):
            conditionW = True
    elif lilArr[0] in range(bigArr[0], bigArr[2] + 1) or lilArr[2] in range(bigArr[0], bigArr[2] + 1):
        conditionW = True
            
    if lilR.height > bigR.height:
        if bigArr[1] in range(lilArr[1], lilArr[3] + 1) or bigArr[3] in range(lilArr[1], lilArr[3] + 1):
            conditionH = True
    elif lilArr[1] in range(bigArr[1], bigArr[3] + 1) or lilArr[3] in range(bigArr[1], bigArr[3] + 1):
        conditionH = True

    if conditionW and conditionH:
        return "Collission!"

    return "All safe for now."


r = Rectangle(Point(10, 25), 10, 0)
s = Rectangle(Point(10, 20), 10, 4)
# print(r)
# print(r.collission(Point(10, 25)))
# print(r.contains(Point(10, 25)))

print(collission(r, s))