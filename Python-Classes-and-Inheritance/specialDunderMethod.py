class Point():
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):  # tells how to print point object
        return "Point ({},{})".format(self.x, self.y)
    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x,
                     self.y + otherPoint.y)
    def __subtract__(self, otherPoint):
        return Point(self.x - otherPoint.x,
                     self.y - otherPoint.y)
p1 = Point(-5,10)
p2 = Point(10,20)
print(p1)
print(p2)
print(p1+p2)   # p1 is passsed to self & p2 to otherPoint
print(p1-p2)
