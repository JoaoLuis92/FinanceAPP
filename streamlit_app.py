import streamlit as st
import pandas as pd
from compound_calculators import *
from general_functions import *

make_title()

option_choice = st.selectbox("Select the topic below",("Compound calculators", "Others"))

if option_choice == "Compound calculators":

    tab1, tab2 = st.tabs(["Annual compound", "Monthly compound"])

    with tab1:

        annual_compound_block()

    with tab2:

        st.write("Under development! :mechanic: :screwdriver:")

if option_choice == "Others":

    st.write("Under development! :mechanic: :screwdriver:")