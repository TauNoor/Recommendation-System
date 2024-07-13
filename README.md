# Recommendation-System
This system makes movie recommendations based on an algorithm that looks to perform a form of collaborative filtering.

## Recommendation Algorithm Description
The algorithm takes your inputted movie and finds other users who liked the same movie as you. We check what other movies those users liked and select them as our preliminary list of suggested movies. We proceed to filter it further using the similarness in the genres, ratings and popularity of the movies.

## Setting up the environment to locally host the app
- Ensure you have pip installed all the required libraries
- Make sure to adjust the absolute paths of the .csv files in both .py files after git cloning the repository
- Open up your terminal/command prompt and cd to the 'model' folder and run the command "streamlit run streamlit_app.py"
- Have fun!

## Data Source: 
The data was obtained from the Kaggle Website. Here is the link: https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system
