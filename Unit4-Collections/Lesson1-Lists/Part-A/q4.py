# ==================== PROBLEM 4: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 4: Safe Access with Error Handling")
print("=" * 60)

def safe_get_item(my_list, index):
    """
    Safely get an item from a list by index.
    Use try/except to handle IndexError!
    
    Args:
        my_list: List of items
        index: Index to access (int)
    
    Returns:
        The item if found, or None if index doesn't exist
    
    Example:
        fruits = ["apple", "banana", "cherry"]
        result = safe_get_item(fruits, 1)  # Returns "banana"
        result = safe_get_item(fruits, 10) # Returns None
    
    TODO:
    1. Use try/except to handle IndexError
    2. Try to return my_list[index]
    3. If IndexError happens, return None
    """
    # TODO: Implement safe access
    try:
        return my_list[index]
    except IndexError:
        return None


if __name__ == "__main__":
    fruits = ["apple", "banana", "cherry"]
    print(f"List: {fruits}")
    print(f"safe_get_item(fruits, 1): {safe_get_item(fruits, 1)}")
    print(f"safe_get_item(fruits, 10): {safe_get_item(fruits, 10)}")
    print(f"safe_get_item(fruits, -1): {safe_get_item(fruits, -1)}")