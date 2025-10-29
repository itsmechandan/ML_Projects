import streamlit as st
import pickle
from pathlib import Path
import requests

# 1. Load data into separate, descriptive variables
current_dir = Path(__file__).parent
file_path = current_dir / 'movie_list.pkl'
file2_path = current_dir / 'similarity.pkl'

similarity = pickle.load(open(file2_path,'rb'))
# Keep the full DataFrame in a variable 'movies_df'
movies_df = pickle.load(open(file_path, 'rb')) 

# Create the list of titles for the selectbox
movie_titles = movies_df['title'].values 

def recommend(movie):
    # Use the full DataFrame 'movies_df' here
    movie_index = movies_df[movies_df['title']== movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        # Use the full DataFrame 'movies_df' here as well
        recommended_movies.append(movies_df.iloc[i[0]].title) 
    return recommended_movies

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title('Movie Recommender System')
# Use the titles array for the selectbox
option = st.selectbox('Select Movie Recommendation', movie_titles) 

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)

        