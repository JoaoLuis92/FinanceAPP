import streamlit as st
import pandas as pd
from general_functions import *

class InterestRates:

    tabs = ["Simple rate",
            "Yearly compound",
            "Periodic compound",
            "Continuous compound",
            "Rate converter"]

    @classmethod
    def interest_rates_block(cls):

        cls.interest_rates_info()

        tab1, tab2, tab3, tab4, tab5 = st.tabs(cls.tabs)
        
        with tab1:
            cls.simple_rate_block()

        with tab2:
            cls.yearly_compound_block()

        with tab3:
            cls.periodic_compound_block()

        with tab4:
            cls.continuous_compound_block()

        with tab5:
            cls.rate_converter_block()

    @classmethod
    def simple_rate_block(cls):
        st.dataframe(cls.simple_rate(1000, 0.08, 10))

    def yearly_compound_block():
        pass

    def periodic_compound_block():
        pass

    def continuous_compound_block():
        pass

    def rate_converter_block():
        pass

    # Information blocks

    def interest_rates_info():
        under_development()

    def simple_rate_info():
        under_development()

    def yearly_compound_info():
        under_development()

    def periodic_compound_info():
        under_development()

    def continuos_compound_info():
        under_development()

    def rate_converter_info():
        under_development()

    # Calculations

    def simple_rate(present_value: float, interest_rate: float, number_periods: int):

        data = [[0, present_value]]

        interest_value = present_value * interest_rate

        for i in range(number_periods):
            present_value += interest_value
            data.append([i + 1, present_value])

        df = pd.DataFrame(data, columns = ["Time periods", "Value"], index = "Time periods")

        return df
    