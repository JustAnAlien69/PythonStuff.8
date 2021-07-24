import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv("coffeeVSsleep.csv")
fig = px.scatter(df, y="sleep in hours", x="Coffee in ml")
fig.show()

with open('coffeeVSsleep.csv', newline="") as f:
  reader = csv.reader(f)
  coffeeVSsleepData = list(reader)
print (coffeeVSsleepData)
coffeeVSsleepData.pop(0)
sleep=[]
coffee=[]
for a in coffeeVSsleepData:
    coffee.append(int(a[1]))
    sleep.append(int(a[2]))
print(coffee)
print(sleep)



correlation = np.corrcoef(coffee,sleep)
print("Correlation between Size of Tv and Average time spent watching Tv in a week :-  \n--->",correlation[0,1])
