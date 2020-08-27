""" Here we have a Superclass or Parentclass Book and two subclass as Ebook and
PaperBook that inherits from Book. In addition, we can use Book constructor
method to add some instance variable in each subclass. Finally, we have a
different class called Library which does not inherit anything from Book."""
class Book():
    def __init__ (self, title , author):
        self.title = title
        self. author = author
    def __str__ (self):
        return "{} by {}".format ( self.title, self. author)

class PaperBook (Book):
    def __init__(self, title, author, numPages):
    # title & author can be inherited from parent class Book as
        Book.__init__(self, title, author)
        self.numPages = numPages    # one more instance added

class EBook (Book):
    def __init__(self, title, author, size):
    # title & author can be inherited from parent class Book as
        Book.__init__(self, title, author)
        self.size = size    # one more instance added

# this class does not inherit anything from Super Class
class Library ():
    def __init__(self):
        self.books = []   # no books initially/ composition variable
    def addBook(self, book):
        return self.books.append(book)
    def getNumberBooks(self):
        return len(self.books)

myBook = EBook ( "The Oddessy", "Homer", 2 )
myPaperBook = PaperBook ( "The Oddessy", "Homer", 500 )
print(myBook.size)   # size is an attribute of class Ebook

aadl = Library()
aadl.addBook (myBook)
aadl.addBook (myPaperBook)
print(aadl.getNumberBooks())
    
        
