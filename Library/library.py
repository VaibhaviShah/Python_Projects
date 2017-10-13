# Class ==> Library
# Layers of Abstraction ==> display books, lend a book, add a book


class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayBooks(self):
        print('\n Available Books: ')
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank You")

# class Customer:
#     def requestBook(self):
#         print("Enter the name of book you would like to borrow: ")
#         self.book = input()
#         return self.book
#
#     def returnBook(self):
#         print("Enter the name of the book you want to return: ")
#         self.book = input()
#         return self.book

#
# library = Library(['Atlas Shrugged', 'Monk who sold his Ferrari', '5 Love Languages'])
# customer = Customer()
#
# while True:
#     print("Enter 1 to display books")
#     print("Enter 2 to lend a book")
#     print("Enter 3 to return a book")
#     print("Enter 4 to exit")
#     userChoice = int(input())
#
#     if userChoice is 1:
#         library.displayBooks()
#     elif userChoice is 2:
#         requestedBook = customer.requestBook()
#         library.lendBook(requestedBook)
#     elif userChoice is 3:
#         returnedBook = customer.returnBook()
#         library.addBook(returnedBook)
#     else:
#         quit()
