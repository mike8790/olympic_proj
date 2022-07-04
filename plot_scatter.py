import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# take user arguments and convert them to variables to be manipulated
# create file path for Oly csv from user input of file name and directory, 
# use file path to generate dataframe from csv
pth_file = os.path.join(sys.argv[4], sys.argv[3])
df = pd.read_csv(pth_file, sep= '\t')

# Using user specified variable names for x and y of scatter plot (e.g. Rank and GDP/ 
# Population etc) select required data from dataframe - for y data (if multiple years 
# specified -  take the mean of those years)
y1 = df.loc[:,df.columns.str.contains(sys.argv[2])]
if len(df.columns) > 1:
    y = y1.mean(axis=1)
else:
    y = y1
x1 = df[sys.argv[1]]
x = x1.astype(float) # make sure x variable (will usually be Rank) float (not int) 
                     # so can calculate corrcoef against float data (e.g. GDP, pop etc)

# identify outliers that have z-score's greater then 3 (can change threshold variable)
outliers=[]
threshold=3
mean_y = np.mean(y)
std_y = np.std(y)
    
for i in range(len(y)):
    z_score= (y[i] - mean_y)/std_y 
    if np.abs(z_score) > threshold:
        outliers.append(i)

# if there are outliers in the outlier list - use outlier variable as a variable to create 
# valid data variables (*_in) and outlier data variables (*_out) for plotting and calculating 
# corrcoef
if len(outliers) != 1:
    y_in = y.drop(outliers, axis=0)
    x_in = x.drop(outliers, axis=0)
    y_out = y[outliers]
    x_out = x[outliers]
    idx_in = np.isfinite(x) & np.isfinite(y) # create index for x and y data that is valid 
                                             # for corrcoef calc (i.e. !NaN)
    m_out, b_out = np.polyfit(x_in[idx_in], y_in[idx_in], 1) 
    corc_out = np.corrcoef(x_in[idx_in], y_in[idx_in])[0, 1]

# calculate corrcoef of x/y data including any potential outliers
idx = np.isfinite(x) & np.isfinite(y) # create index for x and y data that is valid 
                                      # for corrcoef calc (i.e. !NaN)
m, b = np.polyfit(x[idx], y[idx], 1)
corc = np.corrcoef(x[idx], y[idx])[0, 1]
print(corc)

# create scatter plots for x (usually Rank in Olympics) against data of choice (GDP, 
# population, previous result in Olympics etc).

title = ('Tokyo 2020 rank vs ' + sys.argv[2])
legend1 = ('Rank vs ' + sys.argv[2])
legend2 = ('CorrCoef (' + str(round(corc, 2)) + ')')

plt.close()

# plot data with outliers and corrcoef calculated with outliers
plt.plot(x, y, 'b.' )
plt.plot(x, b + m * x, 'b-')
plt.legend([legend1, legend2], loc='upper right', bbox_to_anchor=(1.05, 1), fontsize='small', 
               fancybox=True, shadow=True)

# plot + signs over outliers and corrcoef calculated with outlier, if there are any in data
if len(outliers) != 1:
    plt.plot(x_out, y_out, 'r+' )
    plt.plot(x_in, b_out + m_out * x_in, 'r-')
    plt.legend([legend1, legend2, (legend1 + ' (outliers)'), 
                ('CorrCoef (ex. outliers, ' + str(round(corc_out, 2)) + ')')], 
               loc='upper right', bbox_to_anchor=(1.05, 1), fontsize='small', 
               fancybox=True, shadow=True)

plt.title(title)
plt.xlabel('Tokyo Ranking')
plt.ylabel(sys.argv[2])

plt.show()





