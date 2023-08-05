import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('data/spotify_dataset.csv')

# Preprocess the dataset
# Performing a normalization on the tempo and energy values so that different scaling has no influence
df['tempo'] = (df['tempo'] - df['tempo'].mean()) / df['tempo'].std()
df['energy'] = (df['energy'] - df['energy'].mean()) / df['energy'].std()

def calculate_similarity(song1, song2):
    tempo_diff = song1['tempo'] - song2['tempo']
    energy_diff = song1['energy'] - song2['energy']
    genre_similarity = 1 if song1['genre'] == song2['genre'] else 0
    
    return np.sqrt(tempo_diff**2 + energy_diff**2 + (1-genre_similarity)**2)

def find_similar_songs(song_name, family_friendly=True):
    # Find the song from the dataset
    song = df.loc[df['song'] == song_name].iloc[0]

    # Filter songs based on family-friendliness
    if family_friendly:
        filtered_df = df.loc[df['explicit'] == False]
    else:
        filtered_df = df.copy()

    # Calculate similarity with all other songs in the filtered dataset
    filtered_df.loc[:, 'similarity'] = filtered_df.apply(lambda row: calculate_similarity(row, song), axis=1)

    # Sort the filtered dataset based on similarity
    sorted_df = filtered_df.sort_values(by='similarity')

    # Return the top 5 most similar songs
    top_5_similar_songs = sorted_df.iloc[1:6]

    return top_5_similar_songs[['song', 'artist', 'genre']]

def similarity_search():
    print("Welcome to Similarity Search:\nInsert a song name in the input window, we will find you the five most similar songs to it.\n")
    

    while True:
        # Ask user if they want family-friendly songs
        family_friendly_input = input("Do you want family-friendly songs? (y/n): ").lower()
        # Check for a valid input, if not valid print message
        if family_friendly_input in ['y', 'n']:
            family_friendly = family_friendly_input == 'y'
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Get song name from user input til a valid input
    while True:
        song_name = input("Enter the name of the song: ")
        # Find the song in the dataset
        result = df[df['song'] == song_name]
        # If song is not found print message
        if not result.empty:
            break
        else:
            print("Your song is apparently not in the dataset. Try a valid song title.\n")

    # Start similarity search with the users input choices
    result = find_similar_songs(song_name, family_friendly)
    print("The five most similar songs to >{}< are:\n\n{}\n\nHave fun listening!".format(song_name, result))
    
    #similarity()