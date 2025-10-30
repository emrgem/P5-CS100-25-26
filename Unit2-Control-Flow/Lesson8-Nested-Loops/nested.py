# Simple Grid 3x3
for row in range(3):
    for col in range(3):
        # print("hello")
        # print("hello", end=" ")
        # print("*", end=" ")
        print("⬜", end=" ")
    print()
    
# Create a 4x5 rectangle: star emoji
# for row in range(4):
#     for col in range(5):
#         print("⭐", end=" ")
#     print()
    
# Printing Row and Column Numbers
# for row in range(3):
#     for col in range(3):
#         print(f"({row},{col})", end=" ")
#     print()
    
# Star Triangle Ascending
# for row in range(5):
#     for col in range(row + 1):
#         # print(f"({row},{col})", end=" ")
#         print(f"⭐", end=" ")
#     print()
    
# Star Triangle Descending
for row in range(5,0,-1):
    for col in range(row):
        # print(f"⭐", end=" ")
        print(f"({row},{col})", end=" ")
    print()
