from customer import Customer
from library import Library

library_1 = Library(['Atlas Shrugged', 'Monk who sold his Ferrari', '5 Love Languages'])
user = Customer()

while True:
    print("Enter 1 to display books")
    print("Enter 2 to lend a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())

    if userChoice is 1:
        library_1.displayBooks()
    elif userChoice is 2:
        requestedBook = user.requestBook()
        library_1.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = user.returnBook()
        library_1.addBook(returnedBook)
    else:
        quit()
