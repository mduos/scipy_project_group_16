import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def query(df):
    """ Function that tells you the number of artists, songs (of a specific genre/artist) and genres are in a dataset. 
        Takes dataframe as argument. Asks user for input of a keyword and outputs the answer of the query.
    """
    
    key = input("Please choose a number corresponding to what you want to know: \n 1. How many artists are in the dataset? \n 2. How many songs are in the dataset? \n 3. How many genres are in the dataset? \n")
    
    while (key not in ("1", "2", "3")):
        key = input("Please choose a number corresponding to what you want to know: \n 1. How many artists are in the dataset? \n 2. How many songs are in the dataset? \n 3. How many genres are in the dataset? \n")
        
    if key == "1": 
        # Count unique values in column 'artist'
        artist = str(df['artist'].nunique())
        print(f"There is a total of {artist} artists in the dataset!")
        return

    elif key == "2": 
        # Repeat input question as long as user does not pick a valid option
        x = input("Please pick a number corresponding to what you want to know: \n 1. How many songs are in the dataset? \n 2. How many songs of a specific genre are in the dataset? \n 3. How many songs of a specific artist are in the dataset? \n")

        while (x not in ("1", "2", "3")):
            x = input("Please pick a number corresponding to what you want to know: \n 1. How many songs are in the dataset? \n 2. How many songs of a specific genre are in the dataset? \n 3. How many songs of a specific artist are in the dataset? \n")

        if x == "1": 
            # Count unique values in column 'song'
            song = str(df['song'].nunique()) 
            print(f"There is a total of {song} songs in the dataset.")
            return 
        
        elif x == "2": 
            # Since some songs have multiple genres, we need to separate them 
            # Getting rid of blank spaces 
            df['genre'] = df['genre'].str.replace(" ", "")

            # Splitting strings 
            df['genre'] = df['genre'].str.split(",")

            # Separate genres
            genres = df.explode('genre')
            
            # Print list of all genres
            print(genres['genre'].unique())
            
            # Repeat input question until user gives valid input
            while True: 
                g = input("Please pick a genre out of the list: ")
                if g in genres['genre'].unique():
                    break
            
            # Count songs of genre g and return
            print(f"There is a total of {genres[genres['genre'] == g].shape[0]} song(s) with genre {g} in the dataset.")
            return
        
        elif x == "3": 
            # Print list of all artists in dataset
            print(df['artist'].unique())
            
            # Repeat input question until user gives valid input
            while True: 
                a = input("Please pick an artist out of the list: ")
                if a in df['artist'].unique(): 
                    break
            
            # Return count of songs by artist a
            print(f"There is a total of {df[df['artist'] == a]['song'].nunique()} song(s) by artist {a} in the dataset.")
            return
    
    elif key == "3": 
        # Since some songs have multiple genres, we need to separate them 
        # Getting rid of blank spaces 
        df['genre'] = df['genre'].str.replace(" ", "")

        # Splitting strings 
        df['genre'] = df['genre'].str.split(",")

        # Separate genres
        genres = df.explode('genre')

        # Count unique values of column 'genre'
        genre = str(genres['genre'].nunique())
        
        print(f"There is a total of {genre} genres in the dataset.")
        return



if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv('data/clean_spotify_dataset.csv')
    query(df)
