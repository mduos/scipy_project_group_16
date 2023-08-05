# scipy_project_group_16
We use a dataset containing the most popular songs on spotify from the years 2000-2019 to give the user a basic overview about the dataset.
Additionally, we included a similarity search, in which one of the songs from the dataset can be selected and the most similar songs to the input song are listed.

## Dataset
The dataset we used for our project is located in the data folder. The source for the dataset can be found when following this link: [Dataset](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019).

## query.py
The file query.py includes a function **query(df)** that asks the user for input of keywords and gives out either the number of artists, songs or genres that the dataset holds.

## Spotify Analysis.ipynb
The file Spotify Analysis.ipynb includes the data visualizations of our project.
In this file, firstly we break down the structure of the dataset. To give an outline of the dataset we print samples the columns of the dataset, as well as a value description and information about the types of data used in the dataset. 
Then, we include plots showing the most popular artists, songs and genres. Additionally, we plot the average explicitness of popular songs over the years and we check if there is a significant difference in the popularity of modes (major vs. minor). 
In this file, we call two different functions that can be used to plot the relation of certain features on the popularity of songs. One for plotting individual features and one for comparing two features and their effect on popularity.
Lastly, we included a heatmap that portrays the correlation of the features.

## custom_plots.py
The file custom_plots.py includes multiple functions to make the plots adjustable to the users interests.

The function **topSongs(df, num)** takes the dataset and an integer as arguments and ouputs the most popular songs in the dataset. How many songs are plotted is decided by the assignment of num when calling    the function. 

The function **topArtists(df, num)** works the same way as topSongs, but outputs the most popular artists. 

The function **percGenres(df)** takes the dataframe as an argument and plots the percentage of each genre in a pie chart. 

Also in this file, the functions for plotting different features are included, as they are called in the Spotify Analysis.ipynb file. Namely, these functions are the **featurePlotSingle(df, feature)** and **featurePlotDouble(df, feature1, feature2)**. They take one or two (depending on the function) features/ column names of the dataframe as an argument and return a plot that shows the relation between the chosen feature(s) and the popularity. 

## similarity.ipynb
The similarity.ipynb file computes the similarity of all songs to a song which the user picks out of the dataset and recommends five similar songs, based on the tempo, energy and genre of the songs. 
