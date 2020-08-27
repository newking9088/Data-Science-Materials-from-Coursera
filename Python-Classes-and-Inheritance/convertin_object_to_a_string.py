"""Create a class called Cereal that accepts three inputs: 2 strings and 1
integer, and assigns them to 3 instance variables in the constructor: name,
brand, and fiber. When an instance of Cereal is printed, the user should see
the following: “[name] cereal is produced by [brand] and has [fiber integer]
grams of fiber in every serving!” To the variable name c1, assign an instance
of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2.
To the variable name c2, assign an instance of Cereal whose name is
"Honey Nut Cheerios", brand is "General Mills", and fiber is 3.
Practice printing both!"""

class Cereal():
    def __init__ (self, name, brand, fiber):
        self.n = name
        self.b = brand
        self.f = fiber
    def getname(self):
        return self.n
    def getbrand(self):
        return self.b
    def getfiber(self):
        return self.f
    def __str__(self):
        return '{} cereal is produced by {} and has {} grams\
 of fiber in every serving!'\
    .format(self.n, self.b, self.f)

c1 = Cereal ("Corn Flakes", "Kellogg's", 2)
c2 = Cereal ("Honey Nut Cheerios", "General Mills", 3)
print(c1)
print(c2)
