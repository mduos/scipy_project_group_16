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

# Top 10 Genres
topGenres(df, 10)

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

