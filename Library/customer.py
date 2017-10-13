# class ==> Customer
# Layers of Abstraction ==> request a book, return a book

class Customer:
    def requestBook(self):
        print("Enter the name of book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you want to return: ")
        self.book = input()
        return self.book