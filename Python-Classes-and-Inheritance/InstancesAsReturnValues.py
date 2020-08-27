class Point():
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):  # tells how to print point object
        return "x = {}, y = {}".format(self.x, self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceFromOrigin(self):
        return ((self.x**2)+(self.y**2)**0.5)
    def halfway(self,target):
         mx = (self.x + target.x)/2
         my = (self.y + target.y)/2
         return Point(mx,my)
p = Point (3,4)
q = Point (5,12)

mid_pt = p.halfway(q) # should return a mid-point
print(mid_pt)
print(mid_pt.getX())
print(mid_pt.getY())
