import sys
import csv
from tabulate import tabulate

def main():
    # Verifica as condicoes
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    menu = []
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(menu[1:], headers=menu[0], tablefmt='grid'))


if __name__ == "__main__":
    main()
# 16.07
