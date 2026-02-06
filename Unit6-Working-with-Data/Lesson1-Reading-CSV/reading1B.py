"""
Unit 6 - Lesson 1B: Processing CSV Data (Business Edition)
==========================================================
Learn to analyze business data - count, total, find, and search!
"""
import csv

# =============================================================================
# 📚 SYNTAX REFERENCE
# =============================================================================

# --- Loading Data ---
# with open("customers.csv", "r") as file:
#     customers = list(csv.DictReader(file))
#
# --- Counting Items ---
# total = len(customers)
#
# --- Summing Values (Accumulator Pattern) ---
# total = 0
# for customer in customers:
#     total = total + int(customer['revenue'])
#
# --- Finding Maximum ---
# best = None
# highest = 0
# for customer in customers:
#     value = int(customer['revenue'])
#     if value > highest:
#         highest = value
#         best = customer


# =============================================================================
# ⚠️ KEY RULES TO REMEMBER
# =============================================================================

# 1. ALL CSV VALUES ARE STRINGS!
#    Convert with int() when doing math: int(row['revenue'])

# 2. ACCUMULATOR PATTERN: Start at 0, add in a loop
#    total = 0
#    for item in list:
#        total = total + value

# 3. FINDING MAX: Track both the value AND the item
#    if value > highest:
#        highest = value
#        best_item = item


# =============================================================================
# 🎯 ACTIVITY 1: Customer Summary Report
# =============================================================================
# Create a business report with these statistics:
#
# Expected output:
# === CUSTOMER SUMMARY REPORT ===
# Total customers: 20
# Total revenue: $235,500
# Biggest customer: Pacific Trading ($22,000)
# Average revenue: $11,775.00

# Step 1: Load the data
with open("customers.csv", "r") as file:
    customers = list(csv.DictReader(file))

# print(customers) # list of dictionaries


# Step 2: Count total customers
total_customers = len(customers)
print(f"Total Customers: {total_customers}")

# Step 3: Calculate total revenue
# total_revenue = 0
# for customer in customers:
#     # print(customer["revenue"])
#     total_revenue += int(customer["revenue"])
# print(f"Total Revenue: ${total_revenue}")

#Single Liner
# total_revenue = sum([int(customer.get("revenue", 0)) for customer in customers])
total_revenue = sum(int(customer.get("revenue", 0)) for customer in customers)
print(f"Total Revenue: ${total_revenue}")


# Step 4: Find the biggest customer
best_customer = None
highest_revenue = 0

for customer in customers:
    revenue = int(customer["revenue"])
    if revenue > highest_revenue:
        highest_revenue = revenue
        best_customer = customer

# Step 5: Calculate average revenue
average_revenue = total_revenue / total_customers

# Step 6: Print the report

print(f"Biggest Customer: { best_customer["company"]}")
print(f"Revenue: { highest_revenue:,}")
print(f"Average Revenue: {average_revenue:,}")



# =============================================================================
# 🎯 ACTIVITY 2: Customer Lookup Tool
# =============================================================================
# Build an interactive customer search system
#
# Requirements:
# 1. Load customers.csv at the start
# 2. Ask user for a company name to search
# 3. If found → display all their info
# 4. If not found → show error message
# 5. Loop until user types "quit"
#
# Expected output:
# === CUSTOMER LOOKUP ===
# Enter company name (or 'quit'): Acme Corp
#
# Found customer!
#   Company: Acme Corp
#   Contact: Alice Johnson
#   Email: alice@acme.com
#   Revenue: $15,000
#
# Enter company name (or 'quit'): Nobody Inc
#
# Customer 'Nobody Inc' not found!
#
# Enter company name (or 'quit'): quit
# Goodbye!


def find_customer(customers, company_name):
    """Find a customer by company name."""
    for customer in customers:
        if customer['company'].lower() == company_name.lower():
            return customer
    return None


def display_customer(customer):
    """
    Display a customer's information nicely formatted.
    """
    print("\nFound customer!")
    print(f"  Company: {customer['company']}")
    print(f"  Contact: {customer['contact']}")
    print(f"  Email: {customer['email']}")
    print(f"  Revenue: ${int(customer['revenue']):,}")


# Main program
with open("customers.csv", "r") as file:
    customers = list(csv.DictReader(file))

print("=== CUSTOMER LOOKUP ===")

while True:
    search = input("\nEnter company name (or 'quit'): ")
    
    # TODO: Check if user typed 'quit' - if so, print "Goodbye!" and break
    
    # TODO: Call find_customer() to search
    
    # TODO: If found, call display_customer()
    # TODO: If not found, print "Customer 'X' not found!"
    
    pass  # Remove this when you add your code



