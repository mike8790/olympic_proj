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
rank = []

for n in range(0, len(medals), 4):
    gold.append(medals[n].text)
    silver.append(medals[n+1].text)
    bronze.append(medals[n+2].text)
    total.append(medals[n+3].text)

for name in country_names:
    country.append(name.text)

medal_data = {'Gold': gold, 'Silver': silver, 'Bronze': bronze,
              'Total Medals': total}

wine_df = pd.DataFrame(medal_data)

count = 1
for n in range(len(wine_df)):
    if ((wine_df.iloc[n, 1] == wine_df.iloc[n-1, 1])
        and (wine_df.iloc[n, 2] == wine_df.iloc[n-1, 2])
            and (wine_df.iloc[n, 3] == wine_df.iloc[n-1, 3])):
        rank.append(rank[-1])
    else:
        rank.append(count)
    count += 1

wine_df = wine_df.apply(pd.to_numeric, args=('coerce',))
wine_df.insert(0, 'Country', country)
wine_df.insert(0, 'Rank', rank)

print(wine_df)
