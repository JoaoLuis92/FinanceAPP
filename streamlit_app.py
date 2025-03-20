import streamlit as st
import pandas as pd
from compound_calculators import *

st.title(':moneybag: Welcome to JL\'s Finance App! :chart_with_upwards_trend:')

st.header("What can you find here?")
st.write("""
         I'm a student of Financial Engineering and I am using streamlit to organize the
         materials I have learned in different subjects of my course.          
         """)

# select box

option_choice = st.selectbox("Select the topic below",("Compound calculators", "others"))

if option_choice == "Compound calculators":

    tab1, tab2 = st.tabs(["Annual compound", "Monthly compound"])

    with tab1:
        col1, col2, col3, col4 = st.columns(4)

        with col1:

            monthly_deposit = st.number_input("Monthly deposit in EUR", 
                                              min_value = 0, 
                                              max_value = 5000,
                                              value = 1000,
                                              step = 100)
            
        with col2:
            
            annual_return = st.number_input("Annual return in \%", 
                                              min_value = 0, 
                                              max_value = 50,
                                              value = 10,
                                              step = 1)
            
        with col3:
            
            total_time = st.number_input("Total time in years", 
                                              min_value = 1, 
                                              max_value = 50,
                                              value = 10,
                                              step = 1)
            
        with col4:
            
            initial_investment = st.number_input("Initial deposit",
                                                 min_value = 0,
                                                 max_value = 50000,
                                                 value = 1000,
                                                 step = 1000)

        results = annual_compound(monthly_deposit, annual_return, total_time, initial_investment)

        chart_data = pd.DataFrame(results[4], columns=["Value"])

        st.line_chart(chart_data)

        st.metric("Final value", results[0], "{:.2%}".format((results[0] - results[1])/results[1]))

        st.write("Value of your investment after ", total_time, " years: ", round(results[0], 0), "€")
        st.write("Total amount invested during this period: ", round(results[1], 0), "€")
        st.write("This corresponds to a profit of ", round(results[2], 0), "€, or ", round(results[3],0), "%!")
