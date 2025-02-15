import streamlit as st
import joblib
import pandas as pd
import requests
import gdown
import os

# Google Drive direct download links
MOVIES_LIST_URL = "https://drive.google.com/file/d/1jWPuvch2G4O3WwRf5Tecsh71hsrtO8OB/view?usp=sharing"
SIMILARITIES_URL = "https://drive.google.com/file/d/1dr6Isu71xnyCyoDdRDaAjzZUcMnvU-fd/view?usp=sharing"

# Function to download and load joblib files
import joblib
import gdown
import os

@st.cache_data()
def load_joblib(url):
    output = url.split("/")[-2] + ".joblib"  # Extract the file ID and create a filename
    gdown.download(url, output, quiet=False)

    # ✅ Check if the file is actually downloaded
    if not os.path.exists(output):
        st.error(f"Failed to download {output}. Please check the Google Drive link.")
        return None

    return joblib.load(output)


# Load data
movies_list = load_joblib(MOVIES_LIST_URL)
similarities = load_joblib(SIMILARITIES_URL)

# Convert movies list to DataFrame
movies = pd.DataFrame(movies_list)

# OMDB API key
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
