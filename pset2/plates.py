# implement a program that prompts the user for a vanity plate and then output Valid if meets all of the
# requirements or Invalid if it does not. Assume that any letters in the usr’s input will be uppercase.
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and
# False if it does not. Assume that s will be a str
# 26.04

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    elif s[2] == "0":
        return False
    elif "." in s or "!" in s:
        return False
    elif "0" in s and s[-1].isalpha() == True:
        return False

    else:
        return True

main()
