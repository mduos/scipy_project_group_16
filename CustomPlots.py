import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def topSongs(df, numHead):
    #artists sorted from most to least popular (popularity in relation to artist)
    helper = df.copy()
    helper['song'] = helper['song'].astype(str)+ " by " +helper['artist'].astype(str)
    df_popularSongs = helper.groupby('song').sort_values('popularity', ascending = False)
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

def featurePlotSingle(df, feature):
    sorted_df = df.sort_values('popularity', ascending = False)
    featurePlot = plt.plot(sorted_df['popularity'], sorted_df[feature], color = 'green')
    plt.xlabel = 'Popularity'
    plt.ylabel(feature)
    plt.title(f"Effect of {feature} on Popularity")
    return featurePlot

def featurePlotTwo(df, feature1, feature2):
    sorted_df = df.sort_values('popularity', ascending = False)
    featuresPlot = plt.plot(500,10)
    plt.subplot(2,1,1)
    plt.plot(sorted_df['popularity'], sorted_df[feature1], color = 'green')
    plt.subplot(2,1,1)
    plt.plot(sorted_df['popularity'], sorted_df[feature2], color = 'orange')
    plt.xlabel = 'Popularity'
    plt.ylabel(f"{feature1} and {feature2}")
    plt.title(f"Effect of {feature1} and {feature2} on Popularity")
    return featuresPlot
