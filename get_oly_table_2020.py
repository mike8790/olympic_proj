import requests as req
from bs4 import BeautifulSoup as bs
#import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

webpage = req.get(
    "https://olympics.com/en/olympic-games/tokyo-2020/medals")

soup = bs(webpage.content, "html.parser")

country_names = soup.findAll(attrs={"data-cy": "country-name"})
medals = soup.findAll(attrs={"data-cy": "medal-main"})

country = []
rank = []
gold = []
silver = []
bronze = []
total = []
all_medals = []

for medal in medals:
    all_medals.append(medal.text)

for gld in all_medals[0:-1:4]:
    gold.append(gold)

for slv in all_medals[1:-1:4]:
    silver.append(slv)

for brnz in all_medals[2:-1:4]:
    bronze.append(brnz)

for ttl in all_medals[3:-1:4]:
    total.append(ttl)

for name in country_names:
    country.append(name.text)
