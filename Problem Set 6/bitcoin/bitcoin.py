import requests
import sys
import json

try:
    bitcoin = float(sys.argv[1])
except (IndexError, ValueError):
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
    data = response.json()
except requests.RequestException:
    sys.exit(1)

price = data["bpi"]["USD"]["rate_float"]

total_cost = bitcoin * price

print(f"${total_cost:,.4f}")
