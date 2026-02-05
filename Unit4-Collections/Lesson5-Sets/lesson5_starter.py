# unit4_lesson5_sets_data.py

# ===== DATA FROM SLIDES =====

# Slide: Problem 1 - Duplicates
favorites_list = ["Blinding Lights", "Bad Guy", "Blinding Lights"]

# Slide: Set solution
favorites_set = {"Blinding Lights", "Bad Guy", "Blinding Lights"}
print(len(favorites_set))
# Slide: Creating sets with curly braces
genres = {"Rock", "Pop", "Jazz"}

# Slide: Creating sets from list
numbers_list = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers_list)
print(unique_numbers)
# Slide: Empty set examples
empty_dict = {}  # This is a dict, not a set!
empty_set = set()  # Correct empty set

# Slide: Quick check data
quick_check_data = {5, 3, 5, 1, 3, 5, 2, 1}

# Slide: Membership check
colors = {"red", "green", "blue"}

print("red" in colors) #True
print("yellow" in colors) #False

# Slide: Adding items example
tags = {"python", "coding"}  # We'll add "tutorial" during lesson
tags.add("Java")
tags.add("JavaScript")
print(tags)

tags.remove("Java") # will remove Java
# tags.remove("C++") # remove() can error KeyError

tags.discard("C++") # Safe Remove - NO Error

# Slide: Set operations data
gamers = {"Alice", "Bob", "Charlie", "Diana"}
coders = {"Bob", "Diana", "Eve", "Frank"}

# & Intersection - Items in BOTH sets
both = gamers & coders
print(both)

# | Union - All unique items from both
everyone = gamers | coders
print(everyone)

# - Difference - Items in First but NOT second
gamers_only = gamers - coders
print(gamers_only)

# Slide: Another quick check
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Slide: Remove duplicates pattern
scores = [85, 92, 78, 85, 90, 78]
unique_Scores = list(set(scores))
print(unique_Scores)

sorted_scores = sorted(set(scores))
print(sorted_scores)

# Slide: We do together - Playlists
my_songs = {"Song A", "Song B", "Song C"}
friend_songs = {"Song B", "Song C", "Song D"}
