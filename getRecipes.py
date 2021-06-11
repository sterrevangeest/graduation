from recipe_scrapers import scrape_me
import pandas as pd
import json
import sys
sys.setrecursionlimit(10**6)

completeRecipes = []

with open('recipe-links-20.json') as json_file:
    recipes = json.load(json_file)
    for recipe in recipes:
        scraper = scrape_me(
            'https://www.ah.nl/' + recipe['link'], wild_mode=True)
        completeRecipes.append(
            {"link": recipe['link'], "category": recipe['category'], 'title': scraper.title(), 'total_time': scraper.total_time(), "yields": scraper.yields(), 'ingredients': scraper.ingredients(), 'instructions': scraper.instructions(), "image": scraper.image(), "nutrients": scraper.nutrients()
             })

    with open('recipes-20.json', 'w') as outfile:
        json.dump(completeRecipes, outfile)
