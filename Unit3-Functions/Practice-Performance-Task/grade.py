import sys

# Function to run tests and calculate score for each task

def run_task1_tests():
    try:
        from task1_starter import convert_to_stars
    except ImportError:
        print("Error: Cannot import convert_to_stars from task1_starter.py")
        return 0.0
    except Exception as e:
        print(f"Error in Task 1 import: {e}")
        return 0.0

    passed = 0
    total = 5

    try:
        result1 = convert_to_stars(95)
        if result1 == 5:
            passed += 1
    except Exception as e:
        print(f"Error in Task 1 test1: {e}")

    try:
        result2 = convert_to_stars(73)
        if result2 == 4:
            passed += 1
    except Exception as e:
        print(f"Error in Task 1 test2: {e}")

    try:
        result3 = convert_to_stars(45)
        if result3 == 3:
            passed += 1
    except Exception as e:
        print(f"Error in Task 1 test3: {e}")

    try:
        result4 = convert_to_stars(30)
        if result4 == 2:
            passed += 1
    except Exception as e:
        print(f"Error in Task 1 test4: {e}")

    try:
        result5 = convert_to_stars(15)
        if result5 == 1:
            passed += 1
    except Exception as e:
        print(f"Error in Task 1 test5: {e}")

    score = (passed / total) * 25
    print(f"Task 1: {passed}/{total} tests passed, score: {score:.2f}/25")
    return score

def run_task2_tests():
    try:
        from task2_starter import format_review
    except ImportError:
        print("Error: Cannot import format_review from task2_starter.py")
        return 0.0
    except Exception as e:
        print(f"Error in Task 2 import: {e}")
        return 0.0

    passed = 0
    total = 3

    try:
        result1 = format_review("Inception", 9)
        expected1 = "Inception - Rating: 9/10 (Reviewed by: Anonymous)"
        if result1 == expected1:
            passed += 1
    except Exception as e:
        print(f"Error in Task 2 test1: {e}")

    try:
        result2 = format_review("The Matrix", 10, "Alex")
        expected2 = "The Matrix - Rating: 10/10 (Reviewed by: Alex)"
        if result2 == expected2:
            passed += 1
    except Exception as e:
        print(f"Error in Task 2 test2: {e}")

    try:
        result3 = format_review("Frozen", 8, reviewer="Jordan")
        expected3 = "Frozen - Rating: 8/10 (Reviewed by: Jordan)"
        if result3 == expected3:
            passed += 1
    except Exception as e:
        print(f"Error in Task 2 test3: {e}")

    score = (passed / total) * 25
    print(f"Task 2: {passed}/{total} tests passed, score: {score:.2f}/25")
    return score

def run_task3_tests():
    try:
        from task3_starter import parse_rating
    except ImportError:
        print("Error: Cannot import parse_rating from task3_starter.py")
        return 0.0
    except Exception as e:
        print(f"Error in Task 3 import: {e}")
        return 0.0

    passed = 0
    total = 4

    try:
        result1 = parse_rating("8.5")
        if result1 == 8.5:
            passed += 1
    except Exception as e:
        print(f"Error in Task 3 test1: {e}")

    try:
        result2 = parse_rating("10")
        if result2 == 10.0:
            passed += 1
    except Exception as e:
        print(f"Error in Task 3 test2: {e}")

    try:
        result3 = parse_rating("seven")
        if result3 == -1.0:
            passed += 1
    except Exception as e:
        print(f"Error in Task 3 test3: {e}")

    try:
        result4 = parse_rating("")
        if result4 == -1.0:
            passed += 1
    except Exception as e:
        print(f"Error in Task 3 test4: {e}")

    score = (passed / total) * 25
    print(f"Task 3: {passed}/{total} tests passed, score: {score:.2f}/25")
    return score

def run_task4_tests():
    try:
        from task4_starter import validate_rating
    except ImportError:
        print("Error: Cannot import validate_rating from task4_starter.py")
        return 0.0
    except Exception as e:
        print(f"Error in Task 4 import: {e}")
        return 0.0

    passed = 0
    total = 5

    try:
        result1 = validate_rating(7.5)
        if result1 == True:
            passed += 1
    except Exception as e:
        print(f"Error in Task 4 test1: {e}")

    try:
        result2 = validate_rating(0)
        if result2 == True:
            passed += 1
    except Exception as e:
        print(f"Error in Task 4 test2: {e}")

    try:
        result3 = validate_rating(10)
        if result3 == True:
            passed += 1
    except Exception as e:
        print(f"Error in Task 4 test3: {e}")

    # Test negative
    try:
        validate_rating(-3)
    except ValueError as e:
        expected_msg = "Rating cannot be negative"
        if expected_msg in str(e):
            passed += 1
        else:
            print(f"Task 4 negative test: wrong message - Got: {e}")
    except Exception as e:
        print(f"Task 4 negative test: wrong error type: {type(e).__name__}")
    else:
        print("Task 4 negative test: No error raised ✗")

    # Test exceed 10
    try:
        validate_rating(15)
    except ValueError as e:
        expected_msg = "Rating cannot exceed 10"
        if expected_msg in str(e):
            passed += 1
        else:
            print(f"Task 4 exceed test: wrong message - Got: {e}")
    except Exception as e:
        print(f"Task 4 exceed test: wrong error type: {type(e).__name__}")
    else:
        print("Task 4 exceed test: No error raised ✗")

    score = (passed / total) * 25
    print(f"Task 4: {passed}/{total} tests passed, score: {score:.2f}/25")
    return score

if __name__ == "__main__":
    score1 = run_task1_tests()
    score2 = run_task2_tests()
    score3 = run_task3_tests()
    score4 = run_task4_tests()
    total_score = score1 + score2 + score3 + score4
    print(f"Total score: {total_score:.2f}/100")