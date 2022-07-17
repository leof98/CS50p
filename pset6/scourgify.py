import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

names = []
try:
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            n_name = row['name'].split(',')
            names.append({'first':n_name[1].lstrip(), 'last':n_name[0], 'house': row['house']})
except FileNotFoundError:
        sys.exit('Could not read ' + sys.argv[1])

try:
    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        for row in names:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})
except FileNotFoundError:
        sys.exit('Could not read ' + sys.argv[2])


if __name__ == '__main__':
    main()
# 17.07
