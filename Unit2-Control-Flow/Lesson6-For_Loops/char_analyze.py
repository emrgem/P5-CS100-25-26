text = input("Enter the text:")
#Count vowels
vowel_count = 0
vowels = "aeiouAEIOU"
unique = ''
for char in text:
    if char in vowels:
        if char not in unique:
            unique += char
            vowel_count += 1
print(f"Vowels found: {vowel_count}")

# Check capital letters
capitals = ""
for char in text:
    if 'A' <= char <= 'Z':
        capitals += char # capitals = capitals + char

if capitals:
    print(f"Capital Letters:{capitals}")
else:
    print("No capitals found!")