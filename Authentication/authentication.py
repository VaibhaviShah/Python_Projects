# authentication simple code using dictionary
accessGranted = False
member_dict = {'A': 'a1', 'B': 'b1', 'C': 'c1', 'D': 'd1'}

while accessGranted == False:
    username = input("Please enter your membership username: ")
    if username in member_dict:
        password = input("Hello "+username + '! Please enter your password: ')
        if password == member_dict[username]:
            print("ACCESS GRANTED")
            accessGranted = True
        else:
            print("Incorrect Password \n ACCESS DENIED")
    else:
        print("No such username. \n ACCESS DENIED")