# Install Streamlit and pyngrok
!pip install streamlit pyngrok --quiet

# Write a simple Streamlit app to recommend movies for a user
with open("app.py", "w") as f:
    f.write("""
import streamlit as st
import pandas as pd

# Sample data
movies = ['Movie A', 'Movie B', 'Movie C']
users = [1, 2, 3]
preds = [[4.2, 4.8, 2.1],
         [3.9, 2.5, 4.6],
         [2.8, 4.7, 3.3]]

st.title("Simple Movie Recommender")

user = st.selectbox("Select User ID", users)

if st.button("Show Recommendations"):
    idx = users.index(user)
    sorted_movies = sorted(zip(movies, preds[idx]), key=lambda x: x[1], reverse=True)
    st.write("Top Recommendations:")
    for movie, score in sorted_movies:
        st.write(f"{movie}: Predicted Rating {score:.2f}")
""")

# Run the app
from pyngrok import ngrok
public_url = ngrok.connect(port=8501)
print(f"Streamlit app running at: {public_url}")

!streamlit run app.py &>/dev/null &
