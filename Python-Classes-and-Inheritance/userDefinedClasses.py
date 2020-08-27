"""Now that we understand what a point object might look like, we can define a
new class. We’ll want our points to each have an x and a y attribute, so our
first class definition looks like this."""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):

        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happened with the points")

"""The following program adds a few print statements. You can see that the
output suggests that each one is a Point object. However, notice that the
is operator returns False meaning that they are different objects (we will
have more to say about this in a later section)."""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):

        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)

print(p is q)
