# ============================================================
# LIST COMPREHENSIONS - CLASS PRACTICE WORKSHEET
# ============================================================
# 20 Questions | Covers Lessons 2A & 2B | Matches Slide Deck
# 
# SYNTAX REFERENCE:
# Basic:     [expression for item in list]
# Filter:    [expression for item in list if condition]
# Transform: [A if condition else B for item in list]
#
# REMEMBER:
# • if at END → filter (removes items)
# • if-else at START → transform (keeps all items)
# ============================================================

# ============================================================
print("=" * 60)
print("SECTION 1: BASIC COMPREHENSIONS")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ1. Convert to Comprehension - Double each number")
print("Expected: [2, 4, 6, 8, 10]")
print("-" * 40)
# ----------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# TODO:
doubled = []
print("Q1 Result:", doubled)


# ----------------------------------------------------------
print("\nQ2. Create squares of 1-5 using range()")
print("Expected: [1, 4, 9, 16, 25]")
print("-" * 40)
# ----------------------------------------------------------

# TODO:
# squares = 
# print("Q2 Result:", squares)


# ----------------------------------------------------------
print("\nQ3. Uppercase all words")
print("Expected: ['CAT', 'DOG', 'BIRD']")
print("-" * 40)
# ----------------------------------------------------------
words = ["cat", "dog", "bird"]

# TODO:
# result = 
# print("Q3 Result:", result)


# ============================================================
print("\n")
print("=" * 60)
print("SECTION 2: FILTERING (if at END)")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ4. Convert to Comprehension - Keep scores >= 70")
print("Expected: [85, 92, 78, 95]")
print("-" * 40)
# ----------------------------------------------------------
scores = [85, 60, 92, 55, 78, 95]

# TODO:
# passing = 
# print("Q4 Result:", passing)


# ----------------------------------------------------------
print("\nQ5. Keep numbers greater than 5 - How many items?")
print("Expected: 3 items")
print("-" * 40)
# ----------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# TODO:
# result = 
# print("Q5 Result:", result)
# print("Count:", len(result))


# ----------------------------------------------------------
print("\nQ6. Numbers > 12 AND double them")
print("Expected: [50, 60, 30]")
print("-" * 40)
# ----------------------------------------------------------
nums = [10, 25, 8, 30, 15]

# TODO:
# result = 
# print("Q6 Result:", result)


# ============================================================
print("\n")
print("=" * 60)
print("SECTION 3: TRANSFORM (if-else at START)")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ7. Convert to Comprehension - Label temps as hot/cool")
print("Expected: ['cool', 'hot', 'cool', 'hot', 'cool']")
print("-" * 40)
# ----------------------------------------------------------
temps = [65, 82, 70, 90, 75]

# TODO:
# labels = 
# print("Q7 Result:", labels)


# ----------------------------------------------------------
print("\nQ8. Label numbers as even/odd - How many items?")
print("Expected: 8 items")
print("-" * 40)
# ----------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# TODO:
# result = 
# print("Q8 Result:", result)
# print("Count:", len(result))


# ============================================================
print("\n")
print("=" * 60)
print("SECTION 4: FILTER vs TRANSFORM")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ9. THE BIG QUESTION - What's the difference?")
print("Version A: [n for n in nums if n > 0]")
print("Version B: [n if n > 0 else 0 for n in nums]")
print("-" * 40)
# ----------------------------------------------------------
nums = [5, -3, 8, -1, 0]

# TODO: Try both versions and see the difference
# version_a = 
# version_b = 
# print("Version A (filter):", version_a)
# print("Version B (transform):", version_b)


# ----------------------------------------------------------
print("\nQ10. Filter empty strings")
print("Expected: ['alice', 'bob', 'charlie'] and count of 3")
print("-" * 40)
# ----------------------------------------------------------
names = ["", "alice", "", "bob", "charlie", ""]

# TODO:
# result = 
# print("Q10 Result:", result)
# print("Count:", len(result))


# ============================================================
print("\n")
print("=" * 60)
print("SECTION 5: COMPREHENSION vs LOOP")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ11. Write this comprehension as a loop")
print("cubes = [x ** 3 for x in range(1, 5)]")
print("-" * 40)
# ----------------------------------------------------------

# TODO: Write as a loop
# cubes = []
# for x in range(1, 5):
#     ...
# print("Q11 Result:", cubes)


# ----------------------------------------------------------
print("\nQ12. Create even numbers 2-20 using range()")
print("Expected: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]")
print("-" * 40)
# ----------------------------------------------------------

# TODO: Two options - use step in range OR use filter
# Option 1:
# evens = 

# Option 2:
# evens = 

# print("Q12 Result:", evens)


# ============================================================
print("\n")
print("=" * 60)
print("SECTION 6: CHOOSE FILTER OR TRANSFORM")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ13. Keep ONLY negative numbers (the actual values)")
print("Expected: [-3, -1, -7]")
print("-" * 40)
# ----------------------------------------------------------
nums = [5, -3, 8, -1, 0, -7]

# TODO: Use FILTER
# negatives = 
# print("Q13 Result:", negatives)


# ----------------------------------------------------------
print("\nQ14. Label EVERY number as pos/neg/zero")
print("Expected: ['pos', 'neg', 'pos', 'neg', 'zero', 'neg']")
print("-" * 40)
# ----------------------------------------------------------
nums = [5, -3, 8, -1, 0, -7]

# TODO: Use TRANSFORM
# labels = 
# print("Q14 Result:", labels)


# ----------------------------------------------------------
print("\nQ15. Format prices > 10")
print("Expected: ['$24.99', '$15.00']")
print("-" * 40)
# ----------------------------------------------------------
prices = [9.99, 24.99, 4.99, 15.00]

# TODO:
# result = 
# print("Q15 Result:", result)


# ============================================================
print("\n")
print("=" * 60)
print("SECTION 7: FIX THE BUG")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ16. Fix the bug")
print("This crashes: result = [n if n > 2 for n in numbers]")
print("-" * 40)
# ----------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# ❌ This crashes:
# result = [n if n > 2 for n in numbers]

# TODO: Write correct version (filter OR transform)
# Filter version:
# result = 

# Transform version:
# result = 

# print("Q16 Result:", result)


# ----------------------------------------------------------
print("\nQ17. Write this comprehension as a loop")
print('result = ["big" if x > 10 else "small" for x in [5, 15, 8, 20]]')
print("-" * 40)
# ----------------------------------------------------------

# TODO: Write as a loop
# result = []
# for x in [5, 15, 8, 20]:
#     ...
# print("Q17 Result:", result)


# ============================================================
print("\n")
print("=" * 60)
print("SECTION 8: CHALLENGES")
print("=" * 60)
# ============================================================

# ----------------------------------------------------------
print("\nQ18. Challenge: From 1-30, get squares of numbers divisible by 5")
print("Expected: [25, 100, 225, 400, 625, 900]")
print("-" * 40)
# ----------------------------------------------------------

# TODO:
# result = 
# print("Q18 Result:", result)


# ----------------------------------------------------------
print("\nQ19. Quick Fire: What's the Length?")
print("-" * 40)
# ----------------------------------------------------------
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: Predict the length before running!
# basic = [x for x in data]
# filtered = [x for x in data if x > 5]
# transformed = ["y" if x > 5 else "n" for x in data]

# print("Basic length:", len(basic))
# print("Filtered length:", len(filtered))
# print("Transformed length:", len(transformed))


# ----------------------------------------------------------
print("\nQ20. Final Boss: From 1-20, keep odd numbers and cube them")
print("Expected: [1, 27, 125, 343, 729, 1331, 2197, 3375, 4913, 6859]")
print("-" * 40)
# ----------------------------------------------------------

# TODO:
# result = 
# print("Q20 Result:", result)


# ============================================================
print("\n")
print("=" * 60)
print("END OF PRACTICE - 20 QUESTIONS COMPLETE!")
print("=" * 60)
# ============================================================
