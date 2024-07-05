import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
import re
from functions import search, suggested_lst, model

data_fp = os.path.join("..", "Rec_System")

abs_data_fp = os.path.abspath(data_fp)
print(f"Absolute path: {abs_data_fp}")

files = os.listdir(data_fp)

movies = pd.read_csv(
    os.path.join(data_fp, files[-2])
)
users = pd.read_csv(
    os.path.join(data_fp, files[-1])
)

#movies = pd.read_csv('../Rec_System/movies.csv')
#users = pd.read_csv('../Rec_System/ratings.csv')

movies['mod_title']= movies['title'].apply(lambda x: x[:x.find('(')])

# load model from pkl
with open("model.pkl", "rb") as f:
    functions = pickle.load(f)
    f.close()
    
search = functions['func1']
suggested_lst = functions['func2']
model = functions['func3']


#using streamlit methods to create an interactive app

#app title
st.title("Movie Recommendation System")

#text input
x = st.text_input('Type in a movie you liked for recommendations.\
    (Note: Please be patient. System requires about 1 min 35 secs to load):')
lst=[]
if st.button('Make recommendations'):
    lst = model(x)

    if (len(lst)==0):
        st.write('Sorry. But it appears there\'s no movie we can recommend :(')
    else: 
        st.write('Based on the movie you liked, here is a list of movies we recommend:', lst)

