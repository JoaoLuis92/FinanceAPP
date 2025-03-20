import streamlit as st
import pandas as pd
from general_functions import *
from interest_rates import *
from compound_calculators import *



make_title()
make_sidebar()

option_choice = st.selectbox("Select the topic below",("Interest rates", "Compound calculators", "Others"))

if option_choice == "Interest rates":

    InterestRates.interest_rates_block()

if option_choice == "Compound calculators":

    tab1, tab2 = st.tabs(["Annual compound", "Monthly compound"])

    with tab1:

        annual_compound_block()

    with tab2:

        under_development()

if option_choice == "Others":

    under_development()