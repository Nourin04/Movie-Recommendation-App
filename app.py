import streamlit as st
import pickle
import pandas as pd
import requests

# Load the saved model and data
movies_dict = pickle.load(open("movies_list.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarities.pkl", "rb"))

# OMDb API Key
OMDB_API_KEY = "http://www.omdbapi.com/?i=tt3896198&apikey=9e503a3d"

def fetch_poster(movie_title):
    """Fetch movie poster from OMDb API"""
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()
    return response.get("Poster", "https://via.placeholder.com/300x450")  # Default image if not found

def recommend(movie):
    """Get movie recommendations based on similarity scores"""
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))
    
    return recommended_movies, recommended_posters

# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Select a Movie:", movies["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    # Display recommended movies with posters
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], caption=names[i], use_column_width=True)
