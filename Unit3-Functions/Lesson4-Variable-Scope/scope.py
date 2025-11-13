# =====================
# Practice 1: Local Variables
# Instructions: Create a function that uses local variables for calculations
# =======================
def calculate_pizza_slices():
    """Calculate slices per person using local variables."""
    total_slices = 24        # Local variable
    people = 6               # Local variable
    slices_per_person = total_slices / people
    return slices_per_person

result = calculate_pizza_slices()
print(f"Each person gets {result} slices")
# print(people) 
# NameError: name 'people' is not defined
# Local variables does not exist here

# =========================
# Practice 2: Global Constants
# Instructions: Create global constants and a function that uses them
# ==========================
#Global constants (uppercase naming convention)
TAX_RATE = 0.08
SHIPPING_COST = 5.00

def calculate_tax(price):
    return price * TAX_RATE # Can read global constant

def calculate_total(price):
    tax = calculate_tax(price)
    total = price + tax + SHIPPING_COST # using both constants
    return total

item_price = 50.0
final_total = calculate_total(item_price)
print(f"Price: ${item_price:.2f}")
print(f"Total: ${final_total:.2f}")

# ==========================
# Practice 3: Parameters Instead of Globals
# Instructions: Rewrite the code to use parameters instead of global variables
# ==========================
# Parameters are better to update global variables
# X Bad Example - Global Variables
score = 0
def add_points():
    global score
    score += 10
    #Where did this run?
    #Who changed score?
    #Hard to debug
    
# Good Example - Parameters and return
def add_points(score):
    return score + 10
score = 0
score = add_points(score)
#clear what changed
#Easy to test
#Easy to debug



# ===========================
# Practice 4: Multiple Functions Sharing Data
# Instructions: Create two functions that work together using parameters/return
# ===========================
def calculate_grade_percentage(score, max_score):
    """Calculate percentage."""
    percentage = (score / max_score) * 100
    return percentage

def get_letter_grade(percentage):
    """Takes percentage as parameter."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    # ... etc
    
student_score = 85
percent = calculate_grade_percentage(student_score, 100)
letter = get_letter_grade(percent)  # Pass data!
print(f"Grade: {letter}")  # B


# ===========================
# Challenge 1: Shopping Cart System
# Instructions: Build a complete system using proper scope practices
# ===========================



# ==========================
# Challenge 2: Game Score Calculator
# Instructions: Calculate game score using constants and functions with proper scope
# ==========================