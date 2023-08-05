import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

# Top 10 Songs

# Top 10 Genres

# Change of Features over time
