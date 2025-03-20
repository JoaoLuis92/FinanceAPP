import streamlit as st

# This function creates the title and the introduction text 

def make_title():
    st.title('Welcome to JL\'s Finance App! :chart_with_upwards_trend:')

    st.header("What can you find here?")
    st.write("""
         I'm a student of Financial Engineering and I am using streamlit to organize the
         materials I have learned in different subjects of my course. \\
         Last update: 20/03/2025        
         """)