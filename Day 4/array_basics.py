import numpy as np

# Task 1: Create NumPy arrays for:

# Stock prices: [425.00, 150.00, 500.00, 380.00, 140.00]
# Shares owned: [100, 50, 75, 60, 80]
# Print both arrays and their attributes (shape, size, dtype)
prices = np.array([425.00, 150.00, 500.00, 380.00, 140.00])
shares = np.array([100, 50, 75, 60, 80])
print(f"--------------------------------------------------- ")

print(f"\n • Task is to 'Print both arrays and their attributes (shape, size, dtype)'")
print(f"Prices array: {prices}")
print(f"Shape:        {prices.shape}")
print(f"Size:         {prices.size}")
print(f"Dtype:        {prices.dtype}")
print(f"Shares array: {shares}")
print(f"Shape:        {shares.shape}")
print(f"Size:         {shares.size}")
print(f"Dtype:        {shares.dtype}\n")


# Task 2: Create arrays using NumPy functions:

# An array of 10 zeros
# An array of 5 ones
# A sequence from 100 to 1000 with step 100
# 7 evenly spaced values between 0 and 100
zeros = np.zeros(10)
ones = np.ones(5)
sequence = np.arange(100, 1000, 100)
linspace = np.linspace(0, 100, 7)
print(f"--------------------------------------------------- ")

print(f"\n • Task is to 'Print 10 zeros'")
print(f"{zeros}")
print(f"\n • Task is to 'Print 5 ones'")
print(f"{ones}")
print(f"\n • Task is to 'Print a sequence from 100 to 1000 with step 100'")
print(f"{sequence}")
print(f"\n • Task is to 'Print 7 evenly spaced values between 0 and 100'")
print(f"{linspace}\n")

# Task 3: Calculate without loops:

# Portfolio value for each stock (price × shares)
individual_value = prices * shares
# Total portfolio value
portfolio_value = individual_value.sum()
# Average stock price
# print(f"Size of individual_value: {individual_value.size}") just testing to see if the .size works with a new variable that contains the multiplicated values
mean_stock_price = prices.sum() / prices.size
# print(f"Median stock price: {mean_stock_price}") testing/exploring to see if output is right.
# Maximum and minimum prices
in_order_prices = np.sort(prices)
print(f"--------------------------------------------------- ")

# print(f"in_order_prices: {in_order_prices}") #just to check whether sort works.
print(f"\n • Task is to 'Print Minimum value'")
print(f"Minimum value: {in_order_prices[0]}")
print(f"\n • Task is to 'Print Maximum value'")
print(f"Maximum value: {in_order_prices[-1]}")
