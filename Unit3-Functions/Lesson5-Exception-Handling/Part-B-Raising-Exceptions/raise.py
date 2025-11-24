# Raising Exceptions - Making your code say "no"!
def set_volume(level):
    """Set volume level (0-100)"""
    if level < 0:
        raise ValueError("Volume cannot be negative!")
    if level > 100:
        raise ValueError("Volume cannot exceed 100!")
    volume = level
    print(f"Volume set to {volume}")
    
try:
    set_volume(50) #Works fine
    set_volume(-10) # Raises value error
except ValueError as error:
    print(f"Error: {error}") 
"""
Which exception should I raise?
ValueError - Invalid Value(wrong number, wrong format)
TypeError - Wrong data type provided
RuntimeError - General Error in our function
"""

def create_username(name):
    """
    Create a valid username.
    Rules:
        - Must be at least 3 characters
        - Cannot be more than 20 characters
        - Cannot be empty 
    """
    # Check if empty
    if name == "" or not name:
        raise ValueError("Username cannot be empty!")
    # Check minimum length
    if len(name) < 3:
        raise ValueError("Username must be at least 3 characters!")
    # Check maximum length
    if len(name) > 20:
        raise ValueError("Username cannot exceed 20 characters!")
    
    # All checks passed
    username  = name.lower()
    print(f"Username created: {username}")
    return username


# Test valid username
try:
    user = create_username("GamerPro")
    print(f"Success: {user}")
except ValueError as e:
    print(f"Error: {e}")
    
# Test too short
try:
    user = create_username("ab")
    print(f"Success: {user}")
except ValueError as e:
    print(f"Error: {e}")
    
# Test empty
try:
    user = create_username("")
    print(f"Success: {user}")
except ValueError as e:
    print(f"Error: {e}")
    
    
def divide(a,b):
    """Divide two numbers safely"""
    # Validate input
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    # Do the calculation
    result = a / b
    return result

try:
    print(divide(10,2)) # 5.0
    print(divide(10,0)) # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
    
