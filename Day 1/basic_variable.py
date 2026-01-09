# Pick any stock you know
stock_symbol = "TSLA"
buying_price = 425.00
current_market_price = 435.80
shares_owned = 100


ticker_symbol = stock_symbol.upper()
total_investment = buying_price * shares_owned
current_value = current_market_price * shares_owned
current_profit = current_value - total_investment

# if current_profit > 0:
#     is_profitable = True
# else:
#    is_profitable = False
# Alternatively: is_profitable = current_profit > 0
is_profitable = current_profit > 0

profit_percentage = (current_profit / total_investment) * 100

# Modification to calulate what profit would be if the price went up by $10
future_price = current_market_price + 10
future_value = future_price * shares_owned
future_profit = future_value - total_investment
future_profit_percentage = (future_profit / total_investment) * 100

# print ticker symbol (ticker_symbol)
print(f"Ticker Symbol: {stock_symbol.upper()}")
# print buying price (buying_price)
print(f"Buying Price: {buying_price}")
# print current market price (current_market_price)
print(f"Current Market Price: {current_market_price}")
# print shares owned (shares_owned)
print(f"Shares Owned: {shares_owned}")
# print total cost (total_investment)
print(f"Total Investment: ${total_investment:.2f}")
# print current value (current_value)
print(f"Current Value: ${current_value:.2f}")
# print profit or loss (current_profit)
print(f"Profit/Loss: ${current_profit:.2f}")
# print profit percentage (profit_percentage)
print(f"Profit Percentage: {profit_percentage:.2f}%")
# print whether its profitable (is_profitable)
print(f"Is Profitable: {is_profitable}")

# print future profit and future profit percentage
print(f"\nIf the price increased by $10/share...")
print(f"The future profit would be ${future_profit:.2f}")
print(f"The percentage gain in (%) would be {future_profit_percentage:.2f}%")

# Function to encapsulate the logic for reuse in tests
def calculate_trading_metrics(buying_price, current_price, shares):
    """Calculates P&L metrics for a trade."""
    total_investment = buying_price * shares
    current_value = current_price * shares
    current_profit = current_value - total_investment

    is_profitable = current_profit > 0
    profit_percentage = (current_profit / total_investment) * 100 if total_investment != 0 else 0

    return {
        "total_investment": total_investment,
        "current_profit": current_profit,
        "profit_percentage": profit_percentage,
        "is_profitable": is_profitable
    }
