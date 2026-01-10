# Task: Rewrite your CSV reader from Exercise 2 with error handling:

# Handle FileNotFoundError - print friendly message if file doesn't exist
# Handle ValueError - skip rows with invalid data and print warning
# Handle IndexError - skip rows with missing columns
# Use finally to print a completion message
# Test it by:

# Reading a file that doesn't exist
# Creating a CSV with invalid data (like text in the shares column)
# Creating a CSV with missing columns
from function_practice import analyze_stock


# **1. Reading CSV Data:**
def opening_reading_analysis(excelfile):
   try:
      with open(excelfile, "r") as file:
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
   except FileNotFoundError:
      print("Portfolio file not found!")
   except ValueError:
      print("Invalid data in file!")
   except IndexError:
      print("Missing data in some rows!")
   except Exception as e:
      print(f"Unexpected error: {e}")
# commented off finally because using with to open, has an automatic close.
# finally:
#     # This ALWAYS runs, even if there's an error
#     if file:
#         file.close()
#         print("File closed")


