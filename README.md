# olympic_proj
Fun project to play around with Python for data analysis/ science as I extend my
Python/ SQL etc experience with codeacademy and other online learning oppurtunities.

Will be added to inconsistently as I find time and get 

1) 'get_oly_table_2020.py': generated a df containing the medal table for the 2020 Olympics in Japan by scraping from the official website and saved a csv: '2020_oly_table'

2) 'add_nominal_ddp_totable.py': downloaded a csv from worldbank website of historical nominal GDP
values for countries of the world. Loaded this in and the '2020_oly_table' to the script - extract the
GDP values for every country on the olympic table and appended their GDPs for the past 20 years- script
adds new v* to end of oly_table once updated.

3) For world populations = wrote a script to extract country populations from wikipedia, 
but worldbank csv download is much better - as contains data from 1960 onward:
https://data.worldbank.org/indicator/SP.POP.TOTL

4) plot_scatter.py = script to take two columns from specified CSV file and location, plot a scatter and
correlation coefficient of two variables

5) Wrote script to loop through olympic website and extract medal tables from all olympics back to Seoul '88
- ignored Moscow and LA because of major boycotts.

To do?
Calculate correlation between avg. ranking in previous Olympics and performance in most recent Olympics
Create report to show effects of population and GDP on average performance?
Add other factors to the table - identify potential factors of interest and access relevant data
Expand beyond simple correlation analyses and descriptive statistics - perhaps multivariate regression
Transfer data from multiple CSVs to a SQL database

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

Missing data from worldbank lists-
From nominal GDP and population list = Taiwan (Chinese Taipei)




