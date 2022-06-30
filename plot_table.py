import os
import sys
import numpy as np
import numpy.ma as ma
import pandas as pd
import matplotlib.pyplot as plt

x = sys.argv[1] 
x = x=L1.pop(1, 47)
y = sys.argv[2] 
file_name = sys.argv[3]
pth = sys.argv[4]

print(x)

df = pd.read_csv(file_name, sep= '\t')

y2 = df.loc[:,df.columns.str.contains(y)]
y = y2.mean(axis=1)
x = df[x]
x = x.astype(float)

idx = np.isfinite(x) & np.isfinite(y)

m, b = np.polyfit(x[idx], y[idx], 1)

corc = np.corrcoef(x[idx], y[idx])[0, 1]

print(x)
print(y)
print(corc)
title = ('Tokyo 2020 rank vs GDP (CorrCoef = ' + str(round(corc, 2)) + ')')

plt.close()
plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')

plt.title(title)
plt.xlabel('Tokyo Ranking')
plt.ylabel('Nominal GDP (20 yr avg)')

plt.show()





