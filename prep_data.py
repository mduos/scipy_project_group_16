import numpy as np
import pandas as pd


def clean_data(df):
    ''' Prepares dataset for later use. Takes a dataframe as input and returns it cleaned. 
        Saves cleaned dataframe as a claned csv
    '''

    # Checking for null values
    null_bool = pd.isnull(df)

    # Drop null values
    df.drop(columns = df[null_bool == True])

    # Dropping any duplicate rows
    df.drop_duplicates()

    # Save dataframe as csv file
    df.to_csv('data/clean_spotify_dataset.csv')
    
    return df


if __name__ == "__main__": 

    # load dataset
    df = pd.read_csv('data/spotify_dataset.csv')
    
    # Look at first and last 5 rows
    print(df.head())
    print(df.tail())

    # Datapoints
    print(df.columns)

    # More information on dataset
    print(df.info())
    print(df.describe())
    
    df = clean_data(df)
    print(df)

