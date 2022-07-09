import requests
import sys

# Expects the user to specify as a command-line argument the number of Bitcoins, n,  \that they would like to buy.
try:
    n = sys.argv[1]
    argument = float(n)

# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
except requests.RequestException:
    print("aconteceu")

# Queries the API for the CoinDesk Bitcoin Price Index which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
r = r.json()
amount = r['bpi']['USD']['rate_float']
amount = float(n) * amount
# Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.
print(f"${amount:,.4f}")
#08/07
