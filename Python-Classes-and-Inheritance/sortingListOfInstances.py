class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def sort_priority(self):
        return self.price
L = [
    Fruit("Cherry",10),
    Fruit("Apple", 5),
    Fruit("Blueberry",20)
]
# tell how to sort for sorted method in list
for f in sorted(L, key = Fruit.sort_priority):
    print(f.name)
# key = lambda x: x.sort_priority()

L = ["Cherry", "Apple", "Blueberry"]

print(sorted(L, key=len))
#alternative form using lambda, if you find that easier to understand
print(sorted(L, key= lambda x: len(x)))

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)

"""Sometimes you will find it convenient to define a method for the class that
does some computation on the data in an instance. In this case, our class is
too simple to really illustrate that. But to simulate it, I’ve defined a
method sort_priority that just returns the price that’s stored in the
instance. Now, that method, sort_priority takes one instance as input and
returns a number. So it is exactly the kind of function we need to provide
as the key parameter for sorted. Here it can get a little confusing: to
refer to that method, without actually invoking it, you can refer to
Fruit.sort_priority. This is analogous to the code above that
referred to len rather than invoking len()."""
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print ("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print( "---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)


