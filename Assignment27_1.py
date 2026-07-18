# write a python program to implement a class named bookstore with the following specifications

class BookStore:
    NoofBooks = 0

    def __init__(self, name, auther):
        self.name = name
        self.auther = auther
        BookStore.NoofBooks += 1

    def display(self):
        print(self.name, "By", self.auther, "no. of books:", BookStore.NoofBooks)

obj1 = BookStore("linux system programming", "robert love")
obj1.display()



    