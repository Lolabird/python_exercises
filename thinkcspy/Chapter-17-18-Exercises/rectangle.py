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


r = Rectangle(Point(0, 0), 10, 5)
print(r)
print(r.transpose())
    