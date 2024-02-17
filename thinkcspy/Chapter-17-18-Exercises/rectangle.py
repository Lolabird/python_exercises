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
    r2Arr = r2.getCoords()
    r1Arr = r1.getCoords()

    # Compare widths and heights
    if r2.width > r1.width:
        if r1Arr[0] in range(r2Arr[0], r2Arr[2] + 1) or r1Arr[2] in range(r2Arr[0], r2Arr[2] + 1):
            conditionW = True
    elif r2Arr[0] in range(r1Arr[0], r1Arr[2] + 1) or r2Arr[2] in range(r1Arr[0], r1Arr[2] + 1):
        conditionW = True
            
    if r2.height > r1.height:
        if r1Arr[1] in range(r2Arr[1], r2Arr[3] + 1) or r1Arr[3] in range(r2Arr[1], r2Arr[3] + 1):
            conditionH = True
    elif r2Arr[1] in range(r1Arr[1], r1Arr[3] + 1) or r2Arr[3] in range(r1Arr[1], r1Arr[3] + 1):
        conditionH = True

    if conditionW and conditionH:
        return "Collission!"

    return "All safe for now."


r = Rectangle(Point(-23, 25), 100, 50)
s = Rectangle(Point(10, 27), 10, 4)

print(collission(r, s))