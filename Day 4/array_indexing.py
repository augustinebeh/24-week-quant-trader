import numpy as np
from vectorized_operations import further_analysis

print("\n")

# Using array indexing:

# Task 1: Create NumPy arrays for:
# Hint: Use np.argsort() for sorting by another array
symbols = np.array(['TSLA', 'AAPL', 'NVDA', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NFLX'])
prices = np.array([435.80, 165.50, 520.30, 395.20, 142.50, 178.20, 485.30, 625.40])
profits = np.array([1080, 775, 1522, 912, 200, -150, 350, -200])

title = "Using array indexing"
print(f"  •-._.-^-  {title.upper()}  -^._.-•  ")
print("-------------------------------------------")
# Get the first 3 symbols
first_three_symbols = symbols[:3]
print("first_three_symbols:", first_three_symbols) # ['TSLA' 'AAPL' 'NVDA']

# Get the last 3 prices
last_three_prices = prices[-3:]
print("last_three_prices:  ", last_three_prices) # [178.2 485.3 625.4]

# Get every other stock (0, 2, 4, 6)
every_other = symbols[::2]
print("every_other:        ", every_other) # ['TSLA' 'NVDA' 'GOOGL' 'META']

# Get all symbols where profit > 500
symbols_above_500 = symbols[prices > 500]
print("symbols_above_500:  ", symbols_above_500) # ['NVDA' 'NFLX']

# Get prices where profits are negative
negative_prices = prices[profits < 0]
print("negative_prices:    ", negative_prices) # [178.2 625.4]

# Count how many stocks have profit between 500 and 1500
mask_500_1500 = prices[(profits >= 500) & (profits <= 1500)]
print("mask_500_1500:      ", mask_500_1500) # [435.8 165.5 395.2]
between_500_1500 = mask_500_1500.size
print("between_500_1500:   ",between_500_1500) # 3

# Find indices of stocks with losses
indices_of_losers = np.where(profits < 0)[0]
print("indices_of_losers:  ", indices_of_losers) #  [5 7]

# Get symbols of top 3 most profitable stocks
inorder_profitable = np.argsort(profits)[-3:]
print("inorder_profitable: ", inorder_profitable) #  [3 0 2]
selected = symbols[inorder_profitable] 
print("selected:           ",selected) # ['MSFT' 'TSLA' 'NVDA']
