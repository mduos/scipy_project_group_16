# scipy_project_group_16
This project handles a spotify dataset containing the most popular songs from 2000-2019.
We are interested in the idea that the features of songs influence how popular they are and how this might change over the course of time. 
Additionally, we provided a similarity search, in which the user can choose a song out of the dataset and is recommended a list of similar songs. 
The goal of our project is to give the user a good understanding over the dataset and it's values.

## Dataset
The dataset we used for our project is located in the data folder. [Dataset](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019).

## prep_data.py
In this file we define the **clean_data(df)** function, which we use to prepare the data for later use. Using this function, we drop null values and duplicates.

## query.py
The file query.py includes a function **query(df)** that asks the user for input of keywords and gives out either the number of artists, songs or genres that the dataset holds.

## SpotifyAnalysis.ipynb
Spotify Analysis.ipynb is our main code demonstration.
The file includes the data visualizations of our project.
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

## similarity.py
The similarity.py file computes the similarity of all songs to a song which the user picks out of the dataset and recommends five similar songs, based on the tempo, energy and genre of the songs. As an additional feature we include the possibility of only showing family friendly songs, so filtering out songs with explicit content. 
