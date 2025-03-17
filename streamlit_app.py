import streamlit as st

st.title('🎈 App Name')

st.write('Oi Mana')

st.header("Annual compound calculator")

def annual_compound(monthly_deposit = 100, annual_return = 8, total_time = 10, initial_investment = 1000):

    current_value = initial_investment
    total_invested = initial_investment

    for i in range(total_time):
        for j in range(12):

            current_value = current_value * (1 + annual_return / 100) ** (1/12) + monthly_deposit
            total_invested += monthly_deposit
    
    total_profit = current_value - total_invested
    relative_profit = total_profit / total_invested * 100

    return (current_value, total_invested, total_profit, relative_profit)

col1, col2 = st.columns(2)

with col1:

    monthly_deposit = st.slider("Monthly deposit in EUR", 0, 1000)
    annual_return = st.slider("Annual return in percentage", 0, 30)

with col2:

    total_time = st.slider("Total time in years", 1, 50)
    initial_investment = st.slider("Initial investment", 1000, 100000)

results = annual_compound(monthly_deposit, annual_return, total_time, initial_investment)

st.write("Value of your investment after ", total_time, " years: ", round(results[0], 0), "€")
st.write("Total amount invested during this period: ", round(results[1], 0), "€")
st.write("This corresponds to a profit of ", round(results[2], 0), "€, or ", round(results[3],0), "%!")
