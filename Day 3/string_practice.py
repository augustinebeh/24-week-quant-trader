# Task: Write a function clean_stock_data(line) that:

# Takes a CSV line like: "  TSLA  , 425.00 ,  435.80  , 100  "
# Returns a cleaned list: ["TSLA", "425.00", "435.80", "100"]
# Steps:

# Strip leading/trailing whitespace
# Split by comma
# Strip whitespace from each part
# Convert symbol to uppercase

def clean_stock_data(line):
   parts = line.split(",")
   new_part = []
   for part in parts:
      new_part.append(part.strip().upper())
   print(new_part)


if __name__ == "__main__":
   clean_stock_data("  TSLA, king ,            monster  , 425.00 ,  435.80  , 100  ")

