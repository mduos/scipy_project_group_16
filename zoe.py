import pandas as pd
#import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/spotify_dataset.csv')

# Display first and last 5 rows
print(df.head())
print(df.tail())

# Overview of datapoints
print(df.columns)

# Checking for null values
print(df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Overview of unique release years
release_years = np.sort(df['year'].unique())
print(release_years)                       

# Since dataset is supposed to only include songs from 2000-2019, we'll get rid of any songs released before 2000
data_drop = df[(df['year'] < 2000) | (df['year'] > 2019)].index
df = df.drop(data_drop)

# Checking unique release years again
print(np.sort(df['year'].unique()))

# More information about the dataset
print(df.info())                        # Shape and size of dataset
print(df.describe())                    

# How many artists, songs and are in the dataset?
print(df['artist'].nunique())    # There's a total of 819 artists in the dataset
print(df['song'].nunique())      # There's a total of 1840 songs in the dataset
print(df['genre'].nunique())     # There's a total of 58 genres/genre combinations in the dataset

# Who are the top 10 artists?
top_10_artists = df.groupby('artist')[['artist','song', 'explicit','danceability','popularity','loudness','energy','speechiness','instrumentalness','acousticness','liveness','genre']].sum(numeric_only=True).sort_values('popularity', ascending=False).head(10)
print(top_10_artists)

name = top_10_artists[:10].index
popularity = top_10_artists['popularity'][:10]

fig = plt.figure()

plt.bar(name, popularity, color = "Orange")
plt.xlabel('Artists')
plt.ylabel('Popularity')
plt.xticks(rotation = 75)
plt.title('Top 10 Artists from 2000-2019', color = 'black', fontsize = 20)
plt.show()

# What are the top 10 songs?
top_10_songs = df.sort_values('popularity', ascending =False).head(10)[['popularity','song','artist']]
print(top_10_songs)

fig = plt.figure()

plt.bar(top_10_songs['song'], top_10_songs['popularity'], color = 'Orange')
plt.xlabel('Songs')
plt.ylabel('Popularity')
plt.xticks(rotation = 75)
plt.title('Top 10 Songs from 2000-2019', color = 'black', fontsize = 20)
plt.show()



# Top 5 most popular genres


# Most popular artist each year 


# Most popular song each year


# Most popular genre each year






