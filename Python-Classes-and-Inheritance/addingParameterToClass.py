"""We can make our class constructor more generally usable by putting extra
parameters into the __init__ method, as shown in this example."""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

p = Point(7,6)

"""Create a class called NumberSet that accepts 2 integers as input, and defines
two instance variables: num1 and num2, which hold each of the input integers.
Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10.
Save this instance to a variable t."""
class NumberSet():    # parantheses is optional
    def __init__(self,num1,num2): # one of the special method in class
        self.num1 = num1
        self.num2 = num2
t = NumberSet (6, 10)

"""Let’s add another method, distanceFromOrigin, to see better how methods work.
This method will again not need any additional information to do its work,
beyond the data stored in the instance variables. It will perform a more
complex task."""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(7,6)
print(p.distanceFromOrigin())

"""Create a class called Animal that accepts two numbers as inputs and assigns
them respevtively to two instance variables: arms and legs. Create a class
method called limbs that, when called, returns the total number of limbs the
animal has. To the variable name spider, assign an instance of Animal that
has 4 arms and 4 legs. Call the limbs method on the spider instance and save
the result to the variable name spidlimbs."""
class Animal:
    def __init__(self, arms, legs):  # special dunder method
        self.arms = arms
        self.legs = legs
    def limbs(self):                 # method in Animal class
        return ( self.arms + self.legs )
spider = Animal ( 4, 4 )
spidlimbs = spider.limbs()
    
        
