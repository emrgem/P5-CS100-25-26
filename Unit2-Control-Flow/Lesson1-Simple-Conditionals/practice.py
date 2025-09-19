# First Way
height = int(input("Enter your height in inches: "))
print(f"Your height: {height} inches")

if height >= 72:
    print("You are tall!")

if height < 72 and height >= 60:
    print("You are average height!")

if height < 60:
    print("You are short!")
    
#second way
height = int(input("Enter your height in inches: "))
print(f"Your height: {height} inches")

if height >= 72:
    print("You are tall!")
else:
    if height >= 60:
        print("You are average heigt!")
    else:
        print("You are short!")