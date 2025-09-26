# Lesson 4: Ternary Operator & Chained Comparisons

# =============================================================================
# PART 1: TERNARY OPERATOR BASICS
# =============================================================================

# Traditional if-else way
age = 17
if age >= 18:
    status = "adult"
else:
    status = "minor"

print(f"Traditional way: {status}")
# Ternary operator way (one line)
# Pattern: variable = value1 if condition else value2

status = "adult" if age >= 18 else "minor"
print(f"Ternary way: {status}")
# =============================================================================
# PART 2: MORE TERNARY EXAMPLES
# =============================================================================

# Weather clothing choice
temperature = 75
# Use ternary to choose between "shorts" and "jacket if temp > 70"

clothing = "shorts" if temperature > 70 else "jacket"
# Grade pass/fail status  
score = 85
# Use ternary to set passed to "yes" or "no"
passed = "yes" if score >= 70 else "no"
print(f"Score:{score}, Passed:{passed}")

# =============================================================================
# PART 3: CHAINED COMPARISONS
# =============================================================================

# Traditional way with 'and'
age = 16
# Write if statement: age >= 13 and age <= 19
if age >= 13 and age <=19:
    print("Traditional: You are a teenager!")
# Chained comparison way (like math)
# Pattern: if min_value <= variable <= max_value
if 13 <= age <= 19:
    print("Chained: You are a teenager!")

# Grade range checking
grade = 87
# Use chaining to check if grade is B range (80-89)
if 80 <= grade < 90:
    print(f"Grade {grade} is a B!")

# =============================================================================
# PART 4: PRACTICE CONVERSIONS
# =============================================================================

# Convert these to ternary:

# 1. Tired drink choice
tired = True
# if tired:
#     drink = "coffee"
# else:
#     drink = "water"
drink = "coffee" if tired else "water"
print(f"You should drink {drink}")

# 2. Student pricing
is_student = False
# if is_student:
#     price = 10
# else:
#     price = 15
price = 10 if is_student else 15
print(f"Ticket Price: ${price}")

# Convert these to chained comparisons:

# 3. Height check
height = 68
# if height >= 66 and height <= 72:
#     print("Average height")
66 <= height <=72

# 4. Temperature comfort
temp = 72
# if temp >= 65 and temp <= 75:
#     print("Perfect weather!")
65 <= temp <= 75
64 < temp < 76

# =============================================================================
# PART 5: SIMPLE GRADE CALCULATOR
# =============================================================================

# Student information
student_name = "Alex"
student_score = 87

# Use chained comparisons for grade ranges:
# A: 90-100, B: 80-89, C: 70-79, F: below 70
if 90 <= student_score <= 100:
    letter_grade = "A"
elif 80 <= student_score < 90:
    letter_grade = "B"
elif 70 <= student_score < 80:
    letter_grade = "C"
else:
    letter_grade = "F"

# Use ternary for pass/fail status (passing is 70+)
pass_status = "PASS" if student_score >= 70 else "FAIL"

# Print results
print(f"\n--- Grade Report for {student_name} ---")
print(f"Score: {student_score}")
print(f"Letter Grade: {letter_grade}")
print(f"Status: {pass_status}")


# =============================================================================
# WHEN TO USE THESE SHORTCUTS
# =============================================================================

# Use ternary when:
# - Choosing between two simple values
# - Single condition
# - One line is clearer

# Use chained comparisons when:
# - Checking if value is in a range
# - Makes code read like math

# Use regular if-else when:
# - Multiple actions needed
# - Complex conditions
# - Need detailed comments