import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from custom_plots import *

# Load data 
df = pd.read_csv("data/clean_spotify_dataset.csv")

# Number of Songs per Year
songs_per_year = df.groupby('year')['song'].count()

songs_per_year.plot(x='year', y='song', kind='line')
plt.title('Number of Songs over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Songs')
plt.show()

# Top 10 Artists
topArtists(df, 10)

# Top 10 Songs
topSongs(df, 10)

# How often does each genre occur?
percGenres(df)

# How many Songs are explicit?
explicit = df.groupby('explicit', as_index=False).count().sort_values('song', ascending=False)
df.explicit.value_counts().plot(kind = "pie", autopct='%1.1f%%')
plt.title("Percentage of Songs with Explicit Content")
plt.show()

# Explicitness of Songs over the Years
# Grouping the data by 'years' and calculating the average explicit content for each year
explicit_content_by_year = df.groupby('year')['explicit'].mean().reset_index()

# Sorting the data by 'years' in ascending order
explicit_content_by_year = explicit_content_by_year.sort_values('year', ascending=True)

# Creating the plot
plt.plot(explicit_content_by_year['year'], explicit_content_by_year['explicit'], color  = 'green')
plt.xlabel('Years')
plt.ylabel('Average Explicitness')
plt.title('Average Explicitness of Songs over the Years')
plt.xticks(rotation=45)
plt.show()

# How many songs each artist has in dataset
song_per_artist = df.groupby('artist', as_index=False).count().sort_values('song', ascending=False).head(50)
song_per_artist.plot(x = 'artist', y = 'song', kind = 'bar', xlabel = 'Artist', ylabel = 'Number of Songs', title = 'Number of Songs by Each Artist')
plt.show()

# Popularity of Modes 'Minor' and 'Major'
popularityMode = df.groupby('mode').size().reset_index(name='count')
popularityMode['mode'] = popularityMode['mode'].apply(lambda x: 'Major' if x == 1 else 'Minor')
plt.bar(popularityMode['mode'], popularityMode['count'], color = 'green')
plt.xlabel('Mode')
plt.ylabel('Number of Songs')
plt.title('Popularity of Each Mode')

# Sound Feature Correlation Heatmap
sns.set(font_scale=0.8)
info = df.drop(['key','mode','explicit'], axis=1).corr(method = 'pearson')
map = sns.heatmap(info, annot = True, fmt = '.1g', vmin=-1, vmax=1, center=0, cmap='inferno', linewidths=1, linecolor='White',square = False, annot_kws={"fontsize": 8})
map.set_title('Correlation Heatmap')
map.set_xticklabels(map.get_xticklabels(), rotation=90)