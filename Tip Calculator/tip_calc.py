"""
This is a simple program to calculate a tip and also each individual's share of the bill along with the tip.
"""

def calc(amnt, persons, tip):
    """
    Calculates the tip, and individual share

    :param amnt: The total bill amount in number
    :param persons: The no. of individual shares to be calculated for
    :param tip: The percent of bill amount to be paid as extra tip
    :return: Will print the tip, total amount to be paid and individual share
    """
    # percent of tip
    tip_amnt = round((tip/100)*amnt, 2)
    print("The tip you wish to pay is "+str(tip_amnt))

    indiv_bill = round(amnt/persons, 2)
    print("individual share for bill amount is: " + str(indiv_bill))

    indiv_tip = round(tip_amnt/persons, 2)
    print("Individual share for tip is: " + str(indiv_tip))

    print("Total individual share is: " + str(round(indiv_tip+indiv_bill)), 2)

def main():
    """
    Interacts with user to know the basic parameters required to calculate
    makes a call to calculate function for final calculations
    :return: Nothing
    """

    print("The Bill amount: ")
    while True:
        try:
            amnt = float(input())
            break
        except:
            print("Must be a number value")
    print("Enter the no. of individual shares: ")
    while True:
        try:
            persons = int(input())
            break
        except:
            print("Must be a number value")
    print("The tip percent you wish to give: ")
    while True:
        try:
            tip = int(input())
            break
        except:
            print("Must be a number value")

    calc(amnt, persons, tip)

if __name__ == '__main__':
    main()