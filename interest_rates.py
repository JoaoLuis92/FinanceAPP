import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from general_functions import *

class InterestRates:

    tabs = ["Simple rate",
            "Yearly compound",
            "Periodic compound",
            "Continuous compound",
            "Rate converter"]
    
    # Block structure

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

    # Contents of each block

    @classmethod
    def simple_rate_block(cls):

        cls.simple_rate_info()
        (present_value, interest_rate, number_periods) = cls.simple_rate_inputs()
        results_dataframe = cls.simple_rate_function(present_value, interest_rate, number_periods)
        
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(results_dataframe, height = 250, width = 300)
            st.caption("Total value, returns, and percentage returns.")

        with col2:
            plt.figure(1)
            plt.plot(results_dataframe.index, results_dataframe["Value (€)"], marker='o', linestyle='-')
            plt.xlabel("Number of time periods")
            plt.ylabel("Total value in EUR")
            plt.ylim(results_dataframe["Value (€)"].min(), results_dataframe["Value (€)"].max())
            st.pyplot(plt)
            st.caption("Total value as a function of the number of time periods.")

    @classmethod
    def yearly_compound_block(cls):

        cls.yearly_compound_info()
        (present_value, interest_rate, number_periods) = cls.yearly_compound_inputs()
        results_dataframe = cls.yearly_compound_function(present_value, interest_rate, number_periods)
        
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(results_dataframe, height = 250, width = 300)
            st.caption("Total value, returns, and percentage returns.")

        with col2:
            plt.figure(2)
            plt.plot(results_dataframe.index, results_dataframe["Value (€)"], marker='o', linestyle='-')
            plt.xlabel("Number of time periods")
            plt.ylabel("Total value in EUR")
            plt.ylim(results_dataframe["Value (€)"].min(), results_dataframe["Value (€)"].max())
            st.pyplot(plt)
            st.caption("Total value as a function of the number of time periods.")

    @classmethod
    def periodic_compound_block(cls):

        cls.periodic_compound_info()
        (present_value, interest_rate, number_periods, payment_frequency) = cls.periodic_compound_inputs()
        results_dataframe = cls.periodic_compound_function(present_value, interest_rate, number_periods, payment_frequency)
        
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(results_dataframe, height = 250, width = 300)
            st.caption("Total value, returns, and percentage returns.")

        with col2:
            plt.figure(3)
            plt.plot(results_dataframe.index, results_dataframe["Value (€)"], marker='o', linestyle='-')
            plt.xlabel("Number of time periods")
            plt.ylabel("Total value in EUR")
            plt.ylim(results_dataframe["Value (€)"].min(), results_dataframe["Value (€)"].max())
            st.pyplot(plt)
            st.caption("Total value as a function of the number of time periods.")

    @classmethod
    def continuous_compound_block(cls):

        cls.continuous_compound_info()
        (present_value, interest_rate, number_periods) = cls.continuous_compound_inputs()
        results_dataframe = cls.continuous_compound_function(present_value, interest_rate, number_periods)
        
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(results_dataframe, height = 250, width = 300)
            st.caption("Total value, returns, and percentage returns.")

        with col2:
            plt.figure(4)
            plt.plot(results_dataframe.index, results_dataframe["Value (€)"], marker='o', linestyle='-')
            plt.xlabel("Number of time periods")
            plt.ylabel("Total value in EUR")
            plt.ylim(results_dataframe["Value (€)"].min(), results_dataframe["Value (€)"].max())
            st.pyplot(plt)
            st.caption("Total value as a function of the number of time periods.")

    @classmethod
    def rate_converter_block(cls):
        
        cls.rate_converter_info()
        (old_interest_rate, old_frequency, new_frequency) = cls.rate_converter_inputs()
        interest_rate = cls.rate_converter_function(old_interest_rate, old_frequency, new_frequency)

        st.write("The new interest rate after conversion is", interest_rate)

    # Inputs for each function

    def simple_rate_inputs():
        
        col1, col2, col3 = st.columns(3)

        with col1:
            present_value = st.number_input("Initial deposit in EUR", 
                                            min_value = 0, 
                                            max_value = 50000,
                                            value = 1000,
                                            step = 100,
                                            key = "simple rate present value")
        with col2:
            interest_rate = st.number_input("Interest rate in %", 
                                            min_value = 0, 
                                            max_value = 50,
                                            value = 10,
                                            step = 1,
                                            key = "simple rate interest rate")
            
        with col3:
            number_periods = st.number_input("Number of periods",
                                             min_value = 1,
                                             max_value = 50,
                                             value = 10,
                                             step = 1,
                                             key = "simple rate number periods")
            
        return (present_value, interest_rate, number_periods)
    
    def yearly_compound_inputs():
        
        col1, col2, col3 = st.columns(3)

        with col1:
            present_value = st.number_input("Initial deposit in EUR", 
                                            min_value = 0, 
                                            max_value = 50000,
                                            value = 1000,
                                            step = 100,
                                            key = "yearly compound present value")
        with col2:
            interest_rate = st.number_input("Interest rate in %", 
                                            min_value = 0, 
                                            max_value = 50,
                                            value = 10,
                                            step = 1,
                                            key = "yearly compound interest rate")
            
        with col3:
            number_periods = st.number_input("Number of periods",
                                             min_value = 1,
                                             max_value = 50,
                                             value = 10,
                                             step = 1,
                                             key = "yearly compound number periods")
            
        return (present_value, interest_rate, number_periods)

    def periodic_compound_inputs():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            present_value = st.number_input("Initial deposit in EUR", 
                                            min_value = 0, 
                                            max_value = 50000,
                                            value = 1000,
                                            step = 100,
                                            key = "periodic compound present value")
        with col2:
            interest_rate = st.number_input("Interest rate in %", 
                                            min_value = 0, 
                                            max_value = 50,
                                            value = 10,
                                            step = 1,
                                            key = "periodic compound interest rate")
            
        with col3:
            number_periods = st.number_input("Number of periods",
                                             min_value = 1,
                                             max_value = 50,
                                             value = 10,
                                             step = 1,
                                             key = "periodic compound cumber periods")
            
        with col4:
            payment_frequency = st.number_input("Payment frequency",
                                                min_value = 1,
                                                max_value = 12,
                                                value = 3,
                                                step = 1,
                                                key = "periodic compound payment frequency")
            
        return (present_value, interest_rate, number_periods, payment_frequency)
    
    def continuous_compound_inputs():
        
        col1, col2, col3 = st.columns(3)

        with col1:
            present_value = st.number_input("Initial deposit in EUR", 
                                            min_value = 0, 
                                            max_value = 50000,
                                            value = 1000,
                                            step = 100,
                                            key = "continuous compound present value")
        with col2:
            interest_rate = st.number_input("Interest rate in %", 
                                            min_value = 0, 
                                            max_value = 50,
                                            value = 10,
                                            step = 1,
                                            key = "continuous compound interest rate")
            
        with col3:
            number_periods = st.number_input("Number of periods",
                                             min_value = 1,
                                             max_value = 50,
                                             value = 10,
                                             step = 1,
                                             key = "continuous compound number periods")
            
        return (present_value, interest_rate, number_periods)

    def rate_converter_inputs():

        col1, col2, col3 = st.columns(3)

        with col1:
            old_interest_rate = st.number_input("Interest rate in %",
                                                min_value = 0, 
                                                max_value = 50,
                                                value = 10,
                                                step = 1,
                                                key = "rate converter old rate")
        
        with col2:
            old_frequency = st.number_input("Current payments per year",
                                            min_value = 1,
                                            max_value = 12,
                                            value = 3,
                                            step = 1,
                                            key = "rate converter old frequency")
            
        with col3:
            new_frequency = st.number_input("New payments per year",
                                            min_value = 1,
                                            max_value = 12,
                                            value = 4,
                                            step = 1,
                                            key = "rate converter new frequency")
            
        return (old_interest_rate, old_frequency, new_frequency)

    # Implementation of the mathematical functions

    def simple_rate_function(present_value: float, interest_rate: float, number_periods: int):

        data = [[0, present_value, 0, 0]]

        for i in range(number_periods):
            current_value = present_value * (1 + interest_rate * (i + 1) / 100)
            returns_value = current_value - present_value
            returns_percentage = returns_value / present_value * 100
            data.append([i + 1, current_value, returns_value, returns_percentage])

        df = pd.DataFrame(data, columns = ["Time", "Value (€)", "Return (€)", "Return (%)"]).set_index("Time")

        return df
    
    def yearly_compound_function(present_value: float, interest_rate: float, number_periods: int):
    
        data = [[0, present_value, 0, 0]]

        for i in range(number_periods):
            current_value = present_value * (1 + interest_rate / 100) ** (i + 1)
            returns_value = current_value - present_value
            returns_percentage = returns_value / present_value * 100
            data.append([i + 1, current_value, returns_value, returns_percentage])

        df = pd.DataFrame(data, columns = ["Time", "Value (€)", "Return (€)", "Return (%)"]).set_index("Time").apply(lambda x: round(x, 2))

        return df
    
    def periodic_compound_function(present_value: float, interest_rate: float, number_periods: int, payment_frequency: int):

        data = [[0, present_value, 0, 0]]

        total_payments = number_periods * payment_frequency

        for i in range(total_payments):
            current_value = present_value * (1 + interest_rate / (payment_frequency * 100)) ** (i + 1)
            returns_value = current_value - present_value
            returns_percentage = returns_value / present_value * 100
            data.append([i + 1, current_value, returns_value, returns_percentage])

        df = pd.DataFrame(data, columns = ["Time", "Value (€)", "Return (€)", "Return (%)"]).set_index("Time").apply(lambda x: round(x, 2))

        return df
    
    def continuous_compound_function(present_value: float, interest_rate: float, number_periods: int):

        data = [[0, present_value, 0, 0]]

        for i in range(number_periods):
            current_value = present_value * np.exp(interest_rate * (i + 1) / 100)
            returns_value = current_value - present_value
            returns_percentage = returns_value / present_value * 100
            data.append([i + 1, current_value, returns_value, returns_percentage])

        df = pd.DataFrame(data, columns = ["Time", "Value (€)", "Return (€)", "Return (%)"]).set_index("Time").apply(lambda x: round(x, 2))

        return df
    
    def rate_converter_function(old_interest_rate: float, old_frequency: int, new_frequency: int):

        new_interest_rate = new_frequency * ((1 + old_interest_rate / (old_frequency * 100)) ** (old_frequency / new_frequency) - 1) * 100

        return new_interest_rate
    
    # Information about the topics

    def interest_rates_info():
        under_development()

    def simple_rate_info():
        under_development()

    def yearly_compound_info():
        under_development()

    def periodic_compound_info():
        under_development()

    def continuous_compound_info():
        under_development()

    def rate_converter_info():
        under_development()