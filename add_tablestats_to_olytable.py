import pandas as pd

# open the Oly CSV and whatever statistic CSV to add to the Oly table
df_new = pd.read_csv('worldbank_population_table.csv', sep=',')
df_oly = pd.read_csv('2020_oly_table_v2.csv', sep='\t')
data_name = 'Population'

# extract country names columns from both dataframes
new_country = list(df_new.get('Country'))
oly_country = list(df_oly.get('Country'))

# set range of years to extract from table (if multiple years in the CSV)
years = range(2020, 2000, -1)

# nested loop - look at one year at a time, for each year first check
# if country in oly table is in the data - if it is extract the info for 
# that country for that year, appending the list to the end of the Oly table
for year in years:
    new_col = []
    for country in oly_country:
        if country in new_country:
            idx = df_new.index[
                df_new['Country'].str.contains(country)].tolist()
            new_col.append(df_new[str(year)][idx[0]])
        else:
            new_col.append('NULL')
    column_name = (data_name + '_' + str(year))
    df_oly[column_name] = new_col
    df_oly[column_name] = pd.to_numeric(df_oly[column_name],
                                        errors='coerce')

# save expanded df to new csv. Remember to iterate the v.num to reflect a new
# version
version_num = '3'  # as versions get created iterate this
filename = ('2020_oly_table_v' + version_num + '.csv')
df_oly.to_csv(filename, header='True', sep='\t', index=False)
