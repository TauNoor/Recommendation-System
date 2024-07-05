import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
import re
import os 

file_name = "movies.csv"
file_name2 = "ratings.csv"

'''movies = pd.read_csv(
    os.path.abspath(file_name)
)
users = pd.read_csv(
    os.path.abspath(file_name2)
)'''

movies = pd.read_csv('../Rec_System/movies.csv')
users = pd.read_csv('../Rec_System/ratings.csv')

movies['mod_title']= movies['title'].apply(lambda x: x[:x.find('(')])

def search(query):
    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform(movies['mod_title'])
    
    processed = re.sub("[^a-zA-Z0-9 ]","", query.lower())
    query_vec = vectorizer.transform([processed])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    
    indices = np.argpartition(similarity,-10)[-5:]
    
    results = movies.iloc[indices]
    
    return results

def suggested_lst(mov_ID,mov_genre): 
    overlap_users = set()

    for i in range(users.shape[0]):
    
        if users['movieId'].iloc[i] == mov_ID and users['rating'].iloc[i] >= 4.5:
            user_id = users['userId'].iloc[i]
            overlap_users.add(user_id)
            
    similar_users = users[users['userId'].isin(overlap_users)]
    merged_df = similar_users.merge(movies,on='movieId',how='inner')
    
    
    freq_lst = ((merged_df['mod_title'].value_counts() > 30).apply(lambda x: x if x else np.NaN)).dropna()
    freq_names = list(freq_lst.index)
    
    if len(freq_names) == 0:
        return []
    
    common_liked = merged_df[merged_df['mod_title'].isin(freq_names)]
    common_liked['mod_genre'] = common_liked['genres'].str.replace('[|]'," ", regex=True)
    
    most_liked = common_liked.groupby('mod_title').mean()[['rating']].sort_values('rating',ascending=False).\
    reset_index()
    
    genres_movies = common_liked[['mod_title','mod_genre']].drop_duplicates(subset=['mod_title'])
    
    general_rec_df = most_liked.merge(genres_movies, on='mod_title')
    
    vectorizer2 = TfidfVectorizer()
    tfidf2 = vectorizer2.fit_transform(general_rec_df['mod_genre'])
    
    query_genre = mov_genre
    processed2 = re.sub("[|]"," ", query_genre)
    
    query_vec2 = vectorizer2.transform([processed2])
    similarity2 = cosine_similarity(query_vec2, tfidf2).flatten()
    indices2 = np.argpartition(similarity2,-10)[-50:]
    
    recs_df = general_rec_df.iloc[indices2].sort_values('rating',ascending=False)
    final_df = recs_df.iloc[1:11]
    rec_lst = list(final_df['mod_title'])
    
    return rec_lst
    
def model(query):
    
    search_df = search(query)
    
    liked_mov_id = search_df['movieId'].iloc[-1]
    
    liked_mov_genre = search_df['genres'].iloc[-1]
    
    ans = suggested_lst(liked_mov_id, liked_mov_genre)
    
    return ans


functions = {'func1': search, 'func2': suggested_lst, 'func3': model}

current = os.getcwd()
model_fp = os.path.join(current, "model")
os.makedirs(model_fp, exist_ok=True)
model_file = os.path.join(model_fp, "model.pkl")

with open(model_file, "wb") as f:
    pickle.dump(functions, f)
