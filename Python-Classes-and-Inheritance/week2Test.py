"""The class, Pokemon, is provided below and describes a Pokemon and its
leveling and evolving characteristics. An instance of the class is one pokemon
that you create. Grass_Pokemon is a subclass that inherits from Pokemon but
changes some aspects, for instance, the boost values are different. For the
subclass Grass_Pokemon, add another method called action that returns the
string "[name of pokemon] knows a lot of different moves!". Create an
instance of this class with the name as "Belle". Assign this
instance to the variable p1."""
class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
    def action (self):
        return "{} knows a lot of different moves!".format(self.name)
p1 = Grass_Pokemon("Belle")

"""Modify the Grass_Pokemon subclass so that the attack strength for
Grass_Pokemon instances does not change until they reach level 10. At level 10
and up, their attack strength should increase by the attack_boost amount when
they are trained. To test, create an instance of the class with the name as
"Bulby". Assign the instance to the variable p2. Create another instance of
the Grass_Pokemon class with the name set to "Pika" and assign that instance
to the variable p3. Then, use Grass_Pokemon methods to train the p3
Grass_Pokemon instance until it reaches at least level 10."""


