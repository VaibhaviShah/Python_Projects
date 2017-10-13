# Code to understand Multiple Inheritance

class OperatingSystem():
    multitasking = True
    name = 'Operating System'

class Apple():
    website = 'www.apple.com'
    name = 'Apple'

# Order of inheritance important
class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multi tasking system. Visit {} for more details.".format(self.website))
            print("Class Name:", self.name)

macBook = MacBook()