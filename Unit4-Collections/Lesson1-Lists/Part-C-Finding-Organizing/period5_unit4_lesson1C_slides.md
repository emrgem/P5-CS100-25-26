---
marp: true
theme: default
class: invert
paginate: true
backgroundColor: #1a1a2e
color: #eee
---

<style>
section {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 28px;
  padding: 20px 40px;
  line-height: 1.4;
}

section::after {
  font-size: 14px;
  color: #666;
}

h1 {
  color: #4fc3f7;
  text-align: center;
  border-bottom: 4px solid #4fc3f7;
  padding-bottom: 12px;
  font-size: 2.4em;
  margin: 10px 0 25px 0;
}

h2 {
  color: #81c784;
  border-left: 8px solid #81c784;
  padding-left: 18px;
  font-size: 2em;
  margin: 12px 0;
}

code {
  background: #2d2d44;
  padding: 4px 10px;
  border-radius: 6px;
  color: #ffb74d;
  font-size: 1em;
}

pre {
  background: #1e1e1e !important;
  border: 2px solid #4fc3f7;
  border-radius: 8px;
  padding: 20px 25px;
  margin: 15px 0;
}

pre code {
  background: transparent !important;
  color: #d4d4d4 !important;
  font-family: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
  font-size: 1.15em;
  line-height: 1.5;
}

.highlight {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 15px 25px;
  border-radius: 15px;
  margin: 15px 0;
  font-size: 1.6em;
  font-weight: bold;
  text-align: center;
}

.warning {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
  padding: 15px 25px;
  border-radius: 15px;
  margin: 15px 0;
  font-size: 1.5em;
  font-weight: bold;
  text-align: center;
}

.success {
  background: linear-gradient(135deg, #51cf66 0%, #40c057 100%);
  padding: 15px 25px;
  border-radius: 15px;
  margin: 15px 0;
  font-size: 1.4em;
  font-weight: bold;
  text-align: center;
}

.key-point {
  background: linear-gradient(135deg, #a78bfa 0%, #7e22ce 100%);
  padding: 18px 25px;
  border-radius: 15px;
  margin: 15px 0;
  color: #fff;
  font-size: 1.4em;
  font-weight: bold;
}

.big-idea {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  padding: 18px 25px;
  border-radius: 15px;
  margin: 15px 0;
  color: #fff;
  text-align: center;
  font-size: 1.6em;
  font-weight: bold;
}

.vocab-box {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  padding: 18px 25px;
  border-radius: 12px;
  margin: 15px 0;
  color: #000;
  font-size: 1.3em;
  font-weight: bold;
}

.step-box {
  background: #2d2d44;
  border-left: 5px solid #81c784;
  padding: 12px 18px;
  margin: 10px 0;
  border-radius: 8px;
  font-size: 1.4em;
}

.title-slide {
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 50vh;
}

.title-slide h1 {
  font-size: 2.8em;
  margin: 10px 0;
  color: #4fc3f7;
}

.subtitle {
  font-size: 1.6em;
  margin: 15px 0;
  font-weight: bold;
  color: #81c784;
}

.emoji-large {
  font-size: 4em;
  margin: 15px 0;
}

.two-column {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  align-items: start;
  margin: 15px 0;
}

.terminal-box {
  background: #0d0d0d;
  border: 2px solid #51cf66;
  border-radius: 10px;
  padding: 18px;
  margin: 10px 0;
  font-family: 'Cascadia Code', monospace;
  font-size: 1.2em;
  color: #51cf66;
}

.quiz-box {
  background: linear-gradient(135deg, #ffd93d 0%, #ff6b6b 100%);
  padding: 20px 25px;
  border-radius: 15px;
  margin: 15px 0;
  color: #000;
  font-size: 1.4em;
  font-weight: bold;
  text-align: center;
}

.overlay-dark {
  background: rgba(26, 26, 46, 0.95);
  padding: 30px;
  border-radius: 20px;
}
</style>

<!-- ==================== TITLE ==================== -->

<!-- Slide 1: Title -->
![bg](https://images.unsplash.com/photo-1493711662062-fa541f7f3d24?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🔍</div>

# Finding & Organizing

<div class="big-idea">
Unit 4 - Lesson 1C: List Search & Sort
</div>

<div class="subtitle">Find anything, organize everything! 📊</div>

</div>
</div>

<!-- Note: Today we're learning how to FIND items in lists and ORGANIZE them! These are super useful skills you'll use all the time. -->

---

<!-- ==================== REVIEW ==================== -->

<!-- Slide 2: Quick Review -->
## 🔄 Quick Review

<div class="quiz-box">
What methods do we know so far?
</div>

**Creating & Accessing:** `[]`, `list[index]`, `list[-1]`
**Adding:** `append()`, `insert()`, `extend()`
**Removing:** `remove()`, `pop()`
**Other:** `len()`, `for item in list`

<div class="success">
Today: FINDING items and ORGANIZING lists!
</div>

<!-- Note: Quick review! You know how to create lists, access items, add items, and remove items. Today we're adding finding and organizing to your toolkit! -->

---

<!-- ==================== INDEX ==================== -->

<!-- Slide 3: index() Header -->
![bg](https://images.unsplash.com/photo-1518770660439-4636190af475?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">📍</div>

# index() - Find the Position

<div class="subtitle">Where is it in the list?</div>

</div>
</div>

<!-- Note: First up: finding WHERE something is in a list! -->

---

<!-- Slide 4: The Problem -->
## 🤔 The Problem

**You're scrolling through TikTok and want to find a specific video:**

```python
tiktok_feed = ["dance", "cooking", "prank", "gaming", "cats", "comedy"]

# WHERE is the gaming video?
# We need its INDEX to interact with it!
```

<div class="quiz-box">
How do we find what position "gaming" is at?
</div>

<!-- Note: Imagine your TikTok feed. You know "gaming" is in there somewhere. But WHERE? What INDEX is it at? -->

---

<!-- Slide 5: The Solution - index() -->
## 📍 index() - Find the Position!

```python
tiktok_feed = ["dance", "cooking", "prank", "gaming", "cats", "comedy"]

position = tiktok_feed.index("gaming")
print(position)
```

<div class="terminal-box">
3
</div>

<div class="vocab-box">
index(value) - Returns the INDEX of the first occurrence
</div>

<!-- Note: The index() method finds WHERE something is! "gaming" is at index 3. Remember: counting starts at 0! -->

---

<!-- Slide 6: index() Returns Position -->
## 📍 What index() Returns

```python
movies = ["Avengers", "Spider-Man", "Black Panther", "Thor"]
#           0            1              2              3

pos = movies.index("Black Panther")
print(f"Black Panther is at position {pos}")
```

<div class="terminal-box">
Black Panther is at position 2
</div>

<div class="key-point">
index() tells you WHERE something is, not IF it exists!
</div>

<!-- Note: index() gives you the position number. Now you can use that position to do things with that item! -->

---

<!-- Slide 7: Using the Index -->
## 🎯 Using the Index

```python
leaderboard = ["xXGamerXx", "ProPlayer99", "NoobMaster", "ShadowNinja"]

# Find where NoobMaster is ranked
position = leaderboard.index("NoobMaster")
rank = position + 1  # Convert 0-based index to 1-based rank

print(f"NoobMaster is ranked #{rank}")
```

<div class="terminal-box">
NoobMaster is ranked #3
</div>

<div class="success">
Find position → Use it for calculations or display!
</div>

<!-- Note: Once you have the index, you can do things with it! Here we convert the 0-based index to a human-friendly rank number. -->

---

<!-- Slide 8: The Danger! -->
## ⚠️ What Could Go Wrong?

```python
snacks = ["chips", "cookies", "candy"]

position = snacks.index("pizza")  # NOT in the list!
```

<div class="quiz-box">
What happens?
</div>

<!-- Note: Uh oh! What if we search for something that doesn't exist? -->

---

<!-- Slide 9: ValueError Crash -->
## ❌ ValueError - Not Found!

```python
snacks = ["chips", "cookies", "candy"]
position = snacks.index("pizza")
```

<div class="terminal-box">
ValueError: 'pizza' is not in list
</div>

<div class="warning">
index() CRASHES if the item isn't found!
</div>

<!-- Note: CRASH! ValueError. Just like remove(), index() crashes if it can't find what you're looking for. We need to handle this! -->

---

<!-- Slide 10: Safe Approach 1 - Defensive -->
## ✅ Approach 1: Check First (Defensive)

```python
playlist = ["Believer", "Thunder", "Radioactive"]
song_to_find = "Thunder"

if song_to_find in playlist:
    position = playlist.index(song_to_find)
    print(f"'{song_to_find}' is at position {position}")
else:
    print(f"'{song_to_find}' not found!")
```

<div class="terminal-box">
'Thunder' is at position 1
</div>

<div class="key-point">
Check with "in" BEFORE calling index()!
</div>

<!-- Note: Defensive approach: check if it exists FIRST using "in", then call index(). Same pattern we learned before! -->

---

<!-- Slide 11: Safe Approach 2 - Exception -->
## ✅ Approach 2: try/except (Exception Handling)

```python
playlist = ["Believer", "Thunder", "Radioactive"]
song_to_find = "Despacito"

try:
    position = playlist.index(song_to_find)
    print(f"'{song_to_find}' is at position {position}")
except ValueError:
    print(f"'{song_to_find}' not found!")
```

<div class="terminal-box">
'Despacito' not found!
</div>

<div class="key-point">
Catch ValueError when item doesn't exist!
</div>

<!-- Note: Exception handling approach: try to find it, catch the ValueError if it fails. Both approaches work! -->

---

<!-- Slide 12: First Occurrence Only -->
## ⚠️ Important: First Occurrence Only!

```python
reactions = ["😂", "❤️", "😂", "🔥", "😂", "👍"]
#             0     1     2     3     4     5

position = reactions.index("😂")
print(position)
```

<div class="terminal-box">
0
</div>

<div class="warning">
index() returns the FIRST match only!
</div>

"😂" appears at indices 0, 2, and 4... but index() only returns 0!

<!-- Note: Important! index() only finds the FIRST occurrence. If you have duplicates, it returns the first one's position. -->

---

<!-- ==================== COUNT ==================== -->

<!-- Slide 13: count() Header -->
![bg](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🔢</div>

# count() - How Many?

<div class="subtitle">Count occurrences in your list!</div>

</div>
</div>

<!-- Note: Next method: counting how many times something appears! -->

---

<!-- Slide 14: The count() Method -->
## 🔢 count() - Count Occurrences

```python
instagram_likes = ["❤️", "❤️", "👍", "❤️", "🔥", "❤️", "👍"]

heart_count = instagram_likes.count("❤️")
print(f"Hearts: {heart_count}")

fire_count = instagram_likes.count("🔥")
print(f"Fires: {fire_count}")
```

<div class="terminal-box">
Hearts: 4
Fires: 1
</div>

<div class="vocab-box">
count(value) - Returns how many times value appears
</div>

<!-- Note: count() tells you HOW MANY times something appears. 4 hearts, 1 fire emoji. Simple! -->

---

<!-- Slide 15: count() is ALWAYS Safe! -->
## 🎉 count() is ALWAYS Safe!

```python
menu = ["burger", "pizza", "taco", "pizza", "sushi"]

# Count something that EXISTS
pizza_count = menu.count("pizza")
print(f"Pizzas: {pizza_count}")  # 2

# Count something that DOESN'T exist
hotdog_count = menu.count("hotdog")
print(f"Hotdogs: {hotdog_count}")  # 0
```

<div class="terminal-box">
Pizzas: 2
Hotdogs: 0
</div>

<div class="success">
No crash! Returns 0 if not found! 🎉
</div>

<!-- Note: GREAT NEWS! count() is ALWAYS SAFE! If the item doesn't exist, it just returns 0. No ValueError, no crash! -->

---

<!-- Slide 16: count() vs index() -->
## 🆚 count() vs index()

<div class="two-column">

<div>

### index()
```python
# Can CRASH! ⚠️
pos = list.index("x")
```
- Returns **position**
- **Crashes** if not found
- Needs safe handling!

</div>

<div>

### count()
```python
# Always safe! ✅
num = list.count("x")
```
- Returns **quantity**
- Returns **0** if not found
- No error handling needed!

</div>

</div>

<div class="highlight">
count() = safe, index() = needs protection!
</div>

<!-- Note: Key difference! count() is always safe. index() can crash. Remember this when choosing which to use! -->

---

<!-- Slide 17: Practical Use of count() -->
## 🎮 Practical Example: Vote Counter

```python
votes = ["Mario", "Luigi", "Mario", "Peach", "Mario", "Luigi"]

mario_votes = votes.count("Mario")
luigi_votes = votes.count("Luigi")
peach_votes = votes.count("Peach")

print(f"🍄 Mario: {mario_votes} votes")
print(f"💚 Luigi: {luigi_votes} votes")
print(f"👑 Peach: {peach_votes} votes")
```

<div class="terminal-box">
🍄 Mario: 3 votes
💚 Luigi: 2 votes
👑 Peach: 1 votes
</div>

<!-- Note: count() is perfect for vote counting, survey results, tracking duplicates, and more! -->

---

<!-- ==================== SORT ==================== -->

<!-- Slide 18: Sorting Header -->
![bg](https://images.unsplash.com/photo-1507925921958-8a62f3d1a50d?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">📊</div>

# Sorting Lists

<div class="subtitle">Organize your data!</div>

</div>
</div>

<!-- Note: Now let's learn how to ORGANIZE lists - putting things in order! -->

---

<!-- Slide 19: Why Sort? -->
## 🤔 Why Sort?

**Imagine searching through an unsorted contacts list:**

```python
contacts = ["Zoe", "Alex", "Maya", "Ben", "Tyler", "Kai"]
# Where's Maya? 🤷 Have to check every single name!
```

**Now imagine it sorted:**

```python
contacts = ["Alex", "Ben", "Kai", "Maya", "Tyler", "Zoe"]
# Much easier to find Maya! ✨
```

<div class="key-point">
Sorted data is easier to search and display!
</div>

<!-- Note: Sorting makes everything easier! Finding things, displaying rankings, showing alphabetical lists... -->

---

<!-- Slide 20: sort() Method -->
## 📊 sort() - Sort in Place

```python
high_scores = [750, 920, 480, 1100, 650]
print(f"Before: {high_scores}")

high_scores.sort()
print(f"After:  {high_scores}")
```

<div class="terminal-box">
Before: [750, 920, 480, 1100, 650]
After:  [480, 650, 750, 920, 1100]
</div>

<div class="vocab-box">
sort() - Sorts the list IN PLACE (modifies the original!)
</div>

<!-- Note: sort() organizes your list from smallest to largest (or A to Z for strings). The original list CHANGES! -->

---

<!-- Slide 21: sort() Changes Original -->
## ⚠️ sort() MODIFIES the Original!

```python
streamers = ["Ninja", "Pokimane", "xQc", "Shroud"]
print(f"Original: {streamers}")

streamers.sort()
print(f"Sorted:   {streamers}")
print(f"Original is now: {streamers}")  # Changed!
```

<div class="terminal-box">
Original: ['Ninja', 'Pokimane', 'xQc', 'Shroud']
Sorted:   ['Ninja', 'Pokimane', 'Shroud', 'xQc']
Original is now: ['Ninja', 'Pokimane', 'Shroud', 'xQc']
</div>

<div class="warning">
The original list is CHANGED forever!
</div>

<!-- Note: IMPORTANT! sort() changes the original list. The original order is GONE. What if you needed it? -->

---

<!-- Slide 22: sort() Reverse -->
## 🔄 sort() in Reverse Order

```python
scores = [480, 650, 750, 920, 1100]
scores.sort(reverse=True)  # Highest first!
print(scores)
```

<div class="terminal-box">
[1100, 920, 750, 650, 480]
</div>

<div class="key-point">
reverse=True sorts from HIGHEST to LOWEST!
</div>

**Perfect for:**
- Leaderboards (highest score first)
- Top 10 lists
- Rankings

<!-- Note: Add reverse=True to sort biggest first! Great for leaderboards and rankings. -->

---

<!-- Slide 23: sorted() Header -->
![bg](https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">✨</div>

# sorted() - The Safe Way

<div class="subtitle">Sort WITHOUT changing the original!</div>

</div>
</div>

<!-- Note: What if you need to keep the original? Enter sorted()! -->

---

<!-- Slide 24: sorted() Function -->
## ✨ sorted() - Creates a NEW Sorted List

```python
original_queue = ["Charlie", "Alice", "Bob", "Diana"]
print(f"Original: {original_queue}")

alphabetical = sorted(original_queue)
print(f"Sorted:   {alphabetical}")
print(f"Original still: {original_queue}")  # Unchanged!
```

<div class="terminal-box">
Original: ['Charlie', 'Alice', 'Bob', 'Diana']
Sorted:   ['Alice', 'Bob', 'Charlie', 'Diana']
Original still: ['Charlie', 'Alice', 'Bob', 'Diana']
</div>

<div class="success">
Original list stays the same! ✨
</div>

<!-- Note: sorted() creates a NEW list that's sorted, leaving the original alone. Much safer! -->

---

<!-- Slide 25: sort() vs sorted() -->
## 🆚 sort() vs sorted()

<div class="two-column">

<div>

### sort() - Method
```python
my_list.sort()
```
- **Modifies** original ⚠️
- Returns `None`
- Call ON the list

</div>

<div>

### sorted() - Function
```python
new_list = sorted(my_list)
```
- **Keeps** original safe ✅
- Returns new sorted list
- Pass list TO it

</div>

</div>

<div class="highlight">
sorted() is usually safer! Use sort() only when you don't need the original.
</div>

<!-- Note: Key differences! sort() changes original, sorted() makes a new list. Most of the time, sorted() is the safer choice. -->

---

<!-- Slide 26: sorted() Also Has Reverse -->
## 🔄 sorted() with reverse=True

```python
kill_counts = [15, 8, 22, 11, 19]

# Get top scores without changing original
leaderboard = sorted(kill_counts, reverse=True)

print(f"Original data: {kill_counts}")
print(f"Leaderboard:   {leaderboard}")
```

<div class="terminal-box">
Original data: [15, 8, 22, 11, 19]
Leaderboard:   [22, 19, 15, 11, 8]
</div>

<div class="key-point">
sorted(list, reverse=True) = sorted copy, highest first!
</div>

<!-- Note: sorted() also supports reverse=True! Get a sorted copy with highest first, while keeping original data safe. -->

---

<!-- Slide 27: Practical Example -->
## 🎮 Real Example: Game Leaderboard

```python
# Original order (order they joined)
players = ["Tyler", "Alex", "Sam", "Jordan"]
scores = [1500, 2200, 1800, 950]

# Display alphabetically for directory
print(f"Players A-Z: {sorted(players)}")

# Display scores highest first for leaderboard
print(f"Top Scores: {sorted(scores, reverse=True)}")

# Originals unchanged for other uses!
print(f"Join order: {players}")
```

<div class="terminal-box">
Players A-Z: ['Alex', 'Jordan', 'Sam', 'Tyler']
Top Scores: [2200, 1800, 1500, 950]
Join order: ['Tyler', 'Alex', 'Sam', 'Jordan']
</div>

<!-- Note: Real world use! sorted() lets you show data different ways without losing the original order. -->

---

<!-- ==================== SUMMARY ==================== -->

<!-- Slide 28: Summary -->
## 📚 What You Learned Today

<div class="step-box">
<strong>index(value)</strong> - Find position (⚠️ needs safe handling!)
</div>

<div class="step-box">
<strong>count(value)</strong> - Count occurrences (✅ always safe!)
</div>

<div class="step-box">
<strong>sort()</strong> - Sort in place (⚠️ changes original!)
</div>

<div class="step-box">
<strong>sorted()</strong> - Return sorted copy (✅ keeps original!)
</div>

<!-- Note: Four new tools! index and count for finding, sort and sorted for organizing. Remember which ones are safe and which need protection! -->

---

<!-- Slide 29: Safety Cheat Sheet -->
## 🛡️ Safety Cheat Sheet

| Method | Safe? | What to Do |
|--------|-------|------------|
| `index()` | ⚠️ NO | Check with `in` first OR try/except |
| `count()` | ✅ YES | Just use it! Returns 0 if not found |
| `sort()` | ⚠️ | Changes original - make copy first if needed |
| `sorted()` | ✅ | Creates new list - original stays safe |

<div class="highlight">
When in doubt, use count() and sorted()!
</div>

<!-- Note: Quick reference! Bookmark this slide. Green = safe, yellow = careful! -->

---

<!-- Slide 30: Two Approaches Reminder -->
## 🎯 Safe index() - Two Ways

<div class="two-column">

<div>

### Defensive
```python
if item in my_list:
    pos = my_list.index(item)
    print(f"At position {pos}")
else:
    print("Not found")
```

</div>

<div>

### Exception Handling
```python
try:
    pos = my_list.index(item)
    print(f"At position {pos}")
except ValueError:
    print("Not found")
```

</div>

</div>

<div class="success">
Both approaches work! Choose your style!
</div>

<!-- Note: Same two approaches we learned before! Defensive or exception handling - both are valid and professional. -->

---

<!-- Slide 31: Practice Preview -->
## 💻 Practice Problems

<div class="step-box">
<strong>Problem 1:</strong> Safe Search (Defensive) - Find position using "in" check
</div>

<div class="step-box">
<strong>Problem 2:</strong> Safe Search (Exception) - Find position using try/except
</div>

<div class="step-box">
<strong>Problem 3:</strong> Duplicate Counter - Use count() to find duplicates
</div>

<div class="step-box">
<strong>Problem 4:</strong> Safe Sorter - Use sorted() to not modify original
</div>

<!-- Note: Your practice problems! You'll implement both safe search approaches, use count(), and practice sorted(). -->

---

<!-- Slide 32: Coming Up Next -->
## 🔮 Coming Up: Lesson 1D

<div class="big-idea">
References vs Copies - THE GOTCHA! 😱
</div>

**You'll learn:**
- Why `backup = original` is NOT a copy!
- How to make REAL copies of lists
- Avoiding the most common list bug!

<div class="warning">
This trips up EVERYONE the first time!
</div>

<!-- Note: Next time: the biggest gotcha in Python lists! Why copying isn't what you think it is. Don't miss it! -->

---

<!-- Slide 33: You Did It -->
![bg](https://images.unsplash.com/photo-1492619375914-88005aa9e8fb?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🎉</div>

# Great Work!

<div class="success">
You can now FIND and ORGANIZE list data!
</div>

<div class="highlight">
Unit 4 - Lesson 1C Complete!
</div>

</div>
</div>

<!-- Note: Excellent work! You now know how to find items with index() and count(), and organize with sort() and sorted(). Practice these and get ready for the big gotcha next time! -->
