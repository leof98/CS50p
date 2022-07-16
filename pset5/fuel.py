def main():
    fuel = input("Fraction: ")
    n_fuel = convert(fuel)
    fuel_print = gauge(n_fuel)
    print(fuel_print)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            new_x = int(x)
            new_y = int(y)
            n = new_x / new_y
            if n <= 1:
                p = int(n * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
