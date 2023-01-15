# Day 25 - 30DaysOfPython Challenge
import pandas as pd

# Question 1
df = pd.read_csv("hacker_news.csv")
print(df)

# Question 2
first_five_rows = df.head()
print(first_five_rows)

# Question 3
last_five_row = df.tail()
print(last_five_row)

# Question 4
title= df.iloc[:,1]
print(title)

# Question 5
print(df.shape)

# Question 5.1
python_title = df.loc[df['title'].str.contains('Python', case=False)]
print(python_title)

# Question 5.2
js_title = df.loc[df['title'].str.contains('JavaScript', case=False)]
print(js_title)

# Question 5.3
print(df.describe())
print(df.info())
