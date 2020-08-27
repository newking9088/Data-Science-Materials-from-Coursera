CURRENT_YEAR = 2019
class Person:
    def __init__(self,name, year_born):
        self.name = name
        self.year_born = year_born
    def getAge (self):
        return CURRENT_YEAR - self.year_born
    def __str__(self):
        return "{} ({})".format (self.name, self.getAge)
nawa = Person ("Nawaraj Paudel", 1992)
print(nawa)

class Student ():
    def __init__(self,name, year_born):
        self.name = name
        self.year_born = year_born
        self.knowledge = 0
    def getAge (self):
        return CURRENT_YEAR - self.year_born
    def study(self):
        self.knowledge += 1
    def __str__(self):
        return "{} ({})".format (self.name, self.getAge)
nawa = Student ("Nawaraj Paudel", 1992)
nawa.study()
print(nawa.knowledge)

# we can do this in another easy way..since every student is a person
# we can inherit Student from Person class
class Student ( Person ):
    def __init__(self,name, year_born):
        Person.__init__(self, name, year_born)
        self.knowledge = 0
    def study(self):
        self.knowledge += 1
    def __str__(self):
        return "{} ({})".format (self.name, self.getAge)
nawa = Student ("Nawaraj Paudel", 1992)
nawa.study()
print(nawa.knowledge)
print(nawa.getAge())
