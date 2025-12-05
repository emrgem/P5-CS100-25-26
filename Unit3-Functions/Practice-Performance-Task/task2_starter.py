# Task 2: Format a Review (25 points)
def format_review(title, rating, reviewer="Anonymous"):
    """
    Create a formatted review string.
    Parameters:
        title (str): The movie/show title
        rating (int or float): The rating out of 10
        reviewer (str): Name of reviewer (default: "Anonymous")
    Returns:
        str: Formatted as "TITLE - Rating: X/10 (Reviewed by: NAME)"
    Examples:
        format_review("Inception", 9)
            → "Inception - Rating: 9/10 (Reviewed by: Anonymous)"

        format_review("The Matrix", 10, "Alex")
            → "The Matrix - Rating: 10/10 (Reviewed by: Alex)"
    """
    # TODO: Write your code here
    # Create a formatted string using f-string or .format()
    # Remember: reviewer has a default value of "Anonymous"
    # Return the formatted string

    pass  # Remove this line when you add your code


# Tests
if __name__ == "__main__":
    try:
        result1 = format_review("Inception", 9)
        expected1 = "Inception - Rating: 9/10 (Reviewed by: Anonymous)"
        print(f"format_review('Inception', 9)")
        print(f"  Result: {result1}")
        print(f"  {'✓' if result1 == expected1 else '✗ Expected: ' + expected1}")

        result2 = format_review("The Matrix", 10, "Alex")
        expected2 = "The Matrix - Rating: 10/10 (Reviewed by: Alex)"
        print(f"format_review('The Matrix', 10, 'Alex')")
        print(f"  Result: {result2}")
        print(f"  {'✓' if result2 == expected2 else '✗ Expected: ' + expected2}")

        result3 = format_review("Frozen", 8, reviewer="Jordan")
        expected3 = "Frozen - Rating: 8/10 (Reviewed by: Jordan)"
        print(f"format_review('Frozen', 8, reviewer='Jordan')")
        print(f"  Result: {result3}")
        print(f"  {'✓' if result3 == expected3 else '✗ Expected: ' + expected3}")
    except Exception as e:
        print(f"Error in Task 2: {e}")
