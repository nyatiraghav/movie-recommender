import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x:x[1])[1:6]
    recommended_movies_names = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies_names, recommended_movies_poster

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Lets see what would you like to Watch! ',
    movies['title'].values)

st.write('You selected:', selected_movie_name)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

custom_styles = """
    <div class="credits"> Presented by: <a href="https://www.linkedin.com/in/rnyati/" target="_blank"> Raghav Nyati</a></div>
    
    <style>
        .credits {
            font-weight: bold;
            margin-top: 60px;
            background-color: white;
            color: black;
            font-family: Arial, sans-serif;
        }
        .streamlit button {
            background-color: #008080;
            color: white;
        }
        /* Add more styles as needed */
    </style>
    
"""

# Apply styles using st.markdown
st.markdown(custom_styles, unsafe_allow_html=True)