name = input("Please give me your name: ")
age = int(input("Please give me your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday")
else:
    print("Sorry, you cannot enter the party, come back in {0} years".format(18 - age))