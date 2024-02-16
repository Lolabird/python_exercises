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
    

r = Rectangle(Point(4, 5), 6, 5)
print(r)
    