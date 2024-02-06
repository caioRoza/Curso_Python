import pandas as pd

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

df.columns
df["Unit price"].sum()

a = []
for i in range(0, 10):
    if i % 2 == 0:
        print(i)

print('Hello World')