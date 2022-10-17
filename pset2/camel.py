# Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

nome = str(input("camelCase: "))
snake = ""

for letra in nome:
    if letra.islower() == False:
        letra = letra.lower()
        letra = letra.replace(letra, "_" + letra)
        snake += letra
    elif letra.islower() == True:
        snake += letra
    else:
        pass

print(snake)
