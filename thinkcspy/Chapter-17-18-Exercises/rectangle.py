from points import Point

class Rectangle:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height

        self.lowerX = self.pos.getX()
        self.upperX = self.lowerX + self.width
        self.lowerY = self.pos.getY()
        self.upperY = self.lowerY + self.height

        if self.lowerX == self.upperX or self.lowerY == self.upperY:
            return "Error: Rectangle not defined."

        if self.lowerX > self.upperX:
            self.lowerX = self.upperX
            self.upperX = self.pos.getX()

        if self.lowerY > self.upperY:
            self.lowerY = self.upperY
            self.upperY = self.pos.getY()

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
        pntX = pnt.getX()
        pntY = pnt.getY()

        if pntX > self.lowerX and pntX < self.upperX and pntY > self.lowerY and pntY < self.upperY:
            return True

        return False
    
    def diagonal(self):
        pnt = Point(self.width, self.height)
        return pnt.distanceFromOrigin()
    
    def collission(self, pnt):
        pntX = pnt.getX()
        pntY = pnt.getY()

        if (pntX > self.lowerX and pntX < self.upperX) or (pntY > self.lowerY and pntY < self.upperY):
            return True

        return False

r = Rectangle(Point(-10, 5), 4, 30)
#print(r)
print(r.collission(Point(10, 25)))
print(r.contains(Point(10, 25)))
    