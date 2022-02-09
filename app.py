import pandas as pd
import streamlit as st
import numpy
import pickle
import requests

def fetch_poster(movie_id):
   response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=90e5eedac7610751b9995ed5a297b019&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/"+data['poster_path']




def recommend(movie):
    recommend_movie_posters = []
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommend_movie_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
     'Searchh',movies['title'].values)

if st.button('Recommend'):
     name,poster = recommend(selected_movie_name)
     col1, col2, col3 ,col4,col5 = st.columns(5)

     with col1:
         st.text(name[0])
         st.image(poster[0])

     with col2:
         st.text(name[1])
         st.image(poster[1])

     with col3:
         st.text(name[2])
         st.image(poster[2])

     with col4:
         st.text(name[3])
         st.image(poster[3])
     with col5:
         st.text(name[4])
         st.image(poster[4])