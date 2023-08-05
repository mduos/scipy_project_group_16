import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def topSongs(df, numHead):
    #artists sorted from most to least popular (popularity in relation to artist)
    df_popularSongs = df.groupby('song').sum().sort_values('popularity', ascending = False)
    df_popularSongs = df_popularSongs.reset_index()
    df_popularSongs

    topPopularSongs = df_popularSongs.head(numHead)
    plotTopSongs = topPopularSongs.plot(x='song', y='popularity', kind = 'bar', color = 'green')
    
    plotTopSongs.set_title(f"Top {numHead} most popular songs")
    plotTopSongs.set_xlabel('Songs')
    plotTopSongs.set_ylabel('Popularity of the Song')

    return plotTopSongs


def topArtists(df, num):
    df_popularArtists = df.groupby('artist').sum().sort_values('popularity', ascending=False)
    df_popularArtists = df_popularArtists.reset_index()
    df_popularArtists
    # visualize top 10 popularArtists
    topPopularArtists = df_popularArtists.head(num)
    plotTopArtists = topPopularArtists.plot(x='artist', y='popularity', kind = 'bar', color = 'green')

    plotTopArtists.set_title('Artists of the Top 10 most popular songs')
    plotTopArtists.set_xlabel('Artists')
    plotTopArtists.set_ylabel('Popularity of the Song')
    return plotTopArtists

def featurePlot(df, feature):
    sorted_df = df.sort_values('popularity', ascending = False)
    featurePlot = plt.plot(sorted_df['popularity'], sorted_df[feature], color = 'green')
    plt.xlabel = 'Popularity'
    plt.ylabel(feature)
    plt.title(f"Feature Plot: {feature} vs. Popularity")
    return featurePlot