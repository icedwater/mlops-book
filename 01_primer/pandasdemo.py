#! /usr/bin/env python

"""
Example code with pandas
"""

import pandas as pd

df = pd.DataFrame(data={"fruit": ["mango", "kiwi", "durian", "grapefruit", "grape"], \
                        "size": ["large", "small", "large", "medium", "small"], \
                        "quantity": [7, 9, 2, 5, 16]})

print(df.head(1))       # get top row of dataframe
print(df.tail(1))       # get bottom row of dataframe
print(df.describe())    # statistical summary of dataframe
print(df["fruit"])
print(df.loc[df["size"] == "small"])
print(df.iloc[2])       # get the row at position 2
print(df.iloc[1:2, 0:1])
print(df.groupby(["size"])["quantity"].mean())

df.to_csv("fruit.csv")
df.to_excel("fruit.xlsx")       # requires openpyxl
