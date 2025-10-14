text = "Bergen Tech"
i = 0
result = ""
while i < len(text):
    char = text[i]
    if 'A' <= char <= 'Z':
        result += char
    i += 1
print(result)

# Age validator Example
age = -1
while age < 0 or age > 120:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid! Try again.")

print(f"Your age is {age}")