import requests as req
from bs4 import BeautifulSoup as bs

webpage = req.get(
    "https://en.wikipedia.org/wiki/2020_Summer_Olympics_medal_table#Medals")

webpage_s = bs(webpage.content, "html.parser")
