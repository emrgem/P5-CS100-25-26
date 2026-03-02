"""
Unit 6 - Lesson 3: Working with JSON 
========================================================
📌 Keep this open as a reference while following the slides!
"""
import json

# =============================================================================
# 📚 SYNTAX REFERENCE
# =============================================================================

# --- Reading JSON from File ---
#
# with open("filename.json", "r") as file:
#     data = json.load(file)  # File → Python
#

# --- Writing JSON to File ---
#
# with open("filename.json", "w") as file:
#     json.dump(data, file, indent=4)  # Python → File
#

# --- Parsing JSON String ---
#
# data = json.loads(json_string)  # String → Python
#

# --- Creating JSON String ---
#
# json_string = json.dumps(data, indent=4)  # Python → String
#


# =============================================================================
# 🎯 ACTIVITY 1: Read and Analyze Customer Data
# =============================================================================
# Load customer_data.json and find the highest-spending customer
#
# Expected output:
# Top customer: TechStart Inc
# Total spent: $72,000

# YOUR CODE HERE:
#Load the json file
with open("customer_data.json", "r") as file:
    customers = json.load(file)

print(type(customers)) #<class 'list'>
print(type(customers[0])) #<class 'dict'>

#Find the highest spender
highest_spender = customers[0]
for customer in customers:
    if customer["total_spent"] > highest_spender["total_spent"]:
        highest_spender = customer

#Display the results
print(f"Top Customer: {highest_spender["name"]}")
print(f"Total Spent: ${highest_spender['total_spent']:,}")



# =============================================================================
# 🎯 ACTIVITY 2: Create Product Catalog
# =============================================================================
# Create a product catalog and save it as JSON
#
# Products to include:
# - Wireless Mouse ($29.99, Electronics)
# - USB Cable ($12.99, Accessories)
# - Laptop Stand ($45.00, Furniture)

products = [
    {"id": "P001", "name": "Wireless Mouse", "price": 29.99, "category": "Electronics"},
    {"id": "P002", "name": "USB Cable", "price": 12.99, "category": "Accessories"},
    {"id": "P003", "name": "Laptop Stand", "price": 45.00, "category": "Furniture"}
]

# YOUR CODE HERE:
# 1. Write products to "catalog.json" with indent=4
with open("catalog.json", "w") as file:
    json.dump(products, file, indent=4)
print("✔️ Catalog created")

# 2. Read it back and print all product names
with open("catalog.json", "r") as file:
    loaded_products = json.load(file)
    
print("\nProducts in Catalog:")
for product in loaded_products:
    print(f" - {product['name']}")


# =============================================================================
# 🔤 PRACTICE: JSON Strings
# =============================================================================
# Practice with json.loads() and json.dumps()

# Parse this JSON string from an "API response"
api_response = '{"status": "success", "revenue": 45000, "customers": 127}'

# YOUR CODE HERE:
# 1. Parse the string into a Python dictionary
data = json.loads(api_response)

# 2. Print the revenue
print(f"Revenue: ${data['revenue']:,}")

# 3. Convert back to a formatted JSON string
formatted_json = json.dumps(data, indent=4)
print(formatted_json)


# =============================================================================
# 🏢 PRACTICE: Nested Data
# =============================================================================
# Work with nested JSON structures

company = {
    "name": "TechCorp",
    "founded": 2018,
    "location": {
        "city": "San Francisco",
        "state": "CA",
        "zip": "94105"
    },
    "departments": ["Sales", "IT", "Marketing", "Finance"]
}

# YOUR CODE HERE:
# 1. Print the city
print(f"Location: {company['location']['city']}")

# 2. Print the first department
print(f"First Department: {company['departments'][0]}")

# 3. Save this to "company_info.json"
with open("company_info.json", "w") as file:
    json.dump(company, file, indent=4)

print("✅ company_info.json created!")

# =============================================================================
# 📝 NOTES & REMINDERS
# =============================================================================
# ✓ load/dump for FILES, loads/dumps for STRINGS
# ✓ Always use indent=4 for readable output
# ✓ JSON uses lowercase: true, false, null (not True, False, None)
# ✓ JSON keys must be strings (double quotes, not single)
# ✓ Use try-except for error handling when loading external data
