import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv("tempVSsales.csv")
fig = px.scatter(df, y="Ice-cream Sales( ₹ )", x="Temperature")
fig.show()

with open('tempVSsales.csv', newline="") as f:
  reader = csv.reader(f)
  tempVSsalesData = list(reader)
print (tempVSsalesData)
tempVSsalesData.pop(0)
temp=[]
icecream=[]
for a in tempVSsalesData:
    temp.append(float(a[0]))
    icecream.append(float(a[1]))
print(temp)
print(icecream)



correlation = np.corrcoef(temp,icecream)
print("Correlation between tempurature and ice cream sales :-  \n--->",correlation[0,1])
