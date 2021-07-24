#no clue how to fix the error in this one.

import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv("tvSizeVStime.csv")
fig = px.scatter(df, y="hours spent watching in a week", x="Size of TV")
fig.show()

with open('tvSizeVStime.csv', newline="") as f:
  reader = csv.reader(f)
  tvSizeVStimeData = list(reader)
print (tvSizeVStimeData)
tvSizeVStimeData.pop(0)
TVsize=[]
hours=[]
for a in tvSizeVStimeData:
    TVsize.append(float(a[0]))
    hours.append(float(a[1]))
print(TVsize)
print(hours)



correlation = np.corrcoef(TVsize,hours)
print("Correlation between Size of Tv and Average time spent watching Tv in a week :-  \n--->",correlation[0,1])
