# olympic_proj
Fund project to play around with Python for data analysis/ science as I extend my
Python/ SQL etc experience with codeacademy and other online learning oppurtunities.

Long-term - want to add a number of factors to the olympic_table (e.g. GDP, population,
  happiness index, central funding of sport etc), report on the correlations between different factors and performance at different Olympics. Ultimately, try and identify the best predictive model
  for performance in the Olympics. If quick enough with the model, test it on the upcoming commonwealth games (not a perfect test as not all countries present in both, but of interest).

1) 'get_oly_table_2020.py': generated a df containing the medal table for the 2020 Olympics in Japan by scraping from the official website and saved a csv: '2020_oly_table'

2) 'add_nominal_ddp_totable.py': downloaded a csv from worldbank website of historical nominal GDP
values for countries of the world. Loaded this in and the '2020_oly_table' to the script - extract the
GDP values for every country on the olympic table and appended their GDPs for the past 20 years- script
adds new v* to end of oly_table once updated.

To do:
Add olympics results from previous Olympics (back to Barca 1992 as first after fall of the wall?)
Add GDP to table to match first Olympics - up to 2 years before first Olympics on list?
Add population figures.
Create report to show effects of population and GDP on average performance?
Then - begin to add other factors to the table

** Because of different naming conventions - certain countries I have decided on using
a specific name, whenever I extract new CSV etc I will manually adapt these.
Largely tried to keep countries to single word - so if prefixes or suffixes e.g.
'democratic repulic of' or 'peoples repulic' etc I have removed.
Countries to look out for (accepted name)
Egypt
Cote_dIvorie
Bahamas
United_Kingdom
Iran
Kyrgyz
Korea*
Russia
Slovakia
Venezuela
Taiwan
China
Hong_Kong
United_States
Moldova
*refers to South Korea, little info on North Korea and they do not enter olympics

Missing data -
From nominal GDP list = Taiwan (Chinese Taipei)
