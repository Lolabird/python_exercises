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
        
        return math.sqrt(dx**2 + dy**2)
    
    def reflect_x(self):
        return (self.x, -self.y)
    
    def slopeFromOrigin(self):
        return self.y / self.x
    
    def slopeIntercept(self, pnt):
        dx = self.x - pnt.getX()
        dy = self.y - pnt.getY()
        
        # Accounting for points of failure (divide by 0)
        if dx == 0:
            if dy == 0:
                return "Cannot calculate slope of a single point."
            else:
                return "Cannot calculate slope of a vertical line."
        
        m = dy / dx
        b = self.y - m*self.x
        
        return (m, b)
    
    def move(self, pnt):
        self.x += pnt.getX()
        self.y += pnt.getY()
        
        return (self.x, self.y)

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

p = Point(7, 6)
q = Point(10, 3)
print(p.move(q))
