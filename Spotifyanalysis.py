# first import the necessary libraries

import pandas as pd

#read the csv file

df = pd.read_csv(r'C:\Users\\D E L L\\Downloads\\Spotify Most Streamed Songs.csv')
df.head()

# data cleaing

# check for any null values

print(df.isnull().sum())

#check for duplicates

duplicates = df.duplicated().sum()
print(f'Duplicates: {duplicates}')

# display the entire dataframe

print(df)


