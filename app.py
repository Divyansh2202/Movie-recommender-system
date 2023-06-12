import streamlit as st
import pickle
import pandas as pd

# -------------------<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>---------------------------------------------------

# FuNctION FOR MOVIE RECOMMEND ------>>>>

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] # fetching index of movie -->>
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x : x[1])[1:6]  # sorted and 5 movie

    recommended = []

    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended

# -------------------<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>---------------------------------------------------

# -------------------<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>---------------------------------------------------

# IMPORTING MODEL DATA ------>>>>

movies_dict = pickle.load(open('mov_rec.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# -------------------<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>---------------------------------------------------

# TITLE -->>>

st.title("Movie Recommender System")

# -------------------<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>---------------------------------------------------

# SELECT BoX (MOVIE NAME ) ------>>>>

selected_mov_name = st.selectbox(
    'Enter the movie name',
    (movies['title'].values))
st.write('You selected:', selected_mov_name)

# -------------------<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>---------------------------------------------------

# BUTTON FOR MOVIE RECOMMENDATION --->>>>

if st.button('Recommend'):
    recomendation = recommend(selected_mov_name)
    for i in recomendation:
        st.write(i)