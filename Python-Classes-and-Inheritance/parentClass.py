"""Here is an example. Say we want to define a class Cat that inherits from Pet.
Assume we have the Pet class that we defined earlier. We want the Cat type to
be exactly the same as Pet, except we want the sound cats to start out knowing
“meow” instead of “mrrp”, and we want the Cat class to have its own special
method called chasing_rats, which only Cats have.For reference, here’s the
original Tamagotchi code"""

from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that  
#when we make changes to it, we won't affect the other Pets in the class
    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

# Here's the new definition of class Cat, a subclass of Pet.
class Cat(Pet): # the class name that the new class inherits from goes in the parentheses, like so.
    sounds = ['Meow']   # see the constructor of 

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"

"""In the original Tamagotchi game in the last chapter, you saw code
that created instances of the Pet class. Now let’s write a little bit
of code that uses instances of the Pet class AND instances of the Cat class."""
p1 = Pet("Fido")
print(p1) # we've seen this stuff before!

p1.feed()
p1.hi()
print(p1)

cat1 = Cat("Fluffy")
print(cat1) # this uses the same __str__ method as the Pets do

cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi()
print(cat1)

print(cat1.chasing_rats())

#print(p1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!

"""And you can continue the inheritance tree. We inherited Cat from Pet. Now say
we want a subclass of Cat called Cheshire. A Cheshire cat should inherit
everything from Cat, which means it inherits everything that Cat inherits
from Pet, too. But the Cheshire class has its own special method, smile."""
class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")

# Let's try it with instances.
cat1 = Cat("Fluffy")
cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() # Uses the special Cat hello.
print(cat1)

print(cat1.chasing_rats())

new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
new_cat.hi() # same as Cat!
new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
p1 = Pet("Teddy")
p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.

"""Q1. intro-9-1: After you run the code, new_cat = Cheshire("Pumpkin"), how many instance variables
exist for the new_cat instance of Cheshire?
A. 1
B. 2
C. 3
D. 4  (Correct Answer)
Neither Cheshire nor Cat defines an __init__ constructor method,
so the grandaprent class, Pet, will have it's __init__ method called.
That constructor method sets the instance variables name, hunger, boredom, and sounds."""

"""Q2. intro-9-2: What would print after running the following code:

new_cat = Cheshire("Pumpkin”)   # Created an instance
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
another_cat.song()

A. We are Siamese if you please. We are Siamese if you don’t please. (Correct)
B. Error
C. Pumpkin
D. Nothing. There's no print statement.
Another_cat is an instance of Siamese, so its song() method is invoked"""

"""Q3. intro-9-3: What would print after running the following code:

new_cat = Cheshire("Pumpkin”) # Created an instance
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
new_cat.song()
A. We are Siamese if you please. We are Siamese if you don’t please.
B. Error   (Correct)
C. Pumpkin
D. Nothing. There’s no print statement.
You cannot invoke methods defined in the Siamese class on an instance of the Cheshire class.
Both are subclasses of Cat, but Cheshire is not a subclass of Siamese, so it doesn't
inherit its methods."""
