import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv("marksVSpresentese.csv")
fig = px.scatter(df, y="Days Present", x="Marks In Percentage")
fig.show()

with open('marksVSpresentese.csv', newline="") as f:
  reader = csv.reader(f)
  marksVSpresenteseData = list(reader)
print (marksVSpresenteseData)
marksVSpresenteseData.pop(0)
days=[]
percentage=[]
for a in marksVSpresenteseData:
    percentage.append(float(a[1]))
    days.append(float(a[2]))
print(days)
print(percentage)

correlation = np.corrcoef(days,percentage)
print("Correlation between days present and marks :-  \n--->",correlation[0,1])