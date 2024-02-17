from points import Point

class Rectangle:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
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
        lowerX = self.pos.getX()
        upperX = lowerX + self.width
        lowerY = self.pos.getY()
        upperY = lowerY + self.height
        pntX = pnt.getX()
        pntY = pnt.getY()

        if lowerX == upperX or lowerY == upperY:
            return "Error: Rectangle not defined."

        if lowerX > upperX:
            lowerX = upperX
            upperX = self.pos.getX()

        if lowerY > upperY:
            lowerY = upperY
            upperY = self.pos.getY()

        if pntX > lowerX and pntX < upperX and pntY > lowerY and pntY < upperY:
            return True

        return False
    
    def diagonal(self):
        pnt = Point(self.width, self.height)
        return pnt.distanceFromOrigin()

r = Rectangle(Point(-10, 5), 4, 30)
#print(r)
print(r.diagonal())
    