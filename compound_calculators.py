import streamlit as st
import pandas as pd

def annual_compound(monthly_deposit, annual_return, total_time, initial_investment):

        current_value = initial_investment
        total_invested = initial_investment
        data_value = [current_value]
        data_time = [0]

        for i in range(total_time):
            for j in range(12):

                current_value = current_value * (1 + annual_return / 100) ** (1/12) + monthly_deposit
                total_invested += monthly_deposit

                data_value.append(current_value)
                data_time.append((i + j) / 12)
        
        total_profit = current_value - total_invested
        relative_profit = total_profit / total_invested * 100

        return (current_value, total_invested, total_profit, relative_profit, data_value, data_time)

def annual_compound_block():
    st.header("Annual compound calculator", divider = "red")

    st.write("""
            This is the annual compound calculator. It takes four arguments, namely
            the value of your monthly deposit, the annual percentage return, the total
            time in years that the value will be compounding, and the initial deposit.
            """)

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
