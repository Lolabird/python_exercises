import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distanceFromPoint(self, pnt):
        dx = self.x - pnt.getX()
        dy = self.y - pnt.getY()
        
        return math.sqrt(dx**2 +dy**2)

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

p = Point(7, 6)
q = Point(10, 3)
print(p.distanceFromPoint(q))
