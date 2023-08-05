import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def topSongs(df, num):
    """ Takes a dataframe and integer as input and plots the top songs for that number."""

    # Helper dataframe to add artist name to song title
    helper = df.copy()
    helper['song'] = helper['song'].astype(str)+ " by " + helper['artist'].astype(str)

    # Sort by popularity and only show 'num' amount of entries
    top_songs = helper.sort_values('popularity', ascending = False).head(num).reset_index()
    
    top_songs.plot(x='song', y='popularity', kind = 'bar', color = 'green')
    
    plt.title(f"Top {num} Songs")
    plt.xlabel('Songs')
    plt.ylabel('Popularity of the Song')

    plt.show()


def topArtists(df, num):
    """ Takes a dataframe and integer as argument and plots the top artists."""

    top_artists = df.groupby('artist').sum(numeric_only=True).sort_values('popularity', ascending=False).head(num).reset_index()
    
    # Create a barplot

    top_artists.plot(x='artist', y='popularity', kind = 'bar', color = 'green')
    plt.title(f"Top {num} Artists")
    plt.xlabel("Artist")
    plt.ylabel("Popularity")

    plt.show()

    
def percGenres(df):
    """ Takes a dataframe as argument and plots the percentage of each genre."""
    
    # Since some songs have multiple genres, we need to separate them 
    # Getting rid of blank spaces 
    df['genre'] = df['genre'].str.replace(" ", "")

    # Splitting strings 
    df['genre'] = df['genre'].str.split(",")

    # Separate genres
    genres = df.explode('genre')
    
    # Create plot
    fig = plt.figure(figsize = (10, 10))
    genres.genre.value_counts().plot(kind = "pie", autopct='%1.1f%%')
    plt.title(f"Percentage of Genres")

    plt.show()
    


def featurePlotSingle(df, feature):
    """ Takes a dataframe and a feature/column name as argument and returns a plot that 
    shows relation between that feature and popularity.
    """
    
    # Sort by popularity
    sorted_df = df.sort_values('popularity', ascending = False)
    
    # Create a plot with popularity as its x-argument and feature as y-argument
    feature_plot = plt.plot(sorted_df['popularity'], sorted_df[feature], color = 'green')
    plt.xlabel('Popularity')
    plt.ylabel(feature)
    plt.title(f"Effect of {feature} on Popularity")

    plt.show()

def featurePlotDouble(df, feature1, feature2):
    """ Takes a dataframe and two features/column names as argument and returns plot that shows 
    the relation between the features and popularity.
    """
    # Sort by popularity
    sorted_df = df.sort_values('popularity', ascending = False)
    
    # Create plot
    features_plot = plt.plot(500,10)

    plt.subplot(2,1,1)
    plt.plot(sorted_df['popularity'], sorted_df[feature1], color = 'green')
    
    plt.subplot(2,1,1)
    plt.plot(sorted_df['popularity'], sorted_df[feature2], color = 'orange')
   
    plt.xlabel('Popularity')
    plt.ylabel(f"{feature1} and {feature2}")
    plt.title(f"Effect of {feature1} and {feature2} on Popularity")
   
    plt.show()

if __name__ == "__main__":
    # Load data
    df = pd.read_csv("data/clean_spotify_dataset.csv")

    # Top 10 Artists
    topArtists(df, 10)

    # Top 10 Songs
    topSongs(df, 10)

    # Genres
    percGenres(df)

    # Feature Plots
    featurePlotSingle(df, "loudness")
    featurePlotDouble(df, "valence", "energy")




