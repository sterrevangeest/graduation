import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

recipes = []

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

diets = ["vegetarisch", "veganistisch", "zonder-vlees", "zonder-vlees-vis"]

for diet in diets:
    for i in range(0, 10):
        url = "https://www.ah.nl/allerhande/recepten-zoeken?menugang=hoofdgerecht&speciale-wensen=" + \
            diet + "&page=" + str(i)
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        for link in soup.find_all('a'):
            link = link.get('href')
            if link .startswith("/allerhande/recept/"):

                recipes.append({"link": link, "category": diet})

            with open('recipe-links-10.json', 'w') as outfile:
                json.dump(recipes, outfile)
