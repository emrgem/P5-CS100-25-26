"""
Lesson 3: Return Values - Practice Exercises
"""

def greet(name):
    # print(f"Hello {name}")
    return f"Hello {name}"

result = greet("Gemici")
print(result)

def square(num):
    """Returns the square of a number."""
    return num ** 2
# Capture the returned value
result = square(5)
print(f"5 squared is {result}")  # 5 squared is 25
# Use it in a calculation
area = square(7) * 2
print(f"Area: {area}")  # Area: 98



#  Important: Return Ends the Function
def check_age(age):
    if age >= 18:
        return "Adult"    # Function stops here!
        print("This never runs")
    return "Minor"

status = check_age(20)
print(status)  # Adult


def calculate_percentage(score, max_score):
    """ Calculates percentage and RETURNS it. """
    # percentage = (score / max_score) * 100
    # return percentage
    return (score / max_score) * 100

# Test it!
result = calculate_percentage(47, 50)
print(f"Percentage: {result}%")  # 94.0%

def get_letter_grade(percentage):
    """ Returns letter grade based on percentage. """
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
result = get_letter_grade(80)
print(result)
# ============================================================================
# Practice 1: Rectangle Area
# ============================================================================
def calculate_area(length, width):
    """Calculate and return the area of a rectangle."""
    return length*width

rect1 = calculate_area(5,3)
print(f"rectangle 1's area: {rect1}")
rect2 = calculate_area(8,9)
print(f"rectangle 2's area: {rect2}")

# ============================================================================
# Practice 2: Temperature Converter
# ============================================================================
def celsius_to_fahrenheit(celsius): #
    "convert celcius to Fahrenheit (C*9/5)+32" #°alt+0176
    return (celsius*9/5)+32

print(f"0°C = {celsius_to_fahrenheit(0)}°F")  # 32.0
# ============================================================================
# Practice 3: Find Maximum
# ============================================================================
def find_max(num1, num2):
    """Return the larger of two numbers"""
    if num1 > num2:
        return num1
    return num2 #Alternative return max(num1, num2)

print(f"Max(3,5) = {find_max(3,5)}")

# ============================================================================
# Practice 4: Is Even?
# ============================================================================

def is_even(number):
    """Return True if number is even, False if odd."""
    # Method 1: Direct return (best!)
    return number % 2 == 0



# ============================================================================
# Practice 5: Calculate Tip
# ============================================================================




# ============================================================================
# Challenge 1: Calculate Average
# ============================================================================





# ============================================================================
# Challenge 2: Letter Grade
# ============================================================================

