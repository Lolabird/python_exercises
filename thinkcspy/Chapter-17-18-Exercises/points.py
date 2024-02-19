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
                return "Error: Cannot calculate slope of a single point."
            else:
                return "Error: Cannot calculate slope of a vertical line."
        
        m = dy / dx
        b = self.y - m*self.x
        
        return (m, b)
    
    def getMid(self, pnt):
        midX = (self.x + pnt.getX()) / 2
        midY = (self.y + pnt.getY()) / 2
        
        return (midX, midY) 
    
    def findCenterRadius(self, pnt1, pnt2):
        m1, b1 = self.slopeIntercept(pnt1)
        m2, b2 = self.slopeIntercept(pnt2)
        
        if m1 == m2 and b1 == b2:
            return "Error: Points are on the same line."
        
        mid1X, mid1Y = self.getMid(pnt1)
        mid2X, mid2Y = self.getMid(pnt2)
        center = Point(mid1X, mid1Y).getMid(Point(mid2X, mid2Y))
        
        r = self.distanceFromPoint(Point(center[0], center[1]))
        
        return "Circumcenter: {}; Radius: {}".format(center, r)
        
    def move(self, pnt):
        self.x += pnt.getX()
        self.y += pnt.getY()
        
        return (self.x, self.y)

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
