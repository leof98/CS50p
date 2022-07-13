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

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    else:
        return True

if __name__ == "__main__":
    main()
# 13/07
