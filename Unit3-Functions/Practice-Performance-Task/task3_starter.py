# Task 3: Parse Rating Safely (25 points)
def parse_rating(rating_text):
    """
    Safely convert a string to a float rating.
    Uses try/except to handle invalid input gracefully.
    Parameters:
        rating_text (str): A string that should contain a number
    Returns:
        float: The rating as a float if valid
        float: -1.0 if the conversion fails
    Examples:
        parse_rating("8.5")    → 8.5
        parse_rating("10")     → 10.0
        parse_rating("seven")  → -1.0
        parse_rating("")       → -1.0
    """
    # TODO: Write your code here
    # Use try/except to attempt the conversion
    # In the try block: convert rating_text to float and return it
    # In the except block: return -1.0
    
    pass  # Remove this line when you add your code


# Tests
if __name__ == "__main__":
    try:
        result1 = parse_rating("8.5")
        print(f"parse_rating('8.5') = {result1}", end="")
        print(" ✓" if result1 == 8.5 else f" ✗ (expected 8.5)")
        
        result2 = parse_rating("10")
        print(f"parse_rating('10') = {result2}", end="")
        print(" ✓" if result2 == 10.0 else f" ✗ (expected 10.0)")
        
        result3 = parse_rating("seven")
        print(f"parse_rating('seven') = {result3}", end="")
        print(" ✓" if result3 == -1.0 else f" ✗ (expected -1.0)")
        
        result4 = parse_rating("")
        print(f"parse_rating('') = {result4}", end="")
        print(" ✓" if result4 == -1.0 else f" ✗ (expected -1.0)")
    except Exception as e:
        print(f"Error in Task 3: {e}")