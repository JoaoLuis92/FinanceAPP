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
        st.markdown("""This section deals with interest rates! Here you can calculate how the value of your asset
                    evolves over time for different types of interest rates and with different payment periods, 
                    and also calculate how interest rates change when the payment periods are altered.""")
        st.markdown("""
                    - **Simple rate:** calculation of simple interest rates over a given time period;
                    - **Yearly compound:** calculation of yearly compounded interest rates over a given time period;
                    - **Periodic compound:** calculation of interest rates that compound several times per year;
                    - **Continuous compound:** calculation of interest rates that compound continuously over time;
                    - **Rate converter:** conversion of interest rates between two different payment frequencies.
                    """)

    def simple_rate_info():
        st.markdown("""A simple interest rate means that the value of the interest remains a constant fraction of
                    the initial value of the asset over time. This means that you do not earn interest on the 
                    interest previously received. The forward value of an asset that pays a simple 
                    interest rate is given by:""")
        st.latex(r"FV = PV\left(1+nr\right)")
        st.markdown("""
                    - $FV$: forward value;
                    - $PV$: present value;
                    - $r$: simple interest rate;
                    - $n$: number of payments.
                    """)

    def yearly_compound_info():
        st.markdown("""A yearly compounded interest rate means that the interest is paid yearly and that you can earn
                    interest on the interest previously received. As such, the interest rate increases with time. The
                    forward value of an asset that compounds yearly is given by:""")
        st.latex(r"FV = PV\left(1+r\right)^n")
        st.markdown("""
                    - $FV$: forward value;
                    - $PV$: present value;
                    - $r$: interest rate;
                    - $n$: number of years.
                    """)

    def periodic_compound_info():
        st.markdown("""A periodically compounded interest rate means that the interest is paid several times a year and
                    that you earn interest on the interest previously received. As such, the interest rate increases with
                    time, and faster than the yearly compound. The forward value of an asset that compounds periodically
                    over the year is given by:""")
        st.latex(r"FV = PV\left(1+\frac{r}{m}\right)^{m\times n}")
        st.markdown("""
                    - $FV$: forward value;
                    - $PV$: present value;
                    - $r$: interest rate;
                    - $m$: payments per year;
                    - $n$: number of years.
                    """)

    def continuous_compound_info():
        st.markdown("""A continuously compounded interest rate means that the interest is paid at every instant in time.
                    This can be obtained as the limit of periodic compound when the number of payments per year goes to
                    infinity. As such, this is the fastest growing interest rate. The forward value of an asset that compounds
                    continuously is given by:""")
        st.latex(r"FV = PV \times e^{r\times n}")
        st.markdown("""
                    - $FV$: forward value;
                    - $PV$: present value;
                    - $r$: interest rate;
                    - $n$: number of years.
                    """)

    def rate_converter_info():
        st.markdown("""If interest is paid at different frequencies during the year, the resulting compounded value
                    changes. It is possible to calculate the required interest rate such that the compounded value
                    remains the same after the payment frequency is changed. The conversion is as follows:""")
        st.latex(r"r_m=m\left[\left(1+\frac{r_n}{n}\right)^{\frac{n}{m}}-1\right]")
        st.markdown("""
                    - $r_m$: interest rate with new payment frequency;
                    - $r_n$: interest rate with old payment frequency;
                    - $m$: new frequency of payments per year;
                    - $n$: old frequency of payments per year;
                    """)