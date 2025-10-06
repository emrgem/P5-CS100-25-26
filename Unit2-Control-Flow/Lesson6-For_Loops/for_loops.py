# Lesson 5: For Loops 

# PART 1: QUICK PRACTICE - Username Loop
# =====================================
# Write a for loop to print each character in this username

username = "gamer2024"

username[0] #g
username[1] #a
username[-1]#4 last one
#username[len(username)] #Error index out of range
username[len(username)-1] #last character

# Your for loop here
'''
g
a
m
e..
'''
# go through the characters
for letter in username:
    print(letter)

range(5) # 0-5 (0,1,2,3,4)
range(2,5) # 2-5 (2,3,4) 
range(5,50,5) #5-50 (5,10,15,...45)
range(10,2,-2) #10-2 (10,8,6,4)

for i in range(len(username)):
    print(username[i])

# PART 2: CODE ALONG - Username Validator
# =====================================
# Build a username validator that checks:
# - Has at least one number
# - Has at least one uppercase letter
# - Count total characters

username = "CoolGamer123"
char = ''
# Upper case letter check
'A' <= char <= 'Z'
# lower case letter check
'a' <= char <= 'z'
# digit check
'0' <= char <= '9'

# Your code here
username = input("Enter your username:")
has_number = False
has_uppercase = False
total_chars = len(username)

for char in username:
    if 'A' <= char <= 'Z':
        has_uppercase = True
    if '0' <= char <= '9':
        has_number = True
        
print(f"Username: {username}")
print(f"Total characters: {total_chars}")
print(f"Has number: {has_number}")
print(f"Has uppercase: {has_uppercase}")




# PART 3: QUICK PRACTICE - Counting 'e'
# =====================================
# Count how many times the letter 'e' appears (case-insensitive)

tweet = "Hello everyone! Hope you're having a great day!"

e_count = 0
# Your loop here


# PART 4: CODE ALONG - Message Repeater
# =====================================
# Build a message repeater with countdown:
# - Print a message multiple times
# - Add a countdown before each message
# Example: "3... Study hard!"

message = "Study hard!"
times = 5

# Your code here


# PART 5: YOUR TURN - Text Message Analyzer
# ========================================
# - Total characters (use len())
# - Number of spaces
# - Number of letters
# - Number of punctuation marks (! ? . ,)

text = "Hey! How are you doing today? :)"

# Your analysis code here


# PART 6: PATTERN CHALLENGE
# ============================================================================

# Challenge A: Print squares of numbers 1-5 (1, 4, 9, 16, 25)


# Challenge B: Print countdown from 10 to 1


# Challenge C: Print every 3rd number from 0 to 15 (0, 3, 6, 9, 12, 15)

