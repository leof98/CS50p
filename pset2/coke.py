# Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

amount = 0
change = 50
while amount < 50:
    n = int(input("Insert Coin: "))

    if n == 5:
        amount += 5
        change -= 5
        if change < 0:
            print("Change Owed: " + str(abs(change)))
        else:
            print("Amount Due: " + str(change))
            
    elif n == 10:
        amount += 10
        change -= 10
        if change < 0:
            print("Change Owed: " + str(abs(change)))
        else:
            print("Amount Due: " + str(change))
            
    elif n == 25:
        amount += 25
        change -= 25
        if change < 0:
            print("Change Owed: " + str(abs(change)))
        else:
            print("Amount Due: " + str(change))
            
    elif n == 50:
        amount += 50
        change -= 50
        if change < 0:
            print("Change Owed: " + str(abs(change)))
        else:
            print("Amount Due: " + str(change))
            
    else:
        print("Amount Due: " + str(change))
