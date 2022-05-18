import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

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

for n in range(0, len(medals), 4):
    gold.append(medals[n].text)
    silver.append(medals[n+1].text)
    bronze.append(medals[n+2].text)
    total.append(medals[n+3].text)

for name in country_names:
    country.append(name.text)

data = {'Country': country, 'Gold': gold, 'Silver': silver, 'Bronze': bronze,
        'Total Medals': total}

df = pd.DataFrame(data)

print(df)
