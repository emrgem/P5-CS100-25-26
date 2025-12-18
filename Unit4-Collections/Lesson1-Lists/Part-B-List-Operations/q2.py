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
    # if item in my_list:
    #     my_list.remove(item)
    #     return True
    # return False
    pass


# ==================== PROBLEM 2: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 2: Safe Remove with Exception Handling")
print("=" * 60)



