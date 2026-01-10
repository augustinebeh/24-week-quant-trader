import os
from safe_csv_reader import opening_reading_analysis

def run_test_suite():
    # Define file names
    invalid_file = 'invalid_data_test.csv'
    missing_file = 'missing_cols_test.csv'
    original_file = 'portfolio.csv'

    # 1. Test File Not Found
    print("\n🔍 Running Test 1: Missing File Handling...")
    os.system("sleep 0.5")
    opening_reading_analysis('ghost_file.csv')
    print("✅ FileNotFoundError test completed")

    # 2. Test Invalid Data
    print("\n🔍 Running Test 2: Invalid Data...")
    with open(invalid_file, 'w') as f:
        f.write("symbol,buying_price,current_price,shares\n")
        f.write("AAPL,150.00,175.00,BAD_DATA\n")

    os.system("sleep 0.5")
    opening_reading_analysis(invalid_file)
    print("✅ ValueError skipping test completed")

    # 3. Test Missing Columns
    print("\n🔍 Running Test 3: Missing Columns...")
    with open(missing_file, 'w') as f:
        f.write("symbol,buying_price,current_price,shares\n")
        f.write("TSLA,200.00\n")

    os.system("sleep 0.5")
    opening_reading_analysis(missing_file)
    print("✅ IndexError skipping test completed")

    # 4. Test Valid File (Original)
    print(f"\n🔍 Running Test 4: Original Portfolio ({original_file})...")
    if os.path.exists(original_file):
        os.system("sleep 0.5")
        opening_reading_analysis(original_file)
        print("✅ Original file processing completed")
    else:
        print(f"⚠️  Skipping Test 4: {original_file} does not exist.")

    # Cleanup Section - Only delete the generated test files
    print("\n🧹 Cleaning up temporary test files...")
    for temp_file in [invalid_file, missing_file]:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"🗑️  Deleted {temp_file}")

    os.system("sleep 0.3")

if __name__ == "__main__":
    print("========================================")
    print("🚀 STARTING CSV ERROR HANDLING TESTS")
    print("========================================")

    run_test_suite()

    print("\n🎯 Suite executed. Temporary files purged.")
    print("========================================\n")
