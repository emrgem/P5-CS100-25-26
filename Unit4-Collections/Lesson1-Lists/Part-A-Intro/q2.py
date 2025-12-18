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
    shopping = ["bananas", "yogurt", "chicken", "rice", "pasta", "tomatoes"]    
    # TODO: Count the items
    # count = len(...)
    count = len(shopping)
    
    # TODO: Return both
    # return shopping, count
    return shopping, count

if __name__ == "__main__":
    shopping, count = create_shopping_list()
    print(f"Shopping List: {shopping}")
    print(f"Count: {count}")