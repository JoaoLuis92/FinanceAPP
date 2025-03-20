import streamlit as st

# Creates the title and the introduction text 

def make_title():
    st.title('Welcome to JL\'s Finance App! :chart_with_upwards_trend:')

    st.header("What can you find here?")
    st.write("""
         I'm a student of Financial Engineering and I am using streamlit to organize the
         materials I have learned in different subjects of my course. \\
         Last update: 20/03/2025        
         """)
    
# Creates the sidebar and information inside

def make_sidebar():

    with st.sidebar:
        under_development()
    
# Prints a message that says this part is under development

def under_development():

    st.write("Under development! :mechanic: :screwdriver:")