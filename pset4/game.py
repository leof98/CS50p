# implement a program that:

#Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
#Randomly generates an integer between 1 and , inclusive, using the random module.
#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit.


import random

# Loop until positive
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except:
        pass

while True:
    number = random.randint(1, n)
    try:
        guess = input("Guess: ")
        if int(guess) == number:
            print("Just right!")
            break
        elif int(guess) > number:
            print("Too large!")
        elif int(guess) < number:
            print("Too small!")
    except:
        pass

#06/07
