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
    test_scores.append(60)
    # TODO: Calculate total using a loop
    total = 0
    for score in test_scores:
        total += score
    
    # TODO: Calculate average
    average = total / len(test_scores)
    
    # TODO: Return average
    return average

if __name__ == "__main__":
    test_scores = [85, 90, 88]
    print(f"Original scores: {test_scores}")
    avg = calculate_test_average(test_scores)
    print(f"After adding score: {test_scores}")
    print(f"Average: {avg}")