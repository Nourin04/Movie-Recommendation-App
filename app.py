import streamlit as st
import pickle
import pandas as pd
import requests
import gdown

# Google Drive links for pickle files
MOVIES_LIST_URL = "https://drive.google.com/file/d/13v9lWU2aUn3L6tY8_NImOY9WIEuIahNX/view?usp=drive_link"
SIMILARITIES_URL = "https://drive.google.com/file/d/1iUp9RhiNwkq8mQgdWTckrn8pZCTY1Kyr/view?usp=sharing"

# Function to download and load pickle files
@st.cache_data()
def load_pickle(url):
    output = url.split("=")[-1] + ".pkl"
    gdown.download(url, output, quiet=False)
    
    with open(output, "rb") as f:
        return pickle.load(f, encoding="latin1")  # Fix compatibility issue


# Load data
movies_list = load_pickle(MOVIES_LIST_URL)
similarities = load_pickle(SIMILARITIES_URL)

# Convert movies list to DataFrame
movies = pd.DataFrame(movies_list)

# OMDB API key for fetching posters
OMDB_API_KEY = " http://www.omdbapi.com/?i=tt3896198&apikey=9e503a3d"

def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()
    return response.get("Poster", "https://via.placeholder.com/300")

# Function to recommend movies
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"], []

    index = movies[movies['title'] == movie].index[0]
    distances = similarities[index]
    movie_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    posters = []
    
    for i in movie_indices:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        posters.append(fetch_poster(title))

    return recommended_movies, posters

# Streamlit UI
st.title("🎬 Movie Recommendation System")

movie_list = movies["title"].values
selected_movie = st.selectbox("Select a Movie:", movie_list)

if st.button("Recommend"):
    recommended_movies, posters = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    cols = st.columns(5)
    for i in range(len(recommended_movies)):
        with cols[i % 5]:  
            st.image(posters[i], caption=recommended_movies[i], width=120)
