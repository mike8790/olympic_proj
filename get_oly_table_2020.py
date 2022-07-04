import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

# get 2020 Tokyo olympic table and convert to soup object
webpage = req.get(
    "https://olympics.com/en/olympic-games/tokyo-2020/medals")
soup = bs(webpage.content, "html.parser")

# create empty country list, append each country in soup object with country-name 
# attribute
country = []
for n in soup.findAll(attrs={"data-cy": "country-name"}):
    country.append(n.text)

# identify numbers for each medal type + total medals won 
medals = soup.findAll(attrs={"data-cy": "medal-main"})

# create empty list to store numbers for gold-bronze, total and rank for each country
gold = []
silver = []
bronze = []
total = []
rank = []

# loop through medals list - isolate text (number of each medal won), ordered as g/s/b/t 
# and append to the relevant medal list
for n in range(0, len(medals), 4):
    gold.append(medals[n].text)
    silver.append(medals[n+1].text)
    bronze.append(medals[n+2].text)
    total.append(medals[n+3].text)

# combine all medal lists in a dictionary and convert to df
medal_data = {'Gold': gold, 'Silver': silver, 'Bronze': bronze,
              'Total Medals': total}
df = pd.DataFrame(medal_data)

# loop to generate rank list, because some countries acheive same number of all three
# medals which makes them the same rank, add current count to rank if medal numbers 
# are unique or keep rank same as previous rank, if medals numbers are the same
# iterate count on each loop 
count = 1
for n in range(len(df)):
    if ((df.iloc[n, 1] == df.iloc[n-1, 1])
        and (df.iloc[n, 2] == df.iloc[n-1, 2])
            and (df.iloc[n, 3] == df.iloc[n-1, 3])):
        rank.append(rank[-1])
    else:
        rank.append(count)
    count += 1

# adjust medal_data df so NaN become 0 and insert country and rank lists, export 
# complete df to csv
medal_df = (df.apply(pd.to_numeric, args=('coerce',)).
            fillna(0, downcast='infer'))
medal_df.insert(0, 'Country', country)
medal_df.insert(0, 'Rank', rank)
medal_df.to_csv("2020_oly_table_tester.csv", header='True', sep='\t', na_rep='NULL',
                index=False)
