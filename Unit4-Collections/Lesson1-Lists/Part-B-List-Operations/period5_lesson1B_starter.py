"""
Period 5 - Unit 4, Lesson 1B Practice: List Operations
======================================================

Complete the functions below. Run this file to test your solutions!
All tests are provided - your job is to make them pass.

Remember: You can use EITHER defensive checks OR try/except!
"""

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
    # if item in my_list:
    #     my_list.remove(item)
    #     return True
    # return False
    pass


# ==================== PROBLEM 2: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 2: Safe Remove with Exception Handling")
print("=" * 60)

def safe_remove_exception(my_list, item):
    """
    Remove an item from the list safely using exception handling.
    Use try/except to catch ValueError.
    
    Args:
        my_list: List to remove from (will be modified)
        item: Item to remove
    
    Returns:
        bool: True if removed, False if not found
    
    Example:
        fruits = ["apple", "banana", "cherry"]
        result = safe_remove_exception(fruits, "banana")
        # Returns True, fruits is now ["apple", "cherry"]
        
        result = safe_remove_exception(fruits, "grape")
        # Returns False, fruits unchanged
    
    TODO:
    1. Try to remove the item
    2. If ValueError happens, catch it and return False
    3. If successful, return True
    """
    # TODO: Implement exception handling approach
    # try:
    #     my_list.remove(item)
    #     return True
    # except ValueError:
    #     return False
    pass


# ==================== PROBLEM 3: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 3: Queue Manager")
print("=" * 60)

def manage_queue(queue, action, person):
    """
    Manage a queue of people.
    
    Args:
        queue: List of people in queue (will be modified)
        action: "add_end", "add_front", or "serve"
        person: Person to add (not used for "serve")
    
    Returns:
        str: Message about what happened, or None if serve from empty queue
    
    Examples:
        queue = ["Alice", "Bob"]
        result = manage_queue(queue, "add_end", "Charlie")
        # Returns "Charlie added to end", queue is ["Alice", "Bob", "Charlie"]
        
        result = manage_queue(queue, "add_front", "Dave")
        # Returns "Dave added to front", queue is ["Dave", "Alice", "Bob", "Charlie"]
        
        result = manage_queue(queue, "serve", None)
        # Returns "Served: Dave", queue is ["Alice", "Bob", "Charlie"]
    
    TODO:
    1. If action is "add_end": append person, return message
    2. If action is "add_front": insert at index 0, return message
    3. If action is "serve": 
       - If queue is empty, return None
       - Otherwise, pop(0) and return "Served: {person}"
    """
    # TODO: Implement queue management
    # if action == "add_end":
    #     queue.append(person)
    #     return f"{person} added to end"
    # elif action == "add_front":
    #     queue.insert(0, person)
    #     return f"{person} added to front"
    # elif action == "serve":
    #     if len(queue) == 0:
    #         return None
    #     served_person = queue.pop(0)
    #     return f"Served: {served_person}"
    pass


# ==================== TESTS ====================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("RUNNING TESTS")
    print("=" * 60)
    
    # Test Problem 1: safe_remove_defensive
    print("\n--- Testing Problem 1: safe_remove_defensive ---")
    
    # Test 1.1: Remove existing item
    test_list = ["apple", "banana", "cherry"]
    result = safe_remove_defensive(test_list, "banana")
    print(f"Test 1.1: {'✅ PASS' if result == True and test_list == ['apple', 'cherry'] else '❌ FAIL'}")
    print(f"  Expected: True, ['apple', 'cherry']")
    print(f"  Got: {result}, {test_list}")
    
    # Test 1.2: Try to remove non-existent item
    test_list = ["apple", "cherry"]
    result = safe_remove_defensive(test_list, "grape")
    print(f"Test 1.2: {'✅ PASS' if result == False and test_list == ['apple', 'cherry'] else '❌ FAIL'}")
    print(f"  Expected: False, ['apple', 'cherry'] (unchanged)")
    print(f"  Got: {result}, {test_list}")
    
    # Test 1.3: Remove from empty list
    test_list = []
    result = safe_remove_defensive(test_list, "anything")
    print(f"Test 1.3: {'✅ PASS' if result == False and test_list == [] else '❌ FAIL'}")
    print(f"  Expected: False, [] (no crash!)")
    print(f"  Got: {result}, {test_list}")
    
    # Test Problem 2: safe_remove_exception
    print("\n--- Testing Problem 2: safe_remove_exception ---")
    
    # Test 2.1: Remove existing item
    test_list = ["apple", "banana", "cherry"]
    result = safe_remove_exception(test_list, "banana")
    print(f"Test 2.1: {'✅ PASS' if result == True and test_list == ['apple', 'cherry'] else '❌ FAIL'}")
    print(f"  Expected: True, ['apple', 'cherry']")
    print(f"  Got: {result}, {test_list}")
    
    # Test 2.2: Try to remove non-existent item
    test_list = ["apple", "cherry"]
    result = safe_remove_exception(test_list, "grape")
    print(f"Test 2.2: {'✅ PASS' if result == False and test_list == ['apple', 'cherry'] else '❌ FAIL'}")
    print(f"  Expected: False, ['apple', 'cherry'] (unchanged)")
    print(f"  Got: {result}, {test_list}")
    
    # Test 2.3: Remove from empty list
    test_list = []
    result = safe_remove_exception(test_list, "anything")
    print(f"Test 2.3: {'✅ PASS' if result == False and test_list == [] else '❌ FAIL'}")
    print(f"  Expected: False, [] (no crash!)")
    print(f"  Got: {result}, {test_list}")
    
    # Test Problem 3: manage_queue
    print("\n--- Testing Problem 3: manage_queue ---")
    
    # Test 3.1: Add to end
    queue = ["Alice", "Bob"]
    result = manage_queue(queue, "add_end", "Charlie")
    print(f"Test 3.1: {'✅ PASS' if result == 'Charlie added to end' and queue == ['Alice', 'Bob', 'Charlie'] else '❌ FAIL'}")
    print(f"  Expected: 'Charlie added to end', ['Alice', 'Bob', 'Charlie']")
    print(f"  Got: '{result}', {queue}")
    
    # Test 3.2: Add to front
    queue = ["Alice", "Bob"]
    result = manage_queue(queue, "add_front", "Dave")
    print(f"Test 3.2: {'✅ PASS' if result == 'Dave added to front' and queue == ['Dave', 'Alice', 'Bob'] else '❌ FAIL'}")
    print(f"  Expected: 'Dave added to front', ['Dave', 'Alice', 'Bob']")
    print(f"  Got: '{result}', {queue}")
    
    # Test 3.3: Serve from queue
    queue = ["Dave", "Alice", "Bob"]
    result = manage_queue(queue, "serve", None)
    print(f"Test 3.3: {'✅ PASS' if result == 'Served: Dave' and queue == ['Alice', 'Bob'] else '❌ FAIL'}")
    print(f"  Expected: 'Served: Dave', ['Alice', 'Bob']")
    print(f"  Got: '{result}', {queue}")
    
    # Test 3.4: Serve from empty queue
    queue = []
    result = manage_queue(queue, "serve", None)
    print(f"Test 3.4: {'✅ PASS' if result is None and queue == [] else '❌ FAIL'}")
    print(f"  Expected: None, [] (no crash!)")
    print(f"  Got: {result}, {queue}")
    
    # Test 3.5: Multiple operations
    queue = []
    manage_queue(queue, "add_end", "Alice")
    manage_queue(queue, "add_end", "Bob")
    manage_queue(queue, "add_front", "Priority")
    manage_queue(queue, "serve", None)
    print(f"Test 3.5: {'✅ PASS' if queue == ['Alice', 'Bob'] else '❌ FAIL'}")
    print(f"  Expected: ['Alice', 'Bob'] (after add, add, add_front, serve)")
    print(f"  Got: {queue}")
    
    print("\n" + "=" * 60)
    print("Tests complete! Check your results above.")
    print("=" * 60)
    print("\nHINTS:")
    print("- Problem 1: Use 'if item in my_list' to check first")
    print("- Problem 2: Use 'try/except ValueError' to catch errors")
    print("- Problem 3: Use append(), insert(0, person), and pop(0)")
