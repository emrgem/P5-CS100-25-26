# Lesson 3: String Basics - Simple Name Builder

# Part 1: Creating string variables
first_name = "Alex"
last_name = "Doe"
favorite_number = '5'
lucky_number = 0
gpa = 4.0

print(f"Type of favorite number {type(favorite_number)}")
print(f"Type of lucky number {type(lucky_number)}")
# Part 2: Combining strings
full_name = first_name + "-" + last_name # must be str + str
print(f"Full Name: {full_name}")
print(f"{first_name}'s GPA is {gpa-1}")
print(first_name + "'s " + "GPA is " + str(gpa)) 
# Part 3: String repetition
print("=" * 50)
cheer = ("Go " + first_name + "!") * 3
print(cheer)

# Part 4: String length
print(len(first_name))
print(f"Length of variable cheer: {len(cheer)}")

space = ""
print(len(space))
# Part 5: Indexing and Slicing
school = "Bergen Tech!"
print(school)
print(f"Length of school: {len(school)}")
print(school[0]) #first index
print(school[1])
print(school[2])

#negative indexing
print(school[-1]) # last character
print(school[-2])
# print(school[12])# error index out of range
print(school[11])# also last character
print(school[len(school)-1])# also last character

school = "Bergen Tech"
print(school[len(school)-1])
# Part 6: Creative combinations
