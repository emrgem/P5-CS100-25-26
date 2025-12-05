# Task 4: Validate a Rating (25 points)
def validate_rating(rating):
    """
    Check if a rating is valid (between 0 and 10).
    Raises ValueError with specific message for invalid ratings.
    Parameters:
        rating (int or float): The rating to validate
    Returns:
        bool: True if rating is valid (0-10 inclusive)
    Raises:
        ValueError: "Rating cannot be negative" if rating < 0
        ValueError: "Rating cannot exceed 10" if rating > 10
    Examples:
        validate_rating(7.5)  → True
        validate_rating(0)    → True
        validate_rating(10)   → True
        validate_rating(-3)   → raises ValueError
        validate_rating(15)   → raises ValueError
    """
    # TODO: Write your code here
    # Check if rating is less than 0 → raise ValueError with message
    # Check if rating is greater than 10 → raise ValueError with message
    # If valid, return True

    pass  # Remove this line when you add your code


# Tests
if __name__ == "__main__":
    try:
        result1 = validate_rating(7.5)
        print(f"validate_rating(7.5) = {result1}", end="")
        print(" ✓" if result1 == True else f" ✗ (expected True)")

        result2 = validate_rating(0)
        print(f"validate_rating(0) = {result2}", end="")
        print(" ✓" if result2 == True else f" ✗ (expected True)")

        result3 = validate_rating(10)
        print(f"validate_rating(10) = {result3}", end="")
        print(" ✓" if result3 == True else f" ✗ (expected True)")
    except Exception as e:
        print(f"Error in Task 4 (valid cases): {e}")

    # Test ValueError for negative
    try:
        validate_rating(-3)
        print("validate_rating(-3) = No error raised ✗ (expected ValueError)")
    except ValueError as e:
        expected_msg = "Rating cannot be negative"
        if expected_msg in str(e):
            print(f"validate_rating(-3) raised ValueError ✓")
        else:
            print(f"validate_rating(-3) raised ValueError but wrong message ✗")
            print(f"  Got: {e}")
            print(f"  Expected: {expected_msg}")
    except Exception as e:
        print(f"validate_rating(-3) raised wrong error type: {type(e).__name__}")

    # Test ValueError for >10
    try:
        validate_rating(15)
        print("validate_rating(15) = No error raised ✗ (expected ValueError)")
    except ValueError as e:
        expected_msg = "Rating cannot exceed 10"
        if expected_msg in str(e):
            print(f"validate_rating(15) raised ValueError ✓")
        else:
            print(f"validate_rating(15) raised ValueError but wrong message ✗")
            print(f"  Got: {e}")
            print(f"  Expected: {expected_msg}")
    except Exception as e:
        print(f"validate_rating(15) raised wrong error type: {type(e).__name__}")
