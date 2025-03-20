import streamlit as st
import pandas as pd
import numpy as np
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

        cls.simple_rate_info()
        (present_value, interest_rate, number_periods) = cls.simple_rate_inputs()
        results_dataframe = cls.simple_rate_function(present_value, interest_rate, number_periods)
        
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(results_dataframe)

        with col2:
            st.line_chart(results_dataframe, 
                      x_label = "Number of time periods",
                      y_label = "Value in EUR",
                      width = 600,
                      height = 400)

    @classmethod
    def yearly_compound_block(cls):
        pass

    @classmethod
    def periodic_compound_block(cls):
        pass

    @classmethod
    def continuous_compound_block(cls):
        pass

    @classmethod
    def rate_converter_block(cls):
        pass

    # Information about the topics

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

    # Necessary inputs for the functions

    def simple_rate_inputs():
        
        col1, col2, col3 = st.columns(3)

        with col1:
            present_value = st.number_input("Initial deposit in EUR", 
                                            min_value = 0, 
                                            max_value = 50000,
                                            value = 1000,
                                            step = 100)
        with col2:
            interest_rate = st.number_input("Interest rate in %", 
                                            min_value = 0, 
                                            max_value = 50,
                                            value = 10,
                                            step = 1)
            
        with col3:
            number_periods = st.number_input("Number of periods",
                                             min_value = 1,
                                             max_value = 50,
                                             value = 10,
                                             step = 1)
            
        return (present_value, interest_rate, number_periods)

    def yearly_compound_inputs():
        pass

    def periodic_compound_inputs():
        pass

    def continuous_compound_inputs():
        pass

    def rate_converter_inputs():
        pass

    # Implementation of the mathematical expressions

    def simple_rate_function(present_value: float, interest_rate: float, number_periods: int):

        data = [[0, present_value]]

        for i in range(number_periods):
            data.append([i + 1, present_value * (1 + interest_rate * (i + 1) / 100)])

        df = pd.DataFrame(data, columns = ["Time periods", "Value"]).set_index("Time periods")

        return df
    
    def yearly_compound_function(present_value: float, interest_rate: float, number_periods: int):
    
        data = [[0, present_value]]

        for i in range(number_periods):
            data.append([i + 1, present_value * (1 + interest_rate / 100) ** (i + 1)])

        df = pd.DataFrame(data, columns = ["Time periods", "Value"]).set_index("Time periods")

        return df
    
    def periodic_compound_function(present_value: float, interest_rate: float, number_periods: int, payment_frequency: int):

        data = [[0, present_value]]

        total_payments = number_periods * payment_frequency

        for i in range(total_payments):
            data.append([i + 1, present_value * (1 + interest_rate / (payment_frequency * 100)) ** (i + 1)])

        df = pd.DataFrame(data, columns = ["Time periods", "Value"]).set_index("Time periods")

        return df
    
    def continuous_compound_function(present_value: float, interest_rate: float, number_periods: int):

        data = [[0, present_value]]

        for i in range(number_periods):
            data.append([i + 1, present_value * np.exp(interest_rate * (i + 1) / 100)])

        df = pd.DataFrame(data, columns = ["Time periods", "Value"]).set_index("Time periods")

        return df
    
    def rate_converter_function(old_interest_rate: float, old_frequency: int, new_frequency: int):

        new_interest_rate = new_frequency * ((1 + old_interest_rate / (old_frequency * 100)) ** (old_frequency / new_frequency) - 1) * 100

        return new_interest_rate