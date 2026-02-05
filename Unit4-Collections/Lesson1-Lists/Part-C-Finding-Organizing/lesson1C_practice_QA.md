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

.answer-box {
  background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
  padding: 20px 25px;
  border-radius: 15px;
  margin: 15px 0;
  color: #000;
  font-size: 1.3em;
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

![bg](https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🎯</div>

# Lesson 1C Practice Q&A

<div class="big-idea">
Finding & Organizing Lists
</div>

<div class="subtitle">index() • count() • sort() • sorted()</div>

</div>
</div>

<!-- Note: Let's practice finding and organizing! Fun examples ahead! -->

---

<!-- ==================== SECTION: INDEX ==================== -->

![bg](https://images.unsplash.com/photo-1518770660439-4636190af475?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">📍</div>

# Part 1: index()

<div class="subtitle">Find the position!</div>

</div>
</div>

---

## ❓ Q1: Basic index()

```python
netflix_shows = ["Squid Game", "Wednesday", "Stranger Things", "The Crown"]
position = netflix_shows.index("Wednesday")
print(position)
```

<div class="quiz-box">
What number prints?
</div>

**A)** 0
**B)** 1
**C)** 2
**D)** "Wednesday"

---

## ✅ A1: Position 1!

<div class="terminal-box">
1
</div>

<div class="answer-box">
"Wednesday" is at index 1 (second item, but we count from 0!)
</div>

```
Index:      0             1           2                 3
         "Squid Game"  "Wednesday"  "Stranger Things"  "The Crown"
```

---

## ❓ Q2: What's the Output?

```python
emojis = ["🎮", "🎵", "🎬", "📱", "🎮", "🎵"]
pos = emojis.index("🎮")
print(pos)
```

<div class="quiz-box">
🎮 appears twice! What does index() return?
</div>

---

## ✅ A2: First One Only!

<div class="terminal-box">
0
</div>

<div class="answer-box">
index() returns the FIRST occurrence only!
</div>

```python
# 🎮 is at index 0 AND index 4
# But index() only returns 0 (the first one)
```

---

## ❓ Q3: What Happens Here?

```python
fast_food = ["McDonalds", "Wendys", "Taco Bell"]
position = fast_food.index("Chipotle")
print(position)
```

<div class="quiz-box">
Crash or success?
</div>

---

## ✅ A3: ValueError CRASH! 💥

<div class="terminal-box">
ValueError: 'Chipotle' is not in list
</div>

<div class="warning">
index() crashes if item doesn't exist!
</div>

This is why we need safe approaches!

---

## ❓ Q4: Fix This Code (Defensive)

```python
def find_song_position(playlist, song):
    """Find song position safely using defensive check."""
    # Fix this to not crash!
    position = playlist.index(song)
    return position
```

<div class="quiz-box">
Add a check BEFORE calling index()!
</div>

---

## ✅ A4: Defensive Solution

```python
def find_song_position(playlist, song):
    """Find song position safely using defensive check."""
    if song in playlist:
        position = playlist.index(song)
        return position
    return -1  # Not found indicator
```

<div class="answer-box">
Check with "in" BEFORE calling index()!
</div>

---

## ❓ Q5: Fix This Code (Exception)

```python
def find_song_position_v2(playlist, song):
    """Find song position safely using try/except."""
    # Fix this using exception handling!
    position = playlist.index(song)
    return position
```

<div class="quiz-box">
Use try/except to catch the error!
</div>

---

## ✅ A5: Exception Solution

```python
def find_song_position_v2(playlist, song):
    """Find song position safely using try/except."""
    try:
        position = playlist.index(song)
        return position
    except ValueError:
        return -1  # Not found indicator
```

<div class="answer-box">
Catch ValueError when item doesn't exist!
</div>

---

## ❓ Q6: Test Both Solutions

```python
playlist = ["Flowers", "Anti-Hero", "Unholy", "As It Was"]

# Test 1: Find existing song
result1 = find_song_position(playlist, "Unholy")

# Test 2: Find non-existing song
result2 = find_song_position(playlist, "Despacito")
```

<div class="quiz-box">
What are result1 and result2?
</div>

---

## ✅ A6: Results

<div class="terminal-box">
result1 = 2
result2 = -1
</div>

<div class="answer-box">
"Unholy" found at index 2, "Despacito" not found → -1
</div>

---

<!-- ==================== SECTION: COUNT ==================== -->

![bg](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🔢</div>

# Part 2: count()

<div class="subtitle">How many are there?</div>

</div>
</div>

---

## ❓ Q7: Basic count()

```python
twitch_emotes = ["Kappa", "PogChamp", "Kappa", "LUL", "Kappa", "PogChamp"]
kappa_count = twitch_emotes.count("Kappa")
print(kappa_count)
```

<div class="quiz-box">
How many "Kappa" emotes?
</div>

---

## ✅ A7: Three!

<div class="terminal-box">
3
</div>

<div class="answer-box">
count() counts ALL occurrences, not just the first!
</div>

---

## ❓ Q8: What About This?

```python
pizza_toppings = ["pepperoni", "cheese", "mushrooms", "olives"]
pineapple_count = pizza_toppings.count("pineapple")
print(pineapple_count)
```

<div class="quiz-box">
"pineapple" doesn't exist. Crash or...?
</div>

---

## ✅ A8: Zero - No Crash! 🎉

<div class="terminal-box">
0
</div>

<div class="success">
count() is ALWAYS SAFE! Returns 0 if not found!
</div>

No try/except needed! No `if in` check needed!

---

## ❓ Q9: count() vs index()

**Which is safer to use without error handling?**

```python
my_list = ["a", "b", "c"]

# Option A
result_a = my_list.index("z")

# Option B  
result_b = my_list.count("z")
```

<div class="quiz-box">
Which one won't crash?
</div>

---

## ✅ A9: count() is Safe!

<div class="two-column">

<div>

### index("z") ⚠️
```
ValueError: 'z' is not in list
```
**CRASH!**

</div>

<div>

### count("z") ✅
```
0
```
**No crash!**

</div>

</div>

<div class="answer-box">
count() returns 0 for missing items, index() crashes!
</div>

---

## ❓ Q10: Practical Application

**Count votes in a Discord poll:**

```python
def count_votes(votes, option):
    """Return how many times option was voted for."""
    # Your code here
    pass

# Test
poll = ["Yes", "No", "Yes", "Yes", "Maybe", "No", "Yes"]
yes_votes = count_votes(poll, "Yes")
# Should return 4
```

<div class="quiz-box">
How simple is this function?
</div>

---

## ✅ A10: One Line!

```python
def count_votes(votes, option):
    """Return how many times option was voted for."""
    return votes.count(option)

# Test
poll = ["Yes", "No", "Yes", "Yes", "Maybe", "No", "Yes"]
yes_votes = count_votes(poll, "Yes")
print(yes_votes)  # 4
```

<div class="answer-box">
count() is so safe, the function is just one line!
</div>

---

<!-- ==================== SECTION: SORT ==================== -->

![bg](https://images.unsplash.com/photo-1507925921958-8a62f3d1a50d?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">📊</div>

# Part 3: sort() & sorted()

<div class="subtitle">Organize your data!</div>

</div>
</div>

---

## ❓ Q11: sort() Output

```python
scores = [85, 92, 78, 95, 88]
scores.sort()
print(scores)
```

<div class="quiz-box">
What's the order after sort()?
</div>

---

## ✅ A11: Low to High!

<div class="terminal-box">
[78, 85, 88, 92, 95]
</div>

<div class="answer-box">
sort() arranges numbers from lowest to highest!
</div>

---

## ❓ Q12: sort() Returns What?

```python
games = ["Zelda", "Mario", "Pokemon", "Kirby"]
result = games.sort()
print(result)
```

<div class="quiz-box">
What does result contain?
</div>

**A)** `["Kirby", "Mario", "Pokemon", "Zelda"]`
**B)** `["Zelda", "Mario", "Pokemon", "Kirby"]`
**C)** `None`
**D)** An error

---

## ✅ A12: None! 😱

<div class="terminal-box">
None
</div>

<div class="warning">
sort() returns None! It modifies the list IN PLACE!
</div>

```python
# The list IS sorted, but sort() doesn't return it
print(games)  # ['Kirby', 'Mario', 'Pokemon', 'Zelda']
```

---

## ❓ Q13: Reverse Sort

```python
fortnite_kills = [5, 12, 3, 8, 15, 7]
fortnite_kills.sort(reverse=True)
print(fortnite_kills)
```

<div class="quiz-box">
What's the order with reverse=True?
</div>

---

## ✅ A13: Highest First!

<div class="terminal-box">
[15, 12, 8, 7, 5, 3]
</div>

<div class="answer-box">
reverse=True sorts from HIGHEST to LOWEST!
</div>

Perfect for leaderboards! 🏆

---

## ❓ Q14: sorted() vs sort()

```python
original = ["Charlie", "Alice", "Bob"]
new_list = sorted(original)

print(f"New: {new_list}")
print(f"Original: {original}")
```

<div class="quiz-box">
Is the original changed?
</div>

---

## ✅ A14: Original Unchanged!

<div class="terminal-box">
New: ['Alice', 'Bob', 'Charlie']
Original: ['Charlie', 'Alice', 'Bob']
</div>

<div class="success">
sorted() creates a NEW list - original stays the same!
</div>

---

## ❓ Q15: The Trap Question!

```python
usernames = ["xXGamerXx", "ProPlayer", "Noob123"]
usernames.sort()
backup = usernames
print(backup)
```

<div class="quiz-box">
What's in backup?
</div>

**A)** `["xXGamerXx", "ProPlayer", "Noob123"]` (original)
**B)** `["Noob123", "ProPlayer", "xXGamerXx"]` (sorted)
**C)** An error

---

## ✅ A15: The Sorted Version!

<div class="terminal-box">
['Noob123', 'ProPlayer', 'xXGamerXx']
</div>

<div class="warning">
sort() changed the original BEFORE backup was made!
</div>

```python
# Timeline:
# 1. usernames = ["xXGamerXx", "ProPlayer", "Noob123"]
# 2. sort() CHANGES usernames to sorted version
# 3. backup = usernames (already sorted!)
```

---

## ❓ Q16: Safe Function

**Write a function that returns a sorted copy WITHOUT changing the original:**

```python
def get_sorted_leaderboard(scores):
    """Return sorted scores (highest first) without modifying original."""
    # Your code here
    pass

# Test
original = [100, 250, 175, 300, 125]
leaderboard = get_sorted_leaderboard(original)
# leaderboard should be [300, 250, 175, 125, 100]
# original should still be [100, 250, 175, 300, 125]
```

---

## ✅ A16: Use sorted()!

```python
def get_sorted_leaderboard(scores):
    """Return sorted scores (highest first) without modifying original."""
    return sorted(scores, reverse=True)

# Test
original = [100, 250, 175, 300, 125]
leaderboard = get_sorted_leaderboard(original)

print(f"Leaderboard: {leaderboard}")  # [300, 250, 175, 125, 100]
print(f"Original: {original}")         # [100, 250, 175, 300, 125] ✅
```

<div class="answer-box">
sorted(list, reverse=True) = sorted copy, original safe!
</div>

---

<!-- ==================== COMBO QUESTIONS ==================== -->

![bg](https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🎯</div>

# Part 4: Combo Challenge!

<div class="subtitle">Put it all together!</div>

</div>
</div>

---

## ❓ Q17: Find and Count

```python
reactions = ["😂", "❤️", "😂", "🔥", "😂", "❤️", "😂"]

laugh_count = reactions.count("😂")
laugh_position = reactions.index("😂")

print(f"Count: {laugh_count}, First at: {laugh_position}")
```

<div class="quiz-box">
What prints?
</div>

---

## ✅ A17: Count All, Index First!

<div class="terminal-box">
Count: 4, First at: 0
</div>

<div class="answer-box">
count() = ALL occurrences (4), index() = FIRST position (0)
</div>

---

## ❓ Q18: Full Challenge

**Complete this game rank checker:**

```python
def check_rank(players, username):
    """
    Return the player's rank (1-based) or "Not ranked" if not found.
    Players list is already sorted by score (best first).
    """
    # Your code here - use safe index approach!
    pass

# Test
leaderboard = ["ProGamer", "NinjaKid", "xXSlayerXx", "Noob42"]
print(check_rank(leaderboard, "xXSlayerXx"))  # Should print: 3
print(check_rank(leaderboard, "Unknown"))      # Should print: "Not ranked"
```

---

## ✅ A18: Solution

```python
def check_rank(players, username):
    """Return the player's rank (1-based) or "Not ranked"."""
    if username in players:
        position = players.index(username)
        return position + 1  # Convert 0-based to 1-based rank
    return "Not ranked"

# Test
leaderboard = ["ProGamer", "NinjaKid", "xXSlayerXx", "Noob42"]
print(check_rank(leaderboard, "xXSlayerXx"))  # 3
print(check_rank(leaderboard, "Unknown"))      # "Not ranked"
```

---

## ❓ Q19: Alternative Solution

**Rewrite check_rank using try/except instead:**

```python
def check_rank_v2(players, username):
    """Return the player's rank using exception handling."""
    # Your code here!
    pass
```

<div class="quiz-box">
Same result, different approach!
</div>

---

## ✅ A19: Exception Version

```python
def check_rank_v2(players, username):
    """Return the player's rank using exception handling."""
    try:
        position = players.index(username)
        return position + 1
    except ValueError:
        return "Not ranked"

# Both versions work identically!
```

<div class="highlight">
Defensive and Exception handling - both valid!
</div>

---

<!-- ==================== SUMMARY ==================== -->

![bg](https://images.unsplash.com/photo-1552820728-8b83bb6b2b0d?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🏆</div>

# Quick Reference

<div class="subtitle">Everything in one place!</div>

</div>
</div>

---

## 📋 Method Cheat Sheet

| Method | Returns | Safe? | Note |
|--------|---------|-------|------|
| `index(x)` | Position of x | ⚠️ NO | Crashes if not found |
| `count(x)` | How many x | ✅ YES | Returns 0 if not found |
| `sort()` | None | ⚠️ | Changes original list |
| `sorted(list)` | New list | ✅ YES | Original unchanged |

---

## 🛡️ Safe index() Patterns

<div class="two-column">

<div>

### Defensive
```python
if item in my_list:
    pos = my_list.index(item)
else:
    pos = -1
```

</div>

<div>

### Exception
```python
try:
    pos = my_list.index(item)
except ValueError:
    pos = -1
```

</div>

</div>

<div class="success">
Both approaches work! Choose your style!
</div>

---

## 📊 sort() vs sorted()

<div class="two-column">

<div>

### sort() - Modifies
```python
my_list.sort()
# Original CHANGED
# Returns None
```

</div>

<div>

### sorted() - Copies
```python
new = sorted(my_list)
# Original SAFE
# Returns new list
```

</div>

</div>

<div class="key-point">
Use sorted() when you need to keep the original!
</div>

---

<!-- Final Slide -->
![bg](https://images.unsplash.com/photo-1533227268428-f9ed0900fb3b?w=1920&h=1080&fit=crop)

<div class="overlay-dark">
<div class="title-slide">

<div class="emoji-large">🎉</div>

# Excellent Practice!

<div class="success">
You've mastered finding and organizing!
</div>

<div class="big-idea">
Ready for the next challenge! 🚀
</div>

</div>
</div>

<!-- Note: Great work! You now know how to find items, count them, and organize lists safely. Next up: the references vs copies gotcha! -->
