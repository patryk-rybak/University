#! python3
# Usage: main2.py <a meal description in a few words>
# Search recipes in natural language and gives a link.
# Patryk Rybak

import private
import requests
import sys

if len(sys.argv) == 1:
    print("Usage: main2.py <a meal description in a few words>")
    quit()

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

querystring = {"query": ' '.join([s for s in sys.argv[1::]])}

headers = {
    "X-RapidAPI-Key": private.Key,
    "X-RapidAPI-Host": private.Host
}

res = requests.request("GET", url, headers=headers, params=querystring)
json = res.json()

print()
for data in json["results"]:
    print(data["sourceUrl"])
    print(data["title"] + ":")
    print("ready in", data["readyInMinutes"], "minuts")
    print("servings:", data["servings"])
    print()
