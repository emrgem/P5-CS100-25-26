"""
Unit 6 - Lesson 1A: Reading CSV Files (Business Edition)
=========================================================
Learn to load business data from CSV files into Python!
"""
# =============================================================================
# 🎯 ACTIVITY 1: Load and Display Customers
# =============================================================================
# Load customers.csv and print a formatted customer list
#
# Expected output:
# === CUSTOMER LIST ===
# Acme Corp | Contact: Alice Johnson | Revenue: $15,000
# TechStart Inc | Contact: Bob Smith | Revenue: $8,500
# Green Gardens | Contact: Carol Davis | Revenue: $12,000
# ...

# TODO: Import csv 
import csv
# TODO: Open the file with "with open(...)"
with open("customers.csv", 'r') as file:
# TODO: Create a DictReader
    reader = csv.DictReader(file)
    # print(reader)
    # for customer in reader:
    #     print(customer)
    customer_list = list(reader)
    # print(customer_list)

# TODO: Print the header "=== CUSTOMER LIST ==="
    print("===CUSTOMER LIST===")
    for row in customer_list:
        # print(row)
        # print(row['company'])
        # print(f"{row['company']}- {row['contact']} - Revenue: {row['revenue']}")
        revenue = int(row['revenue'])  #converted to a number
        
# TODO: Loop through each row and print formatted output
#       Remember: use int() to convert revenue to a number
#       Hint: f"{revenue:,}" adds commas to numbers!

print(f"Loaded {len(customer_list)} customers")
print(customer_list[0]['company']) # first customer



