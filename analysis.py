import pandas as pd
import matplotlib as plt

df = pd.read_csv("data/titanic.csv")
print(df.head())
print(df.describe())

print(df["price"].mean())

df["price"].hist()