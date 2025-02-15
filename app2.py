import streamlit as st
import joblib
import pandas as pd
import requests
import gdown
import os

# ✅ Set page config at the very top before any Streamlit command
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Google Drive direct download links
MOVIES_LIST_URL = "https://drive.google.com/uc?id=1jWPuvch2G4O3WwRf5Tecsh71hsrtO8OB"
SIMILARITIES_URL = "https://drive.google.com/uc?id=1dr6Isu71xnyCyoDdRDaAjzZUcMnvU-fd"

# Function to download and load joblib files
@st.cache_data()
def load_joblib(url):
    output = url.split("/")[-2] + ".joblib"
    gdown.download(url, output, quiet=False)
    if not os.path.exists(output):
        st.error(f"❌ Failed to download {output}. Please check the Google Drive link.")
        return None
    return joblib.load(output)

# Load data
movies_list = load_joblib(MOVIES_LIST_URL)
similarities = load_joblib(SIMILARITIES_URL)

# Convert movies list to DataFrame
movies = pd.DataFrame(movies_list)

# OMDB API key
OMDB_API_KEY = "9e503a3d"

# Function to fetch movie poster
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

# Sidebar with app info
st.sidebar.title("ℹ️ About the App")
st.sidebar.write(
    "🎥 This **Movie Recommendation System** suggests movies based on your selection.\n\n"
    "💡 Using **Machine Learning**, it finds the best matches based on similarity scores.\n\n"
    "📦 Data is fetched from a pre-trained model and movie details come from **OMDb API**."
)
st.sidebar.markdown("---")
st.sidebar.write("📌 **Created by Noureen**")

# Main UI
st.title("🎬 Movie Recommendation System")
st.markdown("**Find the best movies based on your preferences!**")

# Movie selection
movie_list = movies["title"].values
selected_movie = st.selectbox("🎥 Select a Movie:", movie_list)

if st.button("🎬 Recommend"):
    recommended_movies, posters = recommend(selected_movie)

    # Display recommendations in a grid
    st.subheader("🔹 Recommended Movies:")
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    for i in range(len(recommended_movies)):
        with columns[i % 5]:
            st.image(posters[i], caption=recommended_movies[i], width=140)

# Custom CSS for UI enhancements
st.markdown(
    """
    <style>
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
        }
        .stSelectbox {
            width: 80%;
            margin: auto;
        }
        .stImage img {
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.2s ease-in-out;
        }
        .stImage img:hover {
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)
