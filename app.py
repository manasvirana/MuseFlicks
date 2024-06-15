import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

def fetch_movie_details(movie_name, api_key):
    url = f"http://www.omdbapi.com/?t={movie_name.replace(' ', '+')}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    poster_url = data.get('Poster', None)
    plot = data.get('Plot', 'No plot summary available.')
    return poster_url, plot

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

def resize_image(image_url, width, height):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((width, height))
    return img

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
api_key = '9b8994e7'

page_style = '''
<style>
body {
    background-color:#000033;  /* Light gray background color */
    font-family: 'Inter', sans-serif;  /* Custom font */
    color: #000033;  /* Dark gray color for text */
    margin: 0;
    padding: 0;
}
.stApp {
    background: #000033;  /* White background color for the main container */
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Box shadow for a slight elevation */
    width: 80%;  /* Adjust width as needed */
    max-width: 800px;  /* Adjust max-width as needed */
    margin: 2rem auto;  /* Center the container and provide some margin */
}
.title {
    color: #fff;  /* Dark gray color for title */
    font-size: 2.5rem;  /* Adjust font size */
    margin-bottom: 1rem;  /* Bottom margin for spacing */
    font-weight: bold;  /* Bold font weight for emphasis */
    text-align:center;
}
.heading {
    color: #fff;  /* White color for heading */
    font-size: 1.3rem;  /* Adjust font size */
    margin-top: 1.5rem;  /* Top margin for spacing */
    text-align: left;  /* Align text to the left */
    background-color: #000033;  /* Blackish blue background color */
    padding: 1rem;  /* Padding */
    border-radius: 8px;  /* Rounded corners */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 1.5);  /* Shadow effect */
}

.heading h2 {
    margin-bottom: 1rem;  /* Bottom margin for heading */
    text-align:center;
}

.heading ul {
    list-style-type: none;  /* Remove default list style */
    padding: 0;  /* Remove default padding */
    text-align: left;  /* Remove default text alignment */
}

.heading li {
    margin-bottom: 0.5rem;  /* Bottom margin for list items */
    
}

.selectbox-container {
    margin-top: 1.5rem;  /* Top margin for select box */
}
.stButton>button {
    background-color: #333;  /* Blackish blue background color for buttons */
    color: #fff;  /* White text color for buttons */
    border-radius: 4px;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #ffffff;  /* Darker shade of blue on hover */
}
.recommendation {
    margin-top: 2rem;  /* Top margin for recommendations */
}
.recommendation h3 {
    font-size: 1.2rem;  /* Font size for recommendation headings */
    margin-bottom: 0.5rem;  /* Bottom margin for recommendation headings */
    color: #333;  /* Dark gray color for recommendation headings */
}
.recommendation a {
    color: #007bff;  /* Blue color for links */
    text-decoration: none;  /* Remove underline from links */
}
.recommendation a:hover {
    text-decoration: underline;  /* Underline on hover for links */
}
.movie-info {
    margin-top: 1rem;  /* Top margin for movie info */
}
.movie-info img {
    max-width: 100%;  /* Ensure images don't overflow container */
    border-radius: 8px;  /* Rounded corners for images */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Box shadow for images */
}
.movie-info p {
    font-size: 1rem;  /* Font size for movie info */
    line-height: 1.5;  /* Line height for readability */
    margin-top: 0.5rem;  /* Top margin for movie info */
}
</style>
'''

st.markdown(page_style, unsafe_allow_html=True)

# Centered title with custom font and styling
st.markdown('''
<h1 class='title'>MuseFlicks</h1>
<div class="heading">
    <h2>Explore Movie Recommendations.</h2>
    <ul>
        <li>1.Get the most similar movies based on your selection.</li>
        <li>2.Access Google links to gather comprehensive information about the recommended movies.</li>
        <li>3.Explore through brief plot summaries, posters, and other relevant information.</li>
        <li>4.Enjoy a seamless browsing experience and discover your next favorite movie effortlessly.</li>
    </ul>
</div>
''', unsafe_allow_html=True)

# Heading below the title


option = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(option)
    for movie_name in recommendations:
        google_search_url = f"https://www.google.com/search?q={movie_name.replace(' ', '+')}+movie"
        poster_url, plot = fetch_movie_details(movie_name, api_key)
        st.markdown(f"<div class='recommendation'><h3><a href='{google_search_url}' target='_blank'>{movie_name}</a></h3></div>", unsafe_allow_html=True)
        if poster_url:
            resized_image = resize_image(poster_url, width=700, height=500)  # Adjust width and height
            st.image(resized_image, caption=plot, use_column_width=True)
        else:
            st.write(plot)

