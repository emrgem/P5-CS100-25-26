# Part 1 - Basic elif examples
grade = 85
if grade >= 90:
    print('A - Excellent')
elif grade >= 80:
    print('B - Good Job!')
elif grade >= 70:
    print('C - Passing!')
elif grade >= 60:
    print('D - Need Improvement!')
else:
    print("F - Please retake!")

# Alternative assignment
grade = 85
result = ''
if grade >= 90:
    result = 'A - Excellent'
elif grade >= 80:
    result = 'B - Good Job!'
elif grade >= 70:
    result = 'C - Passing!'
elif grade >= 60:
    result = 'D - Need Improvement!'
else:
    result = "F - Please retake!"

print(f"Result: {result}")

# # Restaurant Menu System
# print('==Restaurant Menu System==')
# print('==========================')
# print("🍕 Welcome to Python Pizza!")
# print("1. Cheese Pizza - $12")
# print("2. Pepperoni Pizza - $14")
# print("3. Burger - $10")
# print("4. Salad - $8")
# print("5. Drink - $3")

# choice = int(input("Enter your choice (1-5): "))


# if choice == 1:
#     item = "Cheese Pizza"
#     price = 12
# elif choice == 2:
#     item = "Pepperoni Pizza"
#     price = 14
# elif choice == 3:
#     item = "Burger"
#     price = 10
# elif choice == 4:
#     item = "Salad"
#     price = 8
# elif choice == 5:
#     item = "Drink"
#     price = 3
# else:
#     item = "Invalid choice"
#     price = 0

# print(f"You ordered: {item}")
# print(f"Total cost: ${price}")

# Traffic Light Simulator
print("==Traffic Light Simulator==")
light_color = input("Enter Traffic Light Color").lower()
# print(light_color)
if light_color == 'red':
    print('STOP!')
elif light_color == 'yellow':
    print("Caution!")
elif light_color == 'green':
    print("Go!")
else:
    print("Unknown signal!")