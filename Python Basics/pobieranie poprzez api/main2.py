#! python3
# Usage: main.py <from_curr> <to_curr> <price_alert>
# Usage: main.py <from_curr> <to_curr>
# Usage: main.py
# Tracks exchange rate
# Patryk Rybak 


import requests
import sys
import time


def get_current_data(from_sym='BTC', to_sym='USD'):
    url = 'https://min-api.cryptocompare.com/data/price'

    parameters = {'fsym': from_sym, 'tsyms': to_sym}

    res = requests.get(url, params=parameters)
    data = res.json()

    return data


if len(sys.argv) > 4:
    print("Usage: main.py <from_curr> <to_curr> <price_alert>")
    print("Usage: main.py <from_curr> <to_curr>")
    print("Usage: main.py")
    quit()

if len(sys.argv) == 1: print("\nBTC : " + str(get_current_data()['USD']) + " " + "USD")
elif len(sys.argv) == 3: print("\n" + sys.argv[1].upper() + " : " + str(get_current_data(sys.argv[1].upper(), sys.argv[2].upper())[sys.argv[2].upper()]) + " " + sys.argv[2].upper())
else:
    rate = get_current_data(sys.argv[1].upper(), sys.argv[2].upper())
    rate = rate[sys.argv[2].upper()]
    print()
    precision = 5.0
    while abs(rate - float(sys.argv[3])) > precision:
        time.sleep(5)
        rate = get_current_data(sys.argv[1].upper(), sys.argv[2].upper())
        rate = rate[sys.argv[2].upper()]
        print(sys.argv[1].upper(), ":", rate, sys.argv[2].upper())
        
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(str(sys.argv[1].upper() + "   :   " + str(rate) + " " + sys.argv[2].upper()).center(50))
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

