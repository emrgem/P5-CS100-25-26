# LESSON 6: USER INPUT & PROCESSING - STARTER CODE
# Follow along with your teacher!

# PART 1: Basic Input
print("\n--- PART 1: Basic Input ---")
# Try getting user's name and printing it
# name = input("Enter your name:")
# print(f"Hello, {name}!")
# print(f"Type of name: {type(name)}")

# Try getting a number and adding 1 (this will cause an error!)
# num1 = int(input("Enter a number:"))
# print(f"{num1}+1 = {num1+1}")

# PART 2: Type Conversion  
print("\n--- PART 2: Type Conversion ---")
# Fix the number problem using int()


# Try different conversion functions
# user_name = input("Enter your name: ")
# fav_number = int(input("Enter your favorite number: "))
# doubled = fav_number * 2
# print(f"Hi {user_name}! Your number doubled is {doubled}")

# PART 3: Math Operators
print("\n--- PART 3: Math Operators ---")
# Test all the operators: +, -, *, /, //, **, %

a = 17
b = 3

print(f"{a} + {b} = {a + b}") #Addition
print(f"{a} - {b} = {a - b}") #Subtraction
print(f"{a} * {b} = {a * b}") #Multiplication
print(f"{a} / {b} = {a / b}") #Division(float)
print(f"{a} // {b} = {a // b}") #Floor Division(int)
print(f"{a} ** {b} = {a ** b}") #Exponentiation
print(f"{a} % {b} = {a % b}") #Modulus

# PART 4: Operator Precedence
print("\n--- PART 4: Operator Precedence ---")
# Calculate: 9 + 6 / 3 * 2 - 1
result = 9 + 6 / 3 * 2 - 1
print(f"9 + 6 / 3 * 2 - 1 = {result}")