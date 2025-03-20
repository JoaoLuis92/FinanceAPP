import streamlit as st
import pandas as pd
from compound_calculators import *

st.title('JL\'s Finance App!')

st.header("What can you find here?")
st.write("Description of what you can find here")

# select box

option_choice = st.selectbox("kunami",("Compound calculators", "others"))

if option_choice == "Compound calculators":

    tab1, tab2 = st.tabs(["Annual compound", "Monthly compound"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:

            monthly_deposit = st.slider("Monthly deposit in EUR", 0, 1000)
            annual_return = st.slider("Annual return in percentage", 0, 30)

        with col2:

            total_time = st.slider("Total time in years", 1, 50)
            initial_investment = st.slider("Initial investment", 1000, 100000)

        results = annual_compound(monthly_deposit, annual_return, total_time, initial_investment)

        chart_data = pd.DataFrame(results[4], columns=["Value"])

        st.line_chart(chart_data)

        st.metric("Final value", results[0], "{:.2%}".format((results[0] - results[1])/results[1]))

        st.write("Value of your investment after ", total_time, " years: ", round(results[0], 0), "€")
        st.write("Total amount invested during this period: ", round(results[1], 0), "€")
        st.write("This corresponds to a profit of ", round(results[2], 0), "€, or ", round(results[3],0), "%!")
