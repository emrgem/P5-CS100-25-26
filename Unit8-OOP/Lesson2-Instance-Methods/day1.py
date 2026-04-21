"""=============================================
 UNIT 8 - LESSON 2 - DAY 1: MODIFIER METHODS
================================================
TODAY'S GOAL:
  Add three methods to the Profile class that CHANGE its data:
    1. add_post(self, text)         — appends to self.posts
    2. gain_follower(self)          — adds 1 to self.followers
    3. follow(self, other_username) — appends to self.following
=============================================== """

class Profile:
    def __init__(self, username, display_name, bio):
        self.username = username
        self.display_name = display_name
        self.bio = bio
        self.followers = 0
        self.posts = []
        self.following = []

    # ---------------------------
    # TODO 1: Write add_post(self, text)
    # It should append `text` to self.posts
    # ---------------------------

    def add_post(self, text):
        self.posts.append(text)


    # ---------------------------
    # TODO 2: Write gain_follower(self)
    # It should add 1 to self.followers
    # ---------------------------
    def gain_follower(self):
        self.followers += 1
    


    # ---------------------------
    # TODO 3: Write follow(self, other_username)
    # It should append other_username to self.following
    # ---------------------------

    # YOUR CODE HERE


# ==================================
# -------------TESTS ---------------
# ==================================

# Create a maria profile
maria = Profile("code_queen", "Maria", "Python Enthusiast!")
maria.add_post("Hello BT!")
maria.add_post("Learning OOP!")

print(f"Posts: {maria.posts}")
