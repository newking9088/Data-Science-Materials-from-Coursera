"""You have already seen that each instance of a class has its own namespace
with its own instance variables. Two instances of the Point class each have
their own instance variable x. Setting x in one instance doesn’t affect the
other instance. A class can also have class variables. A class variable is set
as part of the class definition. For example, consider the following version
of the Point class. Here we have added a graph method that generates a string
representing a little text-based graph with the Point plotted on the graph.
It’s not a very pretty graph, in part because the y-axis is stretched like a
rubber band, but you can get the idea from this. Note that there is an
assignment to the variable printed_rep on line 4. It is not inside any method.
That makes it a class variable. It is accessed in the same way as instance
variables. For example, on line 16, there is a reference to self.printed_rep.
If you change line 4, you have it print a different character at the
x,y coordinates of the Point in the graph.
When the interpreter sees an expression of the form <obj>.<varname>, it:
Checks if the object has an instance variable set. If so, it uses that value.
If it doesn’t find an instance variable, it checks whether the class has a
class variable. If so it uses that value.
If it doesn’t find an instance or a class variable, it creates a runtime error
(actually, it does one other check first, which you will
learn about in the next chapter.)
When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
Evaluates the expression on the right-hand side to yield some python object;
Sets the instance variable <varname> of <obj> to be bound to that python object.
Note that an assignment statement of this form never sets the class variable,
it only sets the instance variable"""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"   # class variable

    def __init__(self, initX, initY):   # __init__ is also a class variable

        self.x = initX  # self. x and self.y are instance variables
        self.y = initY

    def graph(self):   # graph is also a class variable
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)  # p1 is instance of our class Point
p2 = Point(3, 12) # p2 is instance of our class Point
print(p1.graph())
print()
print(p2.graph())
