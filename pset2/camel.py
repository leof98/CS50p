# implement a program that prompts the user for the name of a variable in camel case and
# outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.
# 20.04

name = str(input("camelCase: "))

snake = ""
for n in name:
    if n.islower() == False:
        n = n.lower()
        n = n.replace(n, "_" + n)
        snake += n
    elif n.islower() == True:
        snake += n
    else:
        pass

print(snake)
