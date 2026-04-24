"""
=================================================
 UNIT 8 - LESSON 2 - DAY 2: GETTER METHODS
=================================================
TODAY'S GOAL:
  Add three more methods to the Profile class:
    1. post_count(self)         — RETURNS the number of posts
    2. is_popular(self)         — RETURNS True if followers > 100
    3. post_and_gain(self, text) — calls add_post AND gain_follower
"""


class Profile:
    def __init__(self, username, display_name, bio):
        self.username = username
        self.display_name = display_name
        self.bio = bio
        self.followers = 0
        self.posts = []
        self.following = []

    # ---- Day 1 methods (already done) ----

    def add_post(self, text):
        self.posts.append(text)

    def gain_follower(self):
        self.followers += 1

    def follow(self, other_username):
        self.following.append(other_username)

    # -----------------------------------
    # TODO 1: Write post_count(self)
    # It should RETURN the number of posts (hint: use len())
    # ------------------------------------
    def post_count(self):
        return len(self.posts)
    


    # ------------------------------------
    # TODO 2: Write is_popular(self)
    # It should RETURN True if self.followers > 100, otherwise False
    # -------------------------------------
    def is_popular(self):
        return self.followers > 100


    # --------------------------------------
    # TODO 3: Write post_and_gain(self, text)
    # It should:
    #   1. Call self.add_post(text)
    #   2. Call self.gain_follower()
    # ---------------------------------------
    def post_and_gain(self, text):
        self.add_post(text)
        self.gain_follower()


# ===========================================
# ------------------TESTS ------------------ 
# ===========================================

print("Creating Maria's profile...")
maria = Profile("code_queen", "Maria", "Python enthusiast")
print()

# # ---- TEST 1: post_count ----
print(f"Testing post_count")
maria.add_post("Post 1")
maria.add_post("Post 2")
maria.add_post("Post 3")
print(f" Post Count: {maria.post_count()}")
maria.add_post("Post 4")
maria.add_post("Post 5")
print(f" Post Count: {maria.post_count()}")
# # ---- TEST 2: is_popular ----
print("Testing is_popular()")
print(f" Popular with {maria.followers} followers? {maria.is_popular()}")

for _ in range(200):
    maria.gain_follower()

print(f" Popular with {maria.followers} followers? {maria.is_popular()}")


# # ---- TEST 3: post_and_gain ----
print("Testing post_and_gain")
jake = Profile("jake_codes", "Jake", "JS Convert")
jake.post_and_gain("My First Post")
jake.post_and_gain("Another one")
print(f"Posts: {jake.posts}")
print(f"Followers: {jake.followers}")