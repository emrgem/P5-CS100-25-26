# ============================================
# LESSON 2B: Conditional Transformations
# ============================================

# KEY SYNTAX:
# -------------------------------------------------
# Filter:    [expr for item in list if cond]        ← if at END
# Transform: [A if cond else B for item in list]    ← if-else at START
# -------------------------------------------------

# THE BIG DISTINCTION:
# • if at END       → FILTER    → fewer items (removes some)
# • if-else at START → TRANSFORM → same items (changes all)


# ============================================
# PRACTICE 1: Basic If-Else Transform
# ============================================

# Create labels: "Pass" if score >= 70, else "Fail"
scores = [88, 72, 95, 61, 84]

# TODO: Write your comprehension here
# results = 

# print("P1:", results)
# Expected: ["Pass", "Pass", "Pass", "Fail", "Pass"]


# ============================================
# PRACTICE 2: Size Categories
# ============================================

# Create labels: "small" if under 1000, else "big"
followers = [500, 1500, 8000, 200, 12000]

# TODO: Write your comprehension here
# labels = 

# print("P2:", labels)
# Expected: ["small", "big", "big", "small", "big"]


# ============================================
# PRACTICE 3: Filter vs Transform
# ============================================

# Use the SAME data for both:
nums = [2, 5, 8, 3, 9, 1]

# TODO: Write a FILTER - keep only numbers > 4
# filtered = 

# TODO: Write a TRANSFORM - label as "big" if > 4, else "small"  
# transformed = 

# print("P3 Filter:", filtered)
# print("P3 Transform:", transformed)
# 
# How many items in each? Why are they different?


# ============================================
# PRACTICE 4: Choose the Right Tool
# ============================================

# Scenario: You need ONLY the passing scores (70+)
# You want [85, 91, 77] - just 3 numbers, not labels

scores = [85, 62, 91, 58, 77, 69]

# TODO: Which pattern gives you just the passing scores?
# passing = 

# print("P4:", passing)
# Expected: [85, 91, 77]


# ============================================
# PRACTICE 5: Song Duration Labels
# ============================================

# Label songs: "short" if under 3 min (180 sec), 
#              "medium" if under 5 min (300 sec),
#              "long" otherwise

song_lengths = [120, 240, 180, 360, 150, 290]

# TODO: Write your comprehension (hint: chain if-else)
# labels = 

# print("P5:", labels)
# Expected: ["short", "medium", "short", "long", "short", "medium"]


# ============================================
# BONUS: Side-by-Side Comparison
# ============================================
# Uncomment and run to see the difference clearly

# numbers = [1, 2, 3, 4, 5, 6]
# 
# filtered = [n for n in numbers if n > 3]
# transformed = ["big" if n > 3 else "small" for n in numbers]
# 
# print("Original:", numbers, "Length:", len(numbers))
# print("Filtered:", filtered, "Length:", len(filtered))
# print("Transformed:", transformed, "Length:", len(transformed))
