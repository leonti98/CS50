import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        rate = data.get("bpi", {}).get("USD", {}).get("rate")
        for _ in rate:
            rate = "".join(rate.split(","))
        print(f"${float(rate) * float(sys.argv[1]):,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
