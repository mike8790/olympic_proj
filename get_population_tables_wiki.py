import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# get wiki country population and convert to soup object
webpage = req.get(
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
soup = bs(webpage.content, "html.parser")

# empty lists to add countries and populations to in rank order
country = []
population = []

# find in soup objects the countries and their populations (based on "td" flag position
# within table ("tbody")) 
for n in soup.find("tbody").find_all("td")[8:-1:7]:
    country.append(n.text)
for i in soup.find("tbody").find_all(["td"])[10:-1:7]:
    population.append(i.text)

# create data frame from the country and population list, print df to check formatting and 
# export as a csv
population_data = pd.DataFrame(list(zip(country, population)))
population_data.columns = ['Country', 'Population']
print(population_data)

population_data.to_csv("world_population_2022.csv", header='False', sep='\t', na_rep='NULL')