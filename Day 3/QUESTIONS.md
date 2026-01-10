# Day 3 Practice Questions

## 📝 Self-Assessment Questions

After completing Day 3, test your understanding with these questions. Try to answer them without looking back at your code!

---

## Part 1: Functions

### Question 1: Print vs Return
**Q:** What's the difference between these two functions?

```python
def function_a(x):
    print(x * 2)

def function_b(x):
    return x * 2

result_a = function_a(5)
result_b = function_b(5)
```

What are the values of `result_a` and `result_b`?

<details>
<summary>Click to see answer</summary>

**A:**
- `result_a` = `None` (function_a prints but doesn't return anything)
- `result_b` = `10` (function_b returns the calculated value)

**Key Difference:**
- `print()` displays output to console but doesn't give a value back
- `return` sends a value back to the caller that can be stored and used

**Output to console:**
- `function_a(5)` prints `10` to screen
- `function_b(5)` prints nothing (but returns 10)
</details>

---

### Question 2: Default Parameters
**Q:** What happens if you define a function like this?

```python
def my_function(a=10, b):
    return a + b
```

<details>
<summary>Click to see answer</summary>

**A:** **SyntaxError!** 

You cannot have a required parameter (b) after a default parameter (a=10).

**Correct versions:**
```python
# Option 1: All defaults after all required
def my_function(b, a=10):
    return a + b

# Option 2: All parameters have defaults
def my_function(a=10, b=20):
    return a + b
```

**Rule:** Parameters with defaults must come AFTER parameters without defaults.
</details>

---

### Question 3: Multiple Returns
**Q:** What does this function return?

```python
def calculate_metrics(price, shares):
    cost = price * shares
    tax = cost * 0.1
    total = cost + tax
    return cost, tax, total

result = calculate_metrics(100, 10)
```

What type is `result` and how do you access the individual values?

<details>
<summary>Click to see answer</summary>

**A:** `result` is a **tuple** containing three values: `(1000, 100.0, 1100.0)`

**Accessing values:**

**Method 1: Unpacking**
```python
cost, tax, total = calculate_metrics(100, 10)
print(cost)   # 1000
print(tax)    # 100.0
print(total)  # 1100.0
```

**Method 2: Index access**
```python
result = calculate_metrics(100, 10)
print(result[0])  # 1000 (cost)
print(result[1])  # 100.0 (tax)
print(result[2])  # 1100.0 (total)
```

**Method 3: Return dictionary (more readable)**
```python
def calculate_metrics(price, shares):
    cost = price * shares
    tax = cost * 0.1
    total = cost + tax
    return {"cost": cost, "tax": tax, "total": total}

result = calculate_metrics(100, 10)
print(result["cost"])  # 1000
```
</details>

---

## Part 2: File I/O

### Question 4: With Statement
**Q:** What's the advantage of using `with open()` instead of `file = open()`?

```python
# Method A
file = open("data.csv", "r")
content = file.read()
file.close()

# Method B
with open("data.csv", "r") as file:
    content = file.read()
```

<details>
<summary>Click to see answer</summary>

**A:** The `with` statement **automatically closes the file**, even if an error occurs.

**Problem with Method A:**
```python
file = open("data.csv", "r")
content = file.read()
result = int(content)  # ValueError if content isn't a number!
file.close()  # This line never runs if error occurs above!
```

**Method B handles this:**
```python
with open("data.csv", "r") as file:
    content = file.read()
    result = int(content)  # Even if error here...
# ...file is STILL automatically closed!
```

**Benefits:**
1. Automatic cleanup
2. Works even with exceptions
3. Cleaner, more readable code
4. No need to remember `file.close()`
</details>

---

### Question 5: File Modes
**Q:** What's the difference between "w" and "a" modes when opening a file?

```python
# Mode "w"
with open("output.txt", "w") as f:
    f.write("Hello\n")

# Mode "a"  
with open("output.txt", "a") as f:
    f.write("World\n")
```

<details>
<summary>Click to see answer</summary>

**A:**

**"w" mode (write):**
- Creates new file or **OVERWRITES existing file completely**
- Deletes all previous content
- Starts writing from beginning

**"a" mode (append):**
- Creates new file if doesn't exist
- **Adds to end of existing file** without deleting
- Preserves previous content

**Example:**
```python
# File doesn't exist initially

# First operation (w mode)
with open("test.txt", "w") as f:
    f.write("Line 1\n")
# File now contains: "Line 1\n"

# Second operation (w mode) - OVERWRITES!
with open("test.txt", "w") as f:
    f.write("Line 2\n")
# File now contains: "Line 2\n" (Line 1 is gone!)

# Third operation (a mode) - APPENDS!
with open("test.txt", "a") as f:
    f.write("Line 3\n")
# File now contains: "Line 2\nLine 3\n"
```

**Other modes:**
- `"r"` - Read (default, file must exist)
- `"w"` - Write (overwrites)
- `"a"` - Append (adds to end)
- `"r+"` - Read and write
</details>

---

### Question 6: CSV Data Types
**Q:** Why do we use `float()` and `int()` when reading CSV data?

```python
with open("stocks.csv", "r") as file:
    for line in file:
        data = line.strip().split(",")
        price = data[1]
        shares = data[2]
```

What type are `price` and `shares`?

<details>
<summary>Click to see answer</summary>

**A:** Both `price` and `shares` are **strings**, not numbers!

When you read from a file, **everything is text**.

**The Problem:**
```python
data = "TSLA,425.00,100".split(",")
# data = ["TSLA", "425.00", "100"]  # All strings!

price = data[1]     # "425.00" (string)
shares = data[2]    # "100" (string)

total = price * shares  # "425.00100" (string concatenation!) ❌
```

**The Solution:**
```python
price = float(data[1])   # 425.00 (number)
shares = int(data[2])    # 100 (number)

total = price * shares   # 42500.0 (math!) ✅
```

**Type conversion needed:**
- `int("100")` → 100
- `float("425.00")` → 425.0
- `str(100)` → "100"
</details>

---

## Part 3: Error Handling

### Question 7: Exception Catching
**Q:** What's the purpose of `except Exception as e`? Why use `as e`?

```python
try:
    risky_operation()
except Exception as e:
    print(f"Error occurred: {e}")
```

<details>
<summary>Click to see answer</summary>

**A:** 

**`Exception`** - Catches any type of exception (catch-all)

**`as e`** - Stores the exception object in variable `e` so you can:
1. Print the error message
2. Log details
3. Access exception attributes

**Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # "Error: division by zero"
    print(f"Type: {type(e)}")  # "<class 'ZeroDivisionError'>"
```

**Without `as e`:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error occurred!")  # Can't show details
```

**Use cases for Exception info:**
- Logging to file
- Debugging
- User-friendly error messages
- Error reporting
</details>

---

### Question 8: Finally Blocks
**Q:** When would you use `finally` block? Give an example.

<details>
<summary>Click to see answer</summary>

**A:** Use `finally` for code that must run **no matter what** - success or failure.

**Common use cases:**

**1. Logging (even with `with` statement):**
```python
try:
    with open("data.csv", "r") as f:
        data = process(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("✅ Processing attempt complete")
    # Runs whether file found or not
```

**2. Cleanup without `with`:**
```python
file = None
try:
    file = open("data.csv", "r")
    process(file.read())
except FileNotFoundError:
    print("Error!")
finally:
    if file:
        file.close()  # Always close
    print("Cleanup done")
```

**3. Database connections:**
```python
conn = None
try:
    conn = database.connect()
    conn.execute("SELECT * FROM stocks")
except DatabaseError:
    print("Query failed!")
finally:
    if conn:
        conn.close()  # Always close connection
```

**4. Releasing resources:**
```python
lock = acquire_lock()
try:
    critical_operation()
finally:
    release_lock(lock)  # Always release
```

**Key point:** `finally` runs even if:
- No exception occurs
- Exception is caught
- Exception is not caught
- `return` statement in try block
</details>

---

## Part 4: String Manipulation

### Question 9: String Methods
**Q:** What's the output of this code?

```python
text = "  Tesla,TSLA,Technology  "
parts = text.strip().split(",")
result = parts[1].lower()
print(result)
```

<details>
<summary>Click to see answer</summary>

**A:** `tsla`

**Step-by-step:**
1. `text.strip()` → `"Tesla,TSLA,Technology"` (removes leading/trailing spaces)
2. `.split(",")` → `["Tesla", "TSLA", "Technology"]`
3. `parts[1]` → `"TSLA"` (second element)
4. `.lower()` → `"tsla"`

**Common string methods:**
```python
text = "  HELLO  "

text.strip()      # "HELLO"
text.lstrip()     # "HELLO  "
text.rstrip()     # "  HELLO"
text.lower()      # "  hello  "
text.upper()      # "  HELLO  "

# Chaining
text.strip().lower()  # "hello"
```
</details>

---

## Part 5: Coding Challenges

### Challenge 1: Safe Division Function
**Task:** Write a function `safe_divide(a, b)` that:
- Returns `a / b` if successful
- Returns 0 if division by zero
- Returns None if either input isn't a number
- Prints an appropriate error message for each case

<details>
<summary>Click to see solution</summary>

```python
def safe_divide(a, b):
    """
    Safely divide two numbers with error handling.
    
    Returns:
        float: Result of division
        0: If division by zero
        None: If inputs are not numbers
    """
    try:
        # Try to convert to numbers
        num_a = float(a)
        num_b = float(b)
        
        # Try division
        result = num_a / num_b
        return result
        
    except ValueError:
        print(f"Error: Cannot convert {a} or {b} to number")
        return None
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return 0

# Test cases
print(safe_divide(10, 2))        # 5.0
print(safe_divide(10, 0))        # 0 (prints error)
print(safe_divide("abc", 5))     # None (prints error)
print(safe_divide(15, "3"))      # 5.0 (works - string converts)
```
</details>

---

### Challenge 2: CSV Row Parser
**Task:** Write a function `parse_stock_row(line)` that:
- Takes a CSV line: `"TSLA,425.00,100"`
- Returns a dictionary: `{"symbol": "TSLA", "price": 425.0, "shares": 100}`
- Handles errors if data is invalid
- Returns None for invalid rows

<details>
<summary>Click to see solution</summary>

```python
def parse_stock_row(line):
    """
    Parse a CSV row into a stock dictionary.
    
    Args:
        line: String like "TSLA,425.00,100"
        
    Returns:
        dict: Stock data or None if invalid
    """
    try:
        # Clean and split
        parts = line.strip().split(",")
        
        # Validate length
        if len(parts) != 3:
            print(f"Invalid row: expected 3 columns, got {len(parts)}")
            return None
        
        # Parse data
        symbol = parts[0].strip().upper()
        price = float(parts[1].strip())
        shares = int(parts[2].strip())
        
        # Validate values
        if price < 0 or shares < 0:
            print(f"Invalid values: price and shares must be positive")
            return None
        
        return {
            "symbol": symbol,
            "price": price,
            "shares": shares
        }
        
    except ValueError as e:
        print(f"Error parsing row: {e}")
        return None

# Test cases
print(parse_stock_row("TSLA,425.00,100"))     # Valid
print(parse_stock_row("AAPL,150,50"))         # Valid
print(parse_stock_row("NVDA,abc,75"))         # Invalid (price)
print(parse_stock_row("MSFT,380.00"))         # Invalid (missing column)
```
</details>

---

### Challenge 3: Portfolio File Reader
**Task:** Write a complete function that:
- Reads a portfolio CSV file
- Skips the header row
- Parses each stock row
- Skips invalid rows with a warning
- Returns a list of valid stock dictionaries
- Handles file not found error

<details>
<summary>Click to see solution</summary>

```python
def read_portfolio_file(filename):
    """
    Read and parse a portfolio CSV file.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        list: List of stock dictionaries
    """
    stocks = []
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
            # Skip header (first line)
            for i, line in enumerate(lines[1:], start=2):
                try:
                    # Parse line
                    parts = line.strip().split(",")
                    
                    stock = {
                        "symbol": parts[0].strip().upper(),
                        "price": float(parts[1].strip()),
                        "shares": int(parts[2].strip())
                    }
                    
                    stocks.append(stock)
                    
                except (ValueError, IndexError) as e:
                    print(f"⚠️  Skipping line {i}: {e}")
                    continue
        
        print(f"✅ Successfully loaded {len(stocks)} stocks")
        return stocks
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        return []
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return []

# Test
portfolio = read_portfolio_file("portfolio.csv")
for stock in portfolio:
    print(stock)
```
</details>

---

### Challenge 4: Data Validator
**Task:** Write a function `validate_stock_data(stock_dict)` that:
- Checks if all required keys exist
- Validates data types
- Validates value ranges (price > 0, shares > 0)
- Returns `(True, None)` if valid
- Returns `(False, error_message)` if invalid

<details>
<summary>Click to see solution</summary>

```python
def validate_stock_data(stock_dict):
    """
    Validate stock dictionary data.
    
    Args:
        stock_dict: Dictionary with stock data
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check required keys
    required_keys = ["symbol", "price", "shares"]
    for key in required_keys:
        if key not in stock_dict:
            return False, f"Missing required key: {key}"
    
    # Check data types
    if not isinstance(stock_dict["symbol"], str):
        return False, "Symbol must be a string"
    
    try:
        price = float(stock_dict["price"])
        shares = int(stock_dict["shares"])
    except (ValueError, TypeError):
        return False, "Price/shares must be numbers"
    
    # Check value ranges
    if price <= 0:
        return False, f"Price must be positive, got {price}"
    
    if shares <= 0:
        return False, f"Shares must be positive, got {shares}"
    
    # Check symbol format
    if not stock_dict["symbol"].strip():
        return False, "Symbol cannot be empty"
    
    return True, None

# Test cases
stocks = [
    {"symbol": "TSLA", "price": 425.0, "shares": 100},  # Valid
    {"symbol": "", "price": 150.0, "shares": 50},       # Invalid symbol
    {"symbol": "NVDA", "price": -500, "shares": 75},    # Invalid price
    {"symbol": "AAPL", "shares": 50},                   # Missing price
]

for stock in stocks:
    is_valid, error = validate_stock_data(stock)
    if is_valid:
        print(f"✅ {stock['symbol']}: Valid")
    else:
        print(f"❌ {stock.get('symbol', 'Unknown')}: {error}")
```
</details>

---

## Part 6: Advanced Challenges

### Challenge 5: Generator Expression
**Q:** What's the output and why is this efficient?

```python
stocks = [
    {"symbol": "TSLA", "value": 43580},
    {"symbol": "AAPL", "value": 8275},
    {"symbol": "NVDA", "value": 39022}
]

total = sum(s["value"] for s in stocks)
print(total)
```

<details>
<summary>Click to see answer</summary>

**Output:** `90877`

**Why it's efficient:**

**Generator expression:**
```python
sum(s["value"] for s in stocks)
```

**Equivalent list comprehension:**
```python
sum([s["value"] for s in stocks])
```

**Difference:**
- **Generator:** Creates values one at a time (memory efficient)
- **List comprehension:** Creates entire list first (uses more memory)

**For large datasets:**
```python
# Generator - low memory
total = sum(s["value"] for s in million_stocks)

# List comp - high memory (creates list of 1M items)
total = sum([s["value"] for s in million_stocks])
```

**When to use generators:**
- Large datasets
- Single-pass iteration
- Memory constraints

**When to use lists:**
- Need to iterate multiple times
- Need indexing
- Small datasets
</details>

---

### Challenge 6: Nested Error Handling
**Task:** Explain why this pattern is useful:

```python
try:
    with open("data.csv", "r") as file:
        for line in file:
            try:
                process_line(line)
            except ValueError:
                print(f"Skipping bad line")
                continue
except FileNotFoundError:
    print("File not found")
```

<details>
<summary>Click to see answer</summary>

**This pattern separates two types of errors:**

**Outer try-except:** File-level errors
- FileNotFoundError
- PermissionError
- IOError
- If file can't be opened, stop entirely

**Inner try-except:** Row-level errors
- ValueError (bad data in specific row)
- IndexError (missing columns)
- Skip bad row, continue with next

**Why it's useful:**

**1. Robust data processing:**
```python
# Without nested - one bad row stops everything
for line in file:
    process_line(line)  # ValueError stops entire process

# With nested - skip bad rows
for line in file:
    try:
        process_line(line)
    except ValueError:
        continue  # Just skip this row
```

**2. Different error strategies:**
```python
try:
    file = open("data.csv", "r")
    for line in file:
        try:
            process_line(line)  # Try to process
        except ValueError:
            continue  # Skip bad row - keep going
except FileNotFoundError:
    # Can't continue without file - abort
    return None
```

**Real-world example:**
```python
def load_portfolio(filename):
    stocks = []
    try:
        with open(filename, "r") as f:
            for i, line in enumerate(f, 1):
                try:
                    stock = parse_line(line)
                    stocks.append(stock)
                except ValueError:
                    print(f"Row {i}: Invalid data, skipped")
                    # Continue to next row
        return stocks
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []  # Can't continue
```

**Benefits:**
- Graceful degradation
- Partial success possible
- Better user experience
- Production-ready robustness
</details>

---

## Reflection Questions

After completing Day 3, reflect on:

1. **Why use functions instead of copying code?**
   - Reusability, maintainability, testing

2. **When should you use error handling?**
   - File operations, user input, external data, network calls

3. **What's the difference between catching specific exceptions vs `Exception`?**
   - Specific = handle known problems, generic = catch unexpected

4. **Why is the `with` statement important for files?**
   - Automatic cleanup, prevents resource leaks

---

## Scoring Guide

- **15-18 correct:** Excellent! Mastered Day 3 concepts
- **11-14 correct:** Good! Minor review recommended
- **7-10 correct:** Review error handling and file I/O
- **0-6 correct:** Practice more with files and exceptions

---

## Optional Challenges Status

Track your progress on optional challenges:

- ⬜ Challenge 1: List Comprehensions (practice more)
- ⬜ Challenge 2: Exception Re-raising
- ⬜ Challenge 3: Context Managers

---

**Last Updated:** Day 3 - Functions, File I/O & Error Handling
