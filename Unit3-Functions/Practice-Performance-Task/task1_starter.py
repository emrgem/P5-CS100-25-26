# Task 1: Convert Score to Stars (25 points)
def convert_to_stars(score):
    """
    Convert a score (0-100) to a star rating (1-5).
    Conversion chart:
        0-20   → 1 star
        21-40  → 2 stars
        41-60  → 3 stars
        61-80  → 4 stars
        81-100 → 5 stars
    Parameters:
        score (int): A score from 0 to 100
    Returns:
        int: Star rating from 1 to 5
    Examples:
        convert_to_stars(95) → 5
        convert_to_stars(73) → 4
        convert_to_stars(45) → 3
    """
    # TODO: Write your code here
    # Use if/elif/else to check the score ranges
    # Return the appropriate star rating (1, 2, 3, 4, or 5)
    if score <= 20:
        return 1
    elif score <= 40:
        return 2
    elif score <= 60:
        return 3
    elif score <= 80:
        return 4
    else:
        return 5


# Tests
if __name__ == "__main__":
    try:
        result1 = convert_to_stars(95)
        print(f"convert_to_stars(95) = {result1}", end="")
        print(" ✓" if result1 == 5 else f" ✗ (expected 5)")
        
        result2 = convert_to_stars(73)
        print(f"convert_to_stars(73) = {result2}", end="")
        print(" ✓" if result2 == 4 else f" ✗ (expected 4)")
        
        result3 = convert_to_stars(45)
        print(f"convert_to_stars(45) = {result3}", end="")
        print(" ✓" if result3 == 3 else f" ✗ (expected 3)")
        
        result4 = convert_to_stars(30)
        print(f"convert_to_stars(30) = {result4}", end="")
        print(" ✓" if result4 == 2 else f" ✗ (expected 2)")
        
        result5 = convert_to_stars(15)
        print(f"convert_to_stars(15) = {result5}", end="")
        print(" ✓" if result5 == 1 else f" ✗ (expected 1)")
    except Exception as e:
        print(f"Error in Task 1: {e}")
