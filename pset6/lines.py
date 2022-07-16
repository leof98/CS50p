import sys

def main():
    x = len(sys.argv)
    if x < 2:
        print("Too few command-line arguments")
    elif x > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    y = sys.argv[1]
    try:
        z = open(y, "r")
        count = 0
        for lines in z.readlines():
            if is_comment(lines) == False:
                count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


def is_comment(line):
    if line.isspace():
        return True
    elif line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()
# 15.07
