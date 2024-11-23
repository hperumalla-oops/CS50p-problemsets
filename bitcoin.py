import requests
import sys
import json

try:
    sys.argv[1]=float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("could not exctract data from the following source")
else:
    json_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    rate =json_data.json().get("bpi").get("USD").get("rate")
    rate=rate.replace(",","")
    rate= float(rate)
    #print(rate)
    price =sys.argv[1]*rate
    #print("The Number: ", price)
    print("${:,.4f}".format(price))
