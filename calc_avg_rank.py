#!/usr/bin/python

import pandas as pd
import numpy as np
from sql_to_df import sql_to_df
from df_to_sql import df_to_sql
from sql_query import send_query

# call on module to pull table from sql db and convert to df
df = sql_to_df("oly_rank_and_data")
# check import worked
print(df)

# initialise empty lists to add caculated average ranking for each country, 
# one list is the recent most 4 olympics, one for the past 7 years (until 1996)

av_rank_3 = []
av_rank_6 = []

# loop through each row of the df, calculate the average rank over 4 and 7 years,
# added an if, else to check if the country has medalled enough times in each year
# for caluclation to be meaningful, if country not present twice in 4 olympics, avg 
# not calculated, if country not present 3 or more times in 7 olympics avg not calc.
for i in range(len(df)):
    if df.iloc[i,2:4].isna().sum() >= 2:
        av_rank_3.append(np.nan)
    else:
        av_rank_3.append(df.iloc[i,1:4].mean())
    if df.iloc[i,2:7].isna().sum() > 2:
        av_rank_6.append(np.nan)
    else:
        av_rank_6.append(df.iloc[i,1:7].mean())

d = {'country': df['country'], 'av_rank3': av_rank_3, 'av_rank6': av_rank_6}
new_df = pd.DataFrame(d)

df_to_sql(new_df, 'avg_rank_table')

send_query('''CREATE TABLE oly_rank_w_avg AS 
SELECT oly_rank_and_data.*, 
avg_rank_table.av_rank3,
avg_rank_table.av_rank6
FROM oly_rank_and_data
LEFT JOIN avg_rank_table 
ON oly_rank_and_data.country = avg_rank_table.country''')