
# returns metrics dictionary
def calculate_stock_metrics(stock_dict):
    # Extract values from the dictionary
    buying_price = stock_dict.get("buying_price", 0)
    current_price = stock_dict.get("current_price", 0)
    shares = stock_dict.get("shares", 0)

    investment = buying_price * shares
    current_value = current_price * shares
    current_profit = current_value - investment
    is_profitable = current_profit > 0
    profit_percentage = (current_profit / investment) * 100 if investment != 0 else 0

    return {
        "investment": investment,
        "current_value": current_value,
        "current_profit": current_profit,
        "profit_percentage": profit_percentage,
        "is_profitable": is_profitable
    }


# returns list of stock dictionaries
def read_portfolio(excelfile):
   stocks_list = []
   try:
      with open(excelfile, "r") as file:
         contents = file.readlines()

      header = contents[0].strip().split(',')
      total_profit = 0

      for line in contents[1:]:
         try:
            data = line.strip().split(',')

            stock_dictionary = {
               "symbol": data[0],
               "buying_price": float(data[1]),
               "current_price": float(data[2]),
               "shares": int(data[3])
            }
            metrics = calculate_stock_metrics(stock_dictionary)
            stock_dictionary.update(metrics)
            stocks_list.append(stock_dictionary)
            total_profit += metrics["current_profit"]
         except (ValueError, IndexError):
                continue
      print("====================================")
      print(f"Total Portfolio Profit: ${total_profit:.2f}")
      print("====================================")
      return stocks_list
   except FileNotFoundError:
      print("Portfolio file not found!")
   except ValueError:
      print("Invalid data in file!")
   except IndexError:
      print("Missing data in some rows!")



# - writes CSV report
def write_report_csv(stocks_data, filename):
   if not stocks_data:
        print("No data to write to CSV.")
        return
   with open(filename, "w") as file:
      if stocks_data:
         keys = stocks_data[0].keys()
         file.write(",".join(keys) + "\n")

         for stock in stocks_data:
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
   print(f"✅ Report saved to {filename}")


# writes text summary
def write_summary_txt(stocks_data, filename):
    if not stocks_data: return

    total_invested = sum(s['investment'] for s in stocks_data)
    total_value = sum(s['current_value'] for s in stocks_data)
    total_profit = total_value - total_invested
    total_profit_percentage = (total_profit / total_invested) * 100

    with open(filename, "w") as file:
        file.write("=============================\n")
        file.write("PORTFOLIO SUMMARY REPORT\n")
        file.write("=============================\n")
        file.write(f"Total Investment:  ${total_invested:.2f}\n")
        file.write(f"Current Value:     ${total_value:.2f}\n")
        file.write(f"Net Profit/Loss:   ${total_profit:.2f}\n")
        file.write(f"Profit/Loss(%):    {total_profit_percentage:.2f}%\n")

    print(f"✅ Summary saved to {filename}")

# Orchestration
if __name__ == "__main__":
    input_file = 'portfolio_data.csv'

    portfolio_data = read_portfolio(input_file)

    if portfolio_data:
        write_report_csv(portfolio_data, 'portfolio_report.csv')
        write_summary_txt(portfolio_data, 'portfolio_summary.txt')
    else:
        print("Process aborted: No valid data found.")
