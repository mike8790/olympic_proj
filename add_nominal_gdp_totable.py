import pandas as pd

df_gdp = pd.read_csv('worldbank_GDP_table.csv', sep=',')
df_oly = pd.read_csv('2020_oly_table.csv', sep='\t')

gdp_country = list(df_gdp.get('Country_Name'))
oly_country = list(df_oly.get('Country'))

year = '2018'  # string with nominal GDP year you want to generate
column_name = ('Nominal_GDP_' + year)
gdp_col = []

for country in df_oly['Country']:
    if country in gdp_country:
        idx = df_gdp.index[
            df_gdp['Country_Name'].str.contains(country)].tolist()
        gdp_col.append(df_gdp[year][idx[0]])
    else:
        gdp_col.append('NULL')


df_oly[column_name] = gdp_col
df_oly[column_name] = pd.to_numeric(df_oly[column_name],
                                    errors='coerce')

version_num = '3'
filename = ('2020_oly_table' + version_num + '.csv')
df_oly.to_csv(filename, header='False', sep='\t', index=False)

'''
# need to work out plotting of both line and scatter
theta = np.polyfit(df_oly['Rank'], df_oly['Nominal_GDP'], 1)
y_line = theta[1] + theta[0] * df_oly['Rank']
plt.scatter(df_oly['Rank'], df_oly['Nominal_GDP'])
plt.plot(df_oly['Rank'], y_line, 'r')

plt.show()
'''
