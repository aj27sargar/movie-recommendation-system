import streamlit as st
import pandas as pd
import requests
import pickle

# Load the processed data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Fetch movie poster from TMDB API
def fetch_poster(movie_id):
    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  # Replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path', '')  # Handle missing poster paths
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
    else:
        full_path = "https://via.placeholder.com/150"  # Placeholder image if no poster is found
    return full_path

# Custom CSS for background and styling
st.markdown(
    """
    <style>
    /* Background image */
    body {
        background-image: url('https://images.unsplash.com/photo-1590650042891-0ad55a4d5a59?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDE0fHxjYXJkJTIwbW92aWV8ZW58MHx8fHwxNjMxMzU5ODk4&ixlib=rb-1.2.1&q=80&w=1080');
        background-size: cover;
        background-position: center;
        color: white;
        height: 100vh;
        overflow: hidden;
    }

    /* Dark overlay to enhance readability */
    [data-testid="stAppViewContainer"] {
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(10px);
    }

    /* Title Styling */
    .title-style {
        color: #FFFFFF;
        font-size: 48px;
        text-align: center;
        background-color: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
    }

    /* Poster card styling */
    .poster-style {
        border-radius: 10px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.5);
    }
    .poster-style:hover {
        transform: scale(1.1);
        box-shadow: 0px 10px 20px rgba(255, 255, 255, 0.9);
    }

    /* Sidebar Styling */
    .css-1lcbmhc, .css-12oz5g7 {
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: #FFFFFF !important;
    }

    /* Movie Title Styling */
    .movie-title {
        font-size: 16px;
        text-align: center;
        margin-top: 10px;
        color: #FFFFFF;
    }

    /* Adjust container padding */
    .block-container {
        padding: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# App Title
st.markdown('<div class="title-style">Movie Recommendation System</div>', unsafe_allow_html=True)

# Sidebar for movie selection
st.sidebar.title("Choose a Movie")
selected_movie = st.sidebar.selectbox("Select a movie:", movies['title'].values)

if st.sidebar.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.write(f"Top 10 movies similar to **{selected_movie}**:")

    # Create a 2x5 grid layout for movie recommendations
    for i in range(0, 10, 5):  # Loop over rows (2 rows, 5 movies each)
        cols = st.columns(5)  # Create 5 columns for each row
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                movie_id = recommendations.iloc[j]['movie_id']
                poster_url = fetch_poster(movie_id)
                
                with col:
                    st.markdown(
                        f"<img class='poster-style' src='{poster_url}' width='130'><br><div class='movie-title'>{movie_title}</div>", 
                        unsafe_allow_html=True
                    )

# Sidebar footer
st.sidebar.markdown("""
    ### App Information:
    This movie recommendation system suggests movies similar to the one you select. Enjoy exploring new films!
    """)
