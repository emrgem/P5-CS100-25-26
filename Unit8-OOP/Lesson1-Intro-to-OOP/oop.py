"""
Unit 8 - Lesson 1: Why OOP? Classes & Objects - STARTER FILE
=============================================================
From Procedural to Object-Oriented Programming
"""

# =============================================================================
# PART 1: THE PROCEDURAL WAY (Run this first!)
# =============================================================================
# This is a working social media program using dictionaries and functions.
# Run it. It works! But notice what's annoying about it...

def create_profile(username, display_name, bio):
    """Create a profile as a dictionary"""
    return {
        "username": username,
        "display_name": display_name,
        "bio": bio,
        "followers": 0,
        "posts": []
    }

def add_post(profile, text):
    """Add a post to a profile's post list"""
    profile["posts"].append(text)

def gain_follower(profile):
    """Increase a profile's follower count by 1"""
    profile["followers"] += 1

def display_profile(profile):
    """Print a profile's info"""
    print(f"@{profile['username']} ({profile['display_name']})")
    print(f"  Bio: {profile['bio']}")
    print(f"  Followers: {profile['followers']}")
    print(f"  Posts: {len(profile['posts'])}")
    print()

# --- Create some profiles and use them ---
maria = create_profile("code_queen", "Maria", "Python enthusiast")
jake = create_profile("jake_codes", "Jake", "JS convert")

add_post(maria, "Hello world!")
add_post(maria, "Learning OOP today!")
gain_follower(maria)
gain_follower(maria)
gain_follower(maria)

add_post(jake, "Just joined!")

display_profile(maria)
display_profile(jake)

# 🤔 THINK ABOUT:
# 1. What stops you from making a typo in the dictionary keys?
# 2. Where do the functions "live"? Do they belong to any specific profile?
# 3. What if you accidentally called add_post(maria, jake)?  No error!
#    The function doesn't know or care what kind of dict it gets.


# =============================================================================
# PART 2: CONVERT TO OOP
# =============================================================================

# Step 1: Define the Profile class with __init__
class Profile:
    def __init__(self, username, display_name, bio): # constructor method/initializes the object
        self.username = username
        self.display_name = display_name
        self.bio = bio
        self.followers = 0
        self.posts = []
    
# Step 2: Create objects (replaces calling create_profile)
maria = Profile("code_queen", "Maria", "Python Enthusiast!")
jake = Profile("jake_codes", "Jake", "JS Convert")


# Step 3: Access and print attributes
# Use dot notation instead of dictionary bracket notation!
print(maria.username)
print(jake.username)
print(jake.followers)


# Step 4: Prove objects are independent
maria.followers = 500
print(f"Maria: {maria.followers}")
print(f"Jake: {jake.followers}")


# =============================================================================
# PART 3: COMPARE — SAME DATA, TWO WAYS
# =============================================================================
# Look at the two approaches side by side:
#
# PROCEDURAL:
maria = create_profile("code_queen", "Maria", "Python enthusiast")
print(maria["username"])        # bracket notation
add_post(maria, "Hello!")       # function(data)
#
# OOP:
maria = Profile("code_queen", "Maria", "Python enthusiast")
print(maria.username)           # dot notation
# maria.add_post("Hello!")      # Coming in Lesson 2! object.method()
#



# =============================================================================
# PART 4: YOUR TURN — Post Class
# =============================================================================
# Now create a Post class on your own (no procedural version to convert)!
#
# Required parameters: author (string), text (string)
# Default attributes:  likes (starts at 0), comments (starts as empty list)

# ✏️ YOUR CODE HERE:
class Post:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.likes = 0
        self.comments = []



# Test it when you're done:
p1 = Post("maria", "Hello world!")
p2 = Post("jake", "OOP is cool")
print(p1.author)      # maria
print(p2.text)        # OOP is cool
print(p1.likes)       # 0
print(p1.comments)    # []




