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

df = pd.DataFrame(medal_data)

count = 1
for n in range(len(df)):
    if ((df.iloc[n, 1] == df.iloc[n-1, 1])
        and (df.iloc[n, 2] == df.iloc[n-1, 2])
            and (df.iloc[n, 3] == df.iloc[n-1, 3])):
        rank.append(rank[-1])
    else:
        rank.append(count)
    count += 1

medal_df = (df.apply(pd.to_numeric, args=('coerce',)).
            fillna(0, downcast='infer'))
medal_df.insert(0, 'Country', country)
medal_df.insert(0, 'Rank', rank)

medal_df.to_csv("2020_oly_table.csv", header='False', sep='\t', na_rep='NULL')
