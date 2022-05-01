# implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
# as a percentage rounded to the nearest integer, how much fuel is in the tank. If
# though, less than 1% remains, output E instead to indicate that the tank is empty
# And if more than 99% remains, output F instead to indicate that the tank is full
# 01.05

def main():
    while True:
        try:
            fuel = input("Fraction: ")
            x = fuel.split("/")
            x,y = int(x[0]), int(x[1])
            n = x / y
            if y < x:
                raise ValueError

            if n < 0.1:
                print("E")
                break
            elif n == 0.25:
                print("25%")
                break
            elif round(n, 2) == 0.50:
                print("50%")
                break
            elif n == 0.75:
                print("75%")
                break
            elif n > 0.99:
                print("F")
                break
            else:
                break

        except(ValueError, ZeroDivisionError):
            pass

main()
