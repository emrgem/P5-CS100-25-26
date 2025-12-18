# ==================== PROBLEM 1: CODE WRITING ====================

print("=" * 60)
print("PROBLEM 1: Safe Remove with Defensive Check")
print("=" * 60)

def safe_remove_defensive(my_list, item):
    """
    Remove an item from the list safely using defensive programming.
    Use the 'in' operator to check BEFORE removing.
    
    Args:
        my_list: List to remove from (will be modified)
        item: Item to remove
    
    Returns:
        bool: True if removed, False if not found
    
    Example:
        fruits = ["apple", "banana", "cherry"]
        result = safe_remove_defensive(fruits, "banana")
        # Returns True, fruits is now ["apple", "cherry"]
        
        result = safe_remove_defensive(fruits, "grape")
        # Returns False, fruits unchanged
    
    TODO:
    1. Check if item is IN the list
    2. If yes: remove it and return True
    3. If no: return False (don't crash!)
    """
    # TODO: Implement defensive approach
    if item in my_list:
        my_list.remove(item)
        return True
    return False


if __name__ == "__main__":
    # Test 1.1
    test_list = ['apple', "banana", "cherry"]
    result = safe_remove_defensive(test_list, "banana")
    print(f"Test 1.1: {'✅PASS' if result == True and test_list == ['apple', 'cherry'] else '❌FAILED'}")
    print(test_list)
    
    # Test 1.2 - Item is not in the list
    test_list = ['apple', "banana", "cherry"]
    result = safe_remove_defensive(test_list, "grapes")
    print(f"Test 1.2: {'✅PASS' if result == True and test_list == ['apple', 'cherry'] else '❌FAILED'}")
    print(test_list)
    