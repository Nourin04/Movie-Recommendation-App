import streamlit as st
import pickle
import pandas as pd
import requests
import gdown  # To download files from Google Drive

# 🔹 Replace these with your actual Google Drive file IDs
MOVIES_FILE_ID = "https://drive.google.com/file/d/13v9lWU2aUn3L6tY8_NImOY9WIEuIahNX/view?usp=sharing"
MODEL_FILE_ID = "https://drive.google.com/file/d/1iUp9RhiNwkq8mQgdWTckrn8pZCTY1Kyr/view?usp=sharing"

# 🔹 Replace this with your OMDb API Key
OMDB_API_KEY = "http://www.omdbapi.com/?i=tt3896198&apikey=9e503a3d"

# Function to download large files from Google Drive
def download_file(file_id, output):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output, quiet=False)

# Download and load movies.pkl
movies_file = "movies.pkl"
download_file(MOVIES_FILE_ID, movies_file)
movies_dict = pickle.load(open(movies_file, "rb"))
movies = pd.DataFrame(movies_dict)

# Download and load model.pkl
model_file = "model.pkl"
download_file(MODEL_FILE_ID, model_file)
similarity = pickle.load(open(model_file, "rb"))

# Function to fetch movie posters using OMDb API
def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("Poster", "https://via.placeholder.com/300")  # Default poster if not found

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        movie_title = movies.iloc[i[0]]["title"]
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))
    
    return recommended_movies, recommended_posters

# Streamlit UI
st.title("🎬 Movie Recommendation System")
selected_movie = st.selectbox("Select a Movie:", movies["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    # Display recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.text(names[i])
            st.image(posters[i], width=150)
