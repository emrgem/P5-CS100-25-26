"""
Unit 4 Review Practice - Starter File
=====================================
8 practice problems covering lists, dictionaries, tuples, and sets.

Instructions:
- Complete each function according to its docstring
- Run this file to test your solutions
- All tests should pass when you're done!
"""


# ============================================================
# PROBLEM 1: List Basics - Gaming Inventory
# ============================================================
def build_inventory():
    """
    Build a gaming inventory list.
    
    Steps:
    1. Create a list called 'inventory' with: "sword", "shield", "potion"
    2. Add "bow" to the end using append()
    3. Remove "shield" from the list using remove()
    4. Return the length of the final inventory
    
    Returns:
        int: The number of items remaining (should be 3)
    
    Example:
        >>> build_inventory()
        3
    """
    
    


# ============================================================
# PROBLEM 2: Dictionary Basics - Player Profile
# ============================================================
def get_player_info():
    """
    Create and access a player profile dictionary.
    
    Steps:
    1. Create a dictionary 'player' with: "name" -> "Alex", "level" -> 5
    2. Add a new key "score" with value 1500
    3. Use .get() to safely get "rank" with default "Unranked"
    4. Return a tuple: (player's name, rank)
    
    Returns:
        tuple: (name, rank) - should be ("Alex", "Unranked")
    
    Example:
        >>> get_player_info()
        ('Alex', 'Unranked')
    """
    # YOUR CODE HERE
    player = {"name": "Alex", "level":5}
    player["score"] = 1500
    rank = player.get("rank", "Unranked")
    return (player["name"], rank)


# ============================================================
# PROBLEM 3: Tuple Unpacking - Coordinates
# ============================================================
def format_position():
    """
    Use tuple unpacking to format a position string.
    
    Steps:
    1. Create a tuple 'position' with values: (150, 300, "spawn")
    2. Unpack into three variables: x, y, location
    3. Return a formatted string: "Player at (150, 300) - spawn"
    
    Returns:
        str: Formatted position string
    
    Example:
        >>> format_position()
        'Player at (150, 300) - spawn'
    """
    # YOUR CODE HERE
    pass


# ============================================================
# PROBLEM 4: Set Operations - Find Common Songs
# ============================================================
def find_common_songs():
    """
    Use set intersection to find songs two people both like.
    
    Steps:
    1. Create set 'my_songs' with: "Song A", "Song B", "Song C"
    2. Create set 'friend_songs' with: "Song B", "Song C", "Song D"
    3. Find the intersection (songs both have)
    4. Return the set of common songs
    
    Returns:
        set: Songs that appear in both sets
    
    Example:
        >>> find_common_songs()
        {'Song B', 'Song C'}
    """
    # YOUR CODE HERE
    pass


# ============================================================
# PROBLEM 5: List + Loop - Shopping Cart Total
# ============================================================
def calculate_total():
    """
    Calculate the total of a shopping cart using a loop.
    
    Steps:
    1. Create list 'prices' with: 9.99, 24.99, 4.99, 15.00
    2. Use a for loop to add up all prices
    3. Return the total (should be 54.97)
    
    Returns:
        float: The sum of all prices
    
    Example:
        >>> calculate_total()
        54.97
    """
    # YOUR CODE HERE
    pass


# ============================================================
# PROBLEM 6: Dict + Loop - Display Scores
# ============================================================
def get_score_strings():
    """
    Create formatted score strings from a dictionary.
    
    Steps:
    1. Create dict 'scores' with: "Alice" -> 95, "Bob" -> 87, "Charlie" -> 92
    2. Loop through using .items()
    3. Build a list of strings like: "Alice: 95 points"
    4. Return the list of formatted strings
    
    Returns:
        list: List of formatted score strings
    
    Example:
        >>> get_score_strings()
        ['Alice: 95 points', 'Bob: 87 points', 'Charlie: 92 points']
    """
    # YOUR CODE HERE
    pass


# ============================================================
# PROBLEM 7: Remove Duplicates with Set
# ============================================================
def clean_and_sort(numbers):
    """
    Remove duplicates from a list and return sorted unique values.
    
    Steps:
    1. Convert the list to a set (removes duplicates)
    2. Convert back to a sorted list
    3. Return the clean, sorted list
    
    Args:
        numbers (list): A list that may contain duplicates
    
    Returns:
        list: Sorted list with no duplicates
    
    Example:
        >>> clean_and_sort([5, 2, 8, 2, 9, 5, 1, 8])
        [1, 2, 5, 8, 9]
    """
    # YOUR CODE HERE
    pass


# ============================================================
# PROBLEM 8: Function Returns Tuple
# ============================================================
def get_stats(numbers):
    """
    Calculate and return multiple statistics as a tuple.
    
    Steps:
    1. Find the minimum value
    2. Find the maximum value  
    3. Calculate the sum/total
    4. Return all three as a tuple: (min, max, total)
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        tuple: (minimum, maximum, total)
    
    Example:
        >>> get_stats([10, 25, 5, 30, 15])
        (5, 30, 85)
    """
    # YOUR CODE HERE
    pass


# ============================================================
# TEST CODE - Run this file to check your answers!
# ============================================================
def run_tests():
    """Run all tests and display results."""
    print("=" * 50)
    print("UNIT 4 REVIEW - PRACTICE TESTS")
    print("=" * 50)
    
    all_passed = True
    
    # Test Problem 1
    print("\n📦 Problem 1: build_inventory()")
    try:
        result = build_inventory()
        if result == 3:
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected 3, got {result}")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Test Problem 2
    print("\n👤 Problem 2: get_player_info()")
    try:
        result = get_player_info()
        expected = ("Alex", "Unranked")
        if result == expected:
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected {expected}, got {result}")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Test Problem 3
    print("\n📍 Problem 3: format_position()")
    try:
        result = format_position()
        expected = "Player at (150, 300) - spawn"
        if result == expected:
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected '{expected}', got '{result}'")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Test Problem 4
    print("\n🎵 Problem 4: find_common_songs()")
    try:
        result = find_common_songs()
        expected = {"Song B", "Song C"}
        if result == expected:
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected {expected}, got {result}")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Test Problem 5
    print("\n🛒 Problem 5: calculate_total()")
    try:
        result = calculate_total()
        expected = 54.97
        if abs(result - expected) < 0.01:  # Allow small float variance
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected {expected}, got {result}")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Test Problem 6
    print("\n🏆 Problem 6: get_score_strings()")
    try:
        result = get_score_strings()
        expected = ['Alice: 95 points', 'Bob: 87 points', 'Charlie: 92 points']
        if result == expected:
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected {expected}")
            print(f"              Got {result}")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Test Problem 7
    print("\n🔄 Problem 7: clean_and_sort()")
    try:
        result = clean_and_sort([5, 2, 8, 2, 9, 5, 1, 8])
        expected = [1, 2, 5, 8, 9]
        if result == expected:
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected {expected}, got {result}")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Test Problem 8
    print("\n📊 Problem 8: get_stats()")
    try:
        result = get_stats([10, 25, 5, 30, 15])
        expected = (5, 30, 85)
        if result == expected:
            print("   ✅ PASSED!")
        else:
            print(f"   ❌ FAILED: Expected {expected}, got {result}")
            all_passed = False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        all_passed = False
    
    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Great work!")
    else:
        print("❌ Some tests failed. Keep working!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
