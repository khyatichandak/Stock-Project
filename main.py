import csv
import pandas as pd

rows = []
with open("data/stocks-screener-05-30-2022.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
# print(header)
# print(rows)

data= pd.read_csv("data/stocks-screener-05-30-2022.csv")
data
print(data.columns)
print(data.Symbol)