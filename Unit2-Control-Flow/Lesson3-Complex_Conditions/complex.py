# Three logical operators
# and (Both conditions must be True)
# or (At least one condition must be true)
# not (Flips True/False)

# Example - Game access control
# # Take user inputs - as integers
# player_level = int(input("Enter your player level:"))
# has_premium = bool(int(input("Do you have premium account?(0/1):")))
# is_banned = bool(int(input("Are you currently banned?(0/1):")))

# Take user inputs - as strings
player_level = int(input("Enter your player level:"))
has_premium = input("Do you have premium account?(yes/no):")
is_banned = input("Are you currently banned?(yes/no):")

# if statements to turn strings into booleans
if has_premium == "yes":
    has_premium = True
elif has_premium == 'no':
    has_premium = False
else:
    print("Invalid has_premium!")
    
if is_banned == "yes":
    is_banned = True
elif is_banned == 'no':
    is_banned = False
else:
    print("Invalid has_premium!")
#Access Control Logic
can_access_game = not is_banned and (player_level>=10 or has_premium)
can_access_premium_features = not is_banned and has_premium
can_join_tournaments = not is_banned and player_level >=25 and has_premium

# Print access details
print(f"Player Level: {player_level}")
print(f"Premium:{has_premium}")
print(f"Banned:{is_banned}")
print("*"*25)
print(f"Can Access Game:{can_access_game}")
print(f"Can Access Premium Features:{can_access_premium_features}")
print(f"Can Join Tournaments:{can_join_tournaments}")

# Logical Operator Precedence
#1 not(highest)
#2 and
#3 (lowest)

print(not False or False and True)