"""
Unit 6 - Lesson 2: Writing CSV Files (Business Edition)
========================================================
📌 Keep this open as a reference while following the slides!
"""
import csv

# =============================================================================
# 📚 SYNTAX REFERENCE
# =============================================================================

# --- Create New CSV File (Write Mode) ---
#
# with open("filename.csv", "w", newline="") as file:
#     fieldnames = ['col1', 'col2', 'col3']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()      # Write column names
#     writer.writerows(data)    # Write all rows
#

# --- Add to Existing CSV (Append Mode) ---
#
# with open("filename.csv", "a", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writerow(single_record)   # NO header!
#


# =============================================================================
# 🎯 ACTIVITY 1: Create a Sales Report
# =============================================================================
# Create a file called "sales_report.csv" with monthly sales data.

# Expected file contents:
# month,product,units_sold,revenue
# January,Laptops,42,50400
# January,Monitors,67,20100
# February,Laptops,38,45600

sales = [
    {'month': 'January', 'product': 'Laptops', 'units_sold': 42, 'revenue': 50400},
    {'month': 'January', 'product': 'Monitors', 'units_sold': 67, 'revenue': 20100},
    {'month': 'February', 'product': 'Laptops', 'units_sold': 38, 'revenue': 45600}
]

# YOUR CODE HERE:
with open("sales_report.csv", "w", newline="") as file:
    #1 - Define the column names - List of strings
    fieldnames = ['month', 'product', 'units_sold', 'revenue']
    #2 - Create the write with columns
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    #3 - Write the header row
    writer.writeheader()
    #4 - Write all data rows - List of dictionaries
    # writer.writerow(sales[0]) - write a dict as single row
    writer.writerows(sales) # adds lists of dictionaries
    
with open("sales_report.csv", "a", newline="") as file:
    fieldnames = ['month', 'product', 'units_sold', 'revenue']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    #Add one single row ( NO HEADER)
    new_sale = {'month': 'March', 'product': 'VR', 'units_sold': 20, 'revenue': 25000}
    writer.writerow(new_sale)
    
    
    



# =============================================================================
# 🎯 ACTIVITY 2: Add Transaction Function
# =============================================================================
# Create a function that adds a new sale to sales_report.csv
#
# Test with:
# add_sale("March", "Laptops", 45, 54000)
# add_sale("March", "Monitors", 72, 21600)

def add_sale(month, product, units_sold, revenue):
    """Add a new sale to the sales report."""
    # TODO: Create the new_sale dictionary
    new_sale = {
        'month': month,
        'product': product,
        'units_sold': units_sold,
        'revenue': revenue
    }
    # TODO: Open file in APPEND mode
    with open("sales_report.csv", 'a', newline='') as file:
    # TODO: Create DictWriter with fieldnames
        fieldnames = ['month', 'product', 'units_sold', 'revenue']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    # TODO: Write the single row (NO header!)
        writer.writerow(new_sale)
    # TODO: Print confirmation
    print(f"Sale added: {month} - {product} - {units_sold} - {revenue}")


# Test it:
add_sale("March", "Laptops", 45, 54000)
add_sale("March", "Monitors", 72, 21600)






