import pandas as pd

# open the CSV created using olympics wiki medal table
# (see get_oly_table_2020) and the nominal GDP table I downloaded from the
# worldbank website.
df_gdp = pd.read_csv('worldbank_GDP_table.csv', sep=',')
df_oly = pd.read_csv('2020_oly_table.csv', sep=',')

# extract country names columns from both dataframes
gdp_country = list(df_gdp.get('Country_Name'))
oly_country = list(df_oly.get('Country'))

# set range of years to extract GDP for
years = range(2020, 2000, -1)

# nested loop - look at one year of GDP at a time, for each year first check
# if country in oly table is in the worldbank list - if it is extract their GDP
# append it to a list before appending that list to the end of the oly df
for year in years:
    gdp_col = []
    for country in oly_country:
        if country in gdp_country:
            idx = df_gdp.index[
                df_gdp['Country_Name'].str.contains(country)].tolist()
            gdp_col.append(df_gdp[str(year)][idx[0]])
        else:
            gdp_col.append('NULL')
    column_name = ('Nominal_GDP_' + str(year))
    df_oly[column_name] = gdp_col
    df_oly[column_name] = pd.to_numeric(df_oly[column_name],
                                        errors='coerce')

# save expanded df to new text. Remember to iterate the v.num to reflect a new
# version
version_num = '2'  # as versions get created iterate this
filename = ('2020_oly_table_v' + version_num + '.csv')
df_oly.to_csv(filename, header='True', sep='\t', index=False)
