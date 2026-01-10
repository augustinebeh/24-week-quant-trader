from function_practice import categorize_performance, calculate_roi, analyze_stock

# Open and Scrap data from csv file
with open('portfolio.csv', "r") as file:
   contents = file.readlines()

# header = contents[0].strip().split(',')
stock_list = []

# Parse data into stock_analysis
for line in contents[1:]:
   data = line.strip().split(',')
   symbol = data[0]
   buying_price = float(data[1])
   current_price = float(data[2])
   shares = int(data[3])
   stock_analysis = analyze_stock(symbol, buying_price, current_price, shares)
   stock_list.append(stock_analysis)
   print(stock_analysis)

with open('results.csv', "w") as file:
   if stock_list:
      # Writing Header
      keys = stock_list[0].keys()
      file.write(",".join(keys) + "\n")

      # Write Data
      for stock in stock_list:
         formatted_values = []
         for key in keys:
               val = stock[key]

               # Apply formatting based on the key name
               if key in ["investment", "profit", "current_value", "buying_price", "current_price"]:
                  formatted_values.append(f"${val:.2f}")
               elif key == "profit_percentage":
                  formatted_values.append(f"{val:.2f}%")
               else:
                  formatted_values.append(str(val))

         file.write(",".join(formatted_values) + "\n")
