# Python Type Conversion Practice - Starter File

# ====== CODE ALONG SECTION 1: Age Calculator Fix ======
# The wrong way (this will cause an error):
user_age = "16"
next_year = int(user_age) + 1
print("5" + "3")
print(int("5") + int("3"))
print(next_year)



# ====== CODE ALONG SECTION 2: Boolean Testing ======
print(f"bool(0) - {bool(0)}")       # False 
print(f'bool("") - {bool("")}')     # False
print(f'bool(" ") - {bool(" ")}')     # True
print(f'bool(1) - {bool(1)}')     # True
print(f'bool(-5) - {bool(-5)}')     # True


# ====== CODE ALONE CHALLENGE 1: Fix These Errors! ======
# Fix these broken code snippets:

# Problem 1 - height calculation
height = "5.8"
height_in_inches = float(height) * 12
print(height_in_inches)

# Problem 2 - string concatenation with number
test_score = 95
print(f"Before test_score: {type(test_score)}")
message = "You scored " + str(test_score) + " points!"
print(f"After test_score: {type(test_score)}")

test_score = str(test_score) # Reassigning test_score
message = f"You scored {test_score} points!"
print(message)
print(f"After str function assigned test_score: {type(test_score)}")

# Problem 3 - cost calculation
# items = "5"
# total_cost = items * 2.99


# ====== CODE ALONE CHALLENGE 2: Grade Calculator ======
# Build a grade calculator:

# You have these grade strings:
math_grade = "85"
science_grade = "92.5" 
english_grade = "78"

# Your tasks:
# 1. Convert all to numbers (appropriate types)
# 2. Calculate the average
# 3. Determine if average >= 80 (honor roll)
# 4. Create a report message using f-strings


# ====== BONUS - CODE ALONE CHALLENGE: User Profile Builder ======
# Create a complete program:

# Simulated user input (as strings):
user_name = "Jordan"
user_age_str = "17"
fav_number_str = "21"
has_license_str = "yes"

# Your tasks:
# 1. Convert each to appropriate types
# 2. Calculate age in 10 years
# 3. Check if favorite number is even
# 4. Convert "yes"/"no" to True/False for license
# 5. Create a complete profile report