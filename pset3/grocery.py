# implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.
# 10.05

list = {}
n = 1
while True:
    try:
        item = input()
        if item not in list:
            list[item] = 0
        if item in list:
            list[item] += 1
    except KeyError:
        pass

    except EOFError:
        break

for i in sorted(list):
    print(list[i], i.upper())
