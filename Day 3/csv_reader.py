# Task 2: Write code that:

# Reads the CSV file
# Parses each stock's data
# Calculates profit for each stock
# Prints a formatted report showing:

# Symbol
# Profit/Loss amount
# Profit percentage


# Calculates and prints total portfolio profit

# Hint: You can reuse your functions from Exercise 1!
from function_practice import analyze_stock
import csv

# **1. Reading CSV Data:**
with open('portfolio.csv', mode='r') as file:
   contents = file.readlines()

header = contents[0].strip().split(',')
total_profit = 0
for line in contents[1:]:
   data = line.strip().split(',')
   symbol = data[0]
   buying_price = float(data[1])
   current_price = float(data[2])
   shares = int(data[3])
   stock_analysis = analyze_stock(symbol, buying_price, current_price, shares)
   total_profit += stock_analysis["profit"]
   print(stock_analysis)
print("====================================")
print(f"Total Portfolio Profit: ${total_profit:.2f}")
print("====================================")


