# Code for Multi- Level Inheritance

class MusicalInstruments():
    numberOfMajorKeys = 12

class StringedInstruments(MusicalInstruments):
    typeOfWood = 'ToneWood'

class Guitar(StringedInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This Guitar consists of {} strings. It is made of {}, and has {} major keys.".format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))

guitar = Guitar()