"""
Period 5 - Unit 4, Lesson 1A Practice: Your First Collection
============================================================
"""
# ==================== PROBLEM 2: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 2: Create Shopping List and Count Items")
print("=" * 60)

def create_shopping_list():
    """
    Create a shopping list with at least 5 items.
    Return the list AND the count of items.
    
    Returns:
        tuple: (list of items, count of items)
    
    Example:
        shopping, count = create_shopping_list()
        # shopping might be ["milk", "bread", "eggs", "cheese", "apples"]
        # count would be 5
    
    TODO:
    1. Create a list with 5 shopping items (strings)
    2. Count how many items using len()
    3. Return both the list and the count as a tuple
    """
    # TODO: Create your shopping list here
    # shopping = [...]
    
    # TODO: Count the items
    # count = len(...)
    
    # TODO: Return both
    # return shopping, count
    pass


# ==================== PROBLEM 3: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 3: Add Items and Calculate Total")
print("=" * 60)

def calculate_test_average(test_scores):
    """
    Given a list of test scores, add one more score and calculate average.
    
    Args:
        test_scores: List of integers (existing test scores)
    
    Returns:
        float: The average of all scores (including the new one)
    
    Example:
        scores = [85, 90, 88]
        avg = calculate_test_average(scores)
        # Should add a score and return average of all scores
    
    TODO:
    1. Add one more test score (any number 0-100) using append()
    2. Calculate the total of ALL scores (use a loop!)
    3. Calculate average: total / len(test_scores)
    4. Return the average
    """
    # TODO: Add a new score (pick any number 0-100)
    # test_scores.append(...)
    
    # TODO: Calculate total using a loop
    # total = 0
    # for score in test_scores:
    #     total += score
    
    # TODO: Calculate average
    # average = total / len(test_scores)
    
    # TODO: Return average
    # return average
    pass


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
    # try:
    #     return my_list[index]
    # except IndexError:
    #     return None
    pass


# ==================== TESTS ====================
