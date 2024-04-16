#! python3
# Usage: py.exe main.py <waluta>
# <waluta> - trzyliterowy kod waluty (standard ISO 4217)
# Patryk Rybak

import requests
import matplotlib.pyplot as plt
import sys

def prediction_for_next_month(data):
    return (data[-3] + data[-1]) / 2.0

if len(sys.argv) != 2:
    print("Usage: py.exe main.py <waluta>\n<waluta> - trzyliterowy kod waluty (standard ISO 4217)")
    quit()

tab = 'A'
month = "01"
year = "2020"
data2020_NBP = []
data2021_NBP = []
data2020_other = []
data2021_other = []

url1 = f"http://api.nbp.pl/api/exchangerates/rates/{tab}/{sys.argv[1].upper()}/{year}-{month}-01/{year}-{month}-28/?format=json"
url2 = f"https://api.exchangerate.host/timeseries?start_date={year}-{month}-01&end_date={year}-{month}-28&base={sys.argv[1].upper()}&format=json&symbols=PLN"

res1 = requests.get(url1)
res2 = requests.get(url2)

if res1.status_code != 200:
    tab = 'B'
    res1 = requests.get(url1)
    if res1.status_code != 200:
        print("staus code: ", res1.status_code)
        quit()

year = '2020'
for i in range(2):
    for i in range(1, 13):
        val1 = 0
        count1 = 0
        val2 = 0
        count2 = 0

        month = str(i).rjust(2, "0")
        url1 = f"http://api.nbp.pl/api/exchangerates/rates/{tab}/{sys.argv[1].upper()}/{year}-{month}-01/{year}-{month}-28/?format=json"
        for rate in res1.json()["rates"]:
            val1 += float(rate["mid"])
            count1 += 1 
        eval("data" + year + "_NBP").append(val1 / count1)

        url2 = f"https://api.exchangerate.host/timeseries?start_date={year}-{month}-01&end_date={year}-{month}-28&base={sys.argv[1].upper()}&format=json&symbols=PLN"
        res2 = requests.get(url2).json()["rates"]
        for date in res2:
            val2 += res2[date]['PLN']
            count2 += 1
        eval("data" + year + "_other").append(val2 / count2)
          
        res1 = requests.get(url1)
    year = '2021'

# print(data2020_other)
# print(data2021_other)

xs = [i + 1 for i in range(12)]
fig1, (ax1, ax2) = plt.subplots(2, 1, constrained_layout = True)
fig2, (ax3, ax4) = plt.subplots(2, 1, constrained_layout = True)

ax1.plot(xs, data2020_NBP, [12, 13], [data2020_NBP[-1], prediction_for_next_month(data2020_NBP)])
ax1.set_ylabel("PLN")
ax1.set_xlabel("Months")
ax1.set_title("NBP 2020")
ax1.grid()
ax1.legend([sys.argv[1].upper(), "prediction"])


ax2.plot(xs, data2020_other, [12, 13], [data2020_other[-1], prediction_for_next_month(data2020_other)])
ax2.set_ylabel("PLN")
ax2.set_xlabel("Months")
ax2.set_title("other 2020")
ax2.grid()
ax2.legend([sys.argv[1].upper(), "prediction"])

ax3.plot(xs, data2021_NBP, [12, 13], [data2021_NBP[-1], prediction_for_next_month(data2021_NBP)])
ax3.set_ylabel("PLN")
ax3.set_xlabel("Months")
ax3.set_title("NBP 2021")
ax3.grid()
ax3.legend([sys.argv[1].upper(), "prediction"])

ax4.plot(xs, data2021_other, [12, 13], [data2021_other[-1], prediction_for_next_month(data2021_other)])
ax4.set_ylabel("PLN")
ax4.set_xlabel("Months")
ax4.set_title("other 2021")
ax4.grid()
ax4.legend([sys.argv[1].upper(), "prediction"])

plt.show()
