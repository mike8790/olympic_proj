import pandas as pd

df_gdp = pd.read_csv('worldbank_GDP_table.csv', sep=',')
df_oly = pd.read_csv('2020_oly_table.csv', sep='\t')

gdp_country = list(df_gdp.get('Country_Name'))
oly_country = list(df_oly.get('Country'))

gdp_col = []

for country in df_oly['Country']:
    if country in gdp_country:
        idx = df_gdp.index[
            df_gdp['Country_Name'].str.contains(country)].tolist()
        gdp_col.append(df_gdp['2019'][idx[0]])
    else:
        gdp_col.append('NULL')

df_oly['Nominal_GDP'] = gdp_col
df_oly.to_csv("2020_oly_table_v2.csv", header='False', sep='\t', na_rep='NULL')
