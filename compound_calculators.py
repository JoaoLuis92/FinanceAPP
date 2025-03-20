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