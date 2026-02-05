"""
Lesson 1D Practice – References vs Copies
STARTER FILE (Code Writing Only)

Directions:
- Complete each function.
- Do NOT modify original lists unless explicitly intended.
"""

# --------------------------------------------------
# Question 5: Safe Top 3
# --------------------------------------------------

def get_top_3(scores):
    """
    Return the top 3 scores (highest first).
    MUST NOT modify the original list!

    Args:
        scores (list[int])

    Returns:
        list[int]
    """
    # TODO: Write your code here
    working = scores.copy()
    working.sort(reverse=True)
    return working[:3]


all_scores = [85, 92, 78, 95, 88, 91]
top_3 = get_top_3(all_scores)

print("Top 3:", top_3)
print("Original:", all_scores)


# # --------------------------------------------------
# # Question 6: Fix the Bug
# # --------------------------------------------------

# def add_bonus_item(inventory):
#     """
#     Add a bonus item WITHOUT modifying the original list.
#     """
#     # TODO: Fix the bug
#     pass

# player_items = ["sword", "shield", "potion"]
# bonus_inventory = add_bonus_item(player_items)

# print("Original:", player_items)
# print("Bonus:", bonus_inventory)


# # --------------------------------------------------
# # Question 7: Create Save State
# # --------------------------------------------------

# def create_save(player_items, player_level):
#     """
#     Create a save state that WON'T change later.
#     Returns:
#         dict with keys:
#         - 'items' (must be a COPY)
#         - 'level'
#     """
#     # TODO: Write your code here
#     pass

# items = ["sword", "shield"]
# level = 5
# save = create_save(items, level)

# items.append("potion")
# level = 6

# print("Current:", items, level)
# print("Save:", save)


# # --------------------------------------------------
# # Question 8: Backup Safely
# # --------------------------------------------------

# def backup_and_modify(data):
#     """
#     Return a backup that does NOT change when data is modified.
#     """
#     # TODO: Fix reference bug
#     pass


# original = ["item1", "item2"]
# result = backup_and_modify(original)

# print("Original:", original)
# print("Result:", result)
# print("Same object?", original is result)
