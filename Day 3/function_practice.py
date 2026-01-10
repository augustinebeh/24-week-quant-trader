# **Task 1:** Write a function `calculate_roi(investment, current_value)` that:
# - Returns the ROI (Return on Investment) percentage
# - Formula: `((current_value - investment) / investment) * 100`
# - Handles division by zero (return 0 if investment is 0)
def calculate_roi(investment, current_value):
   return ((current_value - investment) / investment) * 100 if investment != 0 else 0

# **Task 2:** Write a function `categorize_performance(profit_percentage)` that:
# - Takes profit percentage as input
# - Returns a string:
#   - "Excellent" if profit_pct >= 10
#   - "Good" if profit_pct >= 5
#   - "Fair" if profit_pct >= 0
#   - "Loss" if profit_pct < 0
def categorize_performance(profit_percentage):
   if profit_percentage >= 10:
      return "Excellent"
   elif profit_percentage >= 5:
      return "Good"
   elif profit_percentage >= 0:
      return "Fair"
   else:
      return "Loss"


# **Task 3:** Write a function `analyze_stock(symbol, buying_price, current_price, shares)` that:
# - Returns a dictionary with all metrics (cost, value, profit, profit_pct, category)
# - Uses the functions from Task 1 and 2
# - Example return: `{"symbol": "TSLA", "cost": 5000, "profit": 500, ...}`
def analyze_stock(symbol, buying_price, current_price, shares):
   total_investment = buying_price * shares
   current_value = current_price * shares
   current_profit = current_value - total_investment
   profit_percentage = calculate_roi(total_investment, current_value)
   performance_category = categorize_performance(profit_percentage)

   return {
      "symbol": symbol,
      "cost": total_investment,
      "current_value": current_value,
      "profit": current_profit,
      "profit_percentage": profit_percentage,
      "category": performance_category
   }

if __name__ == "__main__":
   stock_analysis = analyze_stock("TSLA", 400.00, 450.00, 234)
   for key, value in stock_analysis.items():
      if key in ["cost", "current_value", "profit"]:
         print(f"{key}: ${value:.2f}")
      elif key == "profit_percentage":
         print(f"{key}: {value:.2f}%")
      else:
         print(f"{key}: {value}")
