# Assignment : OOP with Book and EBook 

# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title            # Attribute
        self.author = author          # Attribute
        self.pages = pages            # Attribute

    def read(self):                   # Method
        print(f"Reading '{self.title}' by {self.author}...")

# Child class (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size    # New attribute specific to EBook

    def read(self):                   # Polymorphism: overrides Book's read()
        print(f"Reading the eBook '{self.title}' on a tablet (File size: {self.file_size}MB)")

# Creating objects
physical = Book("The Alchemist", "Paulo Coelho", 208)
digital = EBook("Digital Fortress", "Dan Brown", 356, 2.5)

# Calling methods
physical.read()
digital.read()

# Polymorphism in a loop
bookshelf = [physical, digital]
for item in bookshelf:
    item.read()
