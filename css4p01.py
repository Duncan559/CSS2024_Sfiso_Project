# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
df = pd.read_csv("C:/Users/SFISO/OneDrive - University of Venda/Desktop/CSS_Movie_Dataset/movie_dataset.csv")
import matplotlib.pyplot as plt


pd.set_option('display.max_rows',None)
print(df)


x = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(x, inplace=True)

x = df["Metascore"].mean()
df["Metascore"].fillna(x, inplace=True)
print(df)

# save the cleaned dataset to a new csv file
df.to_csv("C:/Users/SFISO/OneDrive - University of Venda/Desktop/CSS_Movie_Dataset/movie_dataset_cleaned.csv")
df.info()

# create a dictionary
# key = old name
# value = new name
dict = {'Runtime (Minutes)': 'Runtime', 'Revenue (Millions)': 'Revenue'}
print("\nAfter rename")
df.rename(columns=dict,inplace=True)
display(df)


selected_columns = ['Year', 'Runtime','Rating','Votes','Revenue', 'Metascore']
selected_data = df[selected_columns]
correlation_matrix = selected_data.corr()
plt.figure(figsize=(10,8))                         


"""
# arrange the dataframe (df) by ratings
df=df.sort_values(by='Rating', ascending=False)
top_rated = df[['Rating'].head(10,6)]

#arrange the dataframe df by year of release
df=df.sort_values(by='Year',ascending=False)
Year_of_release = df[['Year']].head
"""
#arrange the df by director
df=df. sort_values (by='Director', ascending=False)
Director_con= df[['Director']]
"""
#arrange the df by average revenue 
df=df. sort_values (by='average revenue', ascending=False)
averege_revenue=df[['average revenue']]

import pandas as pd
df=pd.read_csv("C:/Users/SFISO/OneDrive - University of Venda/Desktop/CSS_Movie_Dataset/movie_dataset_cleaned.csv")
print(df)

# frequence of movies per year
df=df.sort_values(by='Year',ascending=False)
