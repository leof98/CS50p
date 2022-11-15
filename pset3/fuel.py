"""
Prompts for a fraction (Formatted as X/Y) and then outputs as a percentage rounded, how much fuel is in the tank.
If < than 1% remains, output E instead. And if > than 99% remains, output F instead.
05.11, 11.22
"""

def main():

    while True:
        try:
            fraction = input('Fraction: ')
            fraction = fraction.split('/')
            x,y = int(fraction[0]),int(fraction[1])
            fuel = (x / y) * 100

            if x > y:
                pass
            elif fuel <= 1:
                print('E')
                break
            elif fuel > 75:
                print('F')
                break
            else:
                fuel = round(fuel)
                print(f'{fuel}%')
                break

        except (ValueError, ZeroDivisionError):
            pass

main()
