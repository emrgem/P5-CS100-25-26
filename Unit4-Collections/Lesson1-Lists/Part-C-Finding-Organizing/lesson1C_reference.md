# Unit 4 - Lesson 1C Reference Guide
## Finding & Organizing Lists

---

## 📍 index() - Find the Position

**What it does:** Returns the INDEX (position) of the first occurrence of an item.

```python
playlist = ["Flowers", "Anti-Hero", "Unholy", "As It Was"]
#              0           1          2           3

position = playlist.index("Unholy")
print(position)  # 2
```

### ⚠️ DANGER: Crashes if item not found!

```python
playlist.index("Despacito")  # ValueError: 'Despacito' is not in list
```

### ✅ Safe Approach 1: Defensive (Check First)

```python
def safe_index_defensive(my_list, item):
    """Find item position safely using 'in' check."""
    if item in my_list:
        return my_list.index(item)
    return -1  # Not found indicator
```

### ✅ Safe Approach 2: Exception Handling

```python
def safe_index_exception(my_list, item):
    """Find item position safely using try/except."""
    try:
        return my_list.index(item)
    except ValueError:
        return -1  # Not found indicator
```

### 🔑 Key Points

- Returns **first occurrence only** (if duplicates exist)
- Returns 0-based index (first item = 0)
- **Always use safe handling!**

---

## 🔢 count() - Count Occurrences

**What it does:** Returns how many times an item appears in the list.

```python
reactions = ["😂", "❤️", "😂", "🔥", "😂", "❤️"]

laugh_count = reactions.count("😂")
print(laugh_count)  # 3

fire_count = reactions.count("🔥")
print(fire_count)  # 1
```

### 🎉 ALWAYS SAFE - No error handling needed!

```python
# Item doesn't exist? No problem!
missing_count = reactions.count("🎮")
print(missing_count)  # 0 (no crash!)
```

### 🔑 Key Points

- Returns **0** if item not found (no crash!)
- Counts **all occurrences**, not just first
- No try/except or `if in` check needed!

---

## 🆚 index() vs count() Comparison

| Feature | index() | count() |
|---------|---------|---------|
| **Returns** | Position (int) | Quantity (int) |
| **If not found** | ❌ ValueError CRASH | ✅ Returns 0 |
| **Needs error handling** | YES | NO |
| **Multiple occurrences** | First only | Counts all |

---

## 📊 sort() - Sort In Place

**What it does:** Sorts the list **in place** (modifies the original).

```python
scores = [85, 92, 78, 95, 88]
scores.sort()
print(scores)  # [78, 85, 88, 92, 95]
```

### 🔄 Reverse Order (Highest First)

```python
scores = [85, 92, 78, 95, 88]
scores.sort(reverse=True)
print(scores)  # [95, 92, 88, 85, 78]
```

### ⚠️ WARNING: Returns None!

```python
scores = [85, 92, 78, 95, 88]
result = scores.sort()  # DON'T DO THIS!
print(result)  # None (not the sorted list!)
print(scores)  # [78, 85, 88, 92, 95] (list IS sorted though)
```

### 🔑 Key Points

- **Modifies original** list permanently
- Returns **None** (not the sorted list)
- Use `reverse=True` for descending order

---

## ✨ sorted() - Return Sorted Copy

**What it does:** Returns a **new sorted list**, original stays unchanged.

```python
original = ["Charlie", "Alice", "Bob"]
alphabetical = sorted(original)

print(alphabetical)  # ['Alice', 'Bob', 'Charlie']
print(original)      # ['Charlie', 'Alice', 'Bob'] (unchanged!)
```

### 🔄 Reverse Order (Highest First)

```python
scores = [85, 92, 78, 95, 88]
leaderboard = sorted(scores, reverse=True)

print(leaderboard)  # [95, 92, 88, 85, 78]
print(scores)       # [85, 92, 78, 95, 88] (original unchanged!)
```

### 🔑 Key Points

- **Creates new list** - original is SAFE
- Returns the sorted list (unlike sort())
- Use `reverse=True` for descending order

---

## 🆚 sort() vs sorted() Comparison

| Feature | sort() | sorted() |
|---------|--------|----------|
| **Type** | Method | Function |
| **Syntax** | `my_list.sort()` | `sorted(my_list)` |
| **Original list** | ⚠️ MODIFIED | ✅ Unchanged |
| **Returns** | None | New sorted list |
| **reverse option** | ✅ Yes | ✅ Yes |

### When to Use Which?

```python
# Use sort() when you don't need the original order
players = ["Zoe", "Alex", "Maya"]
players.sort()  # OK to change original

# Use sorted() when you need to KEEP the original
join_order = ["Tyler", "Alex", "Sam"]
alphabetical = sorted(join_order)  # Original preserved!
```

---

## 🛡️ Quick Safety Reference

| Method | Safe? | What Happens If Not Found |
|--------|-------|---------------------------|
| `index()` | ⚠️ NO | ValueError crash |
| `count()` | ✅ YES | Returns 0 |
| `sort()` | ⚠️ * | Changes original list |
| `sorted()` | ✅ YES | Original unchanged |

*sort() is "safe" from crashes but modifies your data!

---

## 📝 Common Patterns

### Pattern 1: Safe Position Lookup

```python
def get_position(items, target):
    """Return position or -1 if not found."""
    if target in items:
        return items.index(target)
    return -1
```

### Pattern 2: Check If Item Exists and How Many

```python
def item_info(items, target):
    """Return count and first position of target."""
    count = items.count(target)  # Always safe!
    if count > 0:
        position = items.index(target)  # Safe because count > 0
        return count, position
    return 0, -1
```

### Pattern 3: Get Sorted Copy for Display

```python
def display_leaderboard(scores):
    """Display scores from highest to lowest without changing original."""
    ranked = sorted(scores, reverse=True)
    for i, score in enumerate(ranked):
        print(f"#{i + 1}: {score}")
```

### Pattern 4: Convert Index to Rank

```python
def get_rank(leaderboard, player):
    """Return 1-based rank or 'Not ranked'."""
    if player in leaderboard:
        return leaderboard.index(player) + 1  # Convert 0-based to 1-based
    return "Not ranked"
```

---

## ❌ Common Mistakes to Avoid

### Mistake 1: Using index() Without Safety Check

```python
# ❌ BAD - Can crash!
position = my_list.index(item)

# ✅ GOOD - Safe!
if item in my_list:
    position = my_list.index(item)
```

### Mistake 2: Expecting sort() to Return Something

```python
# ❌ BAD - result will be None!
result = my_list.sort()

# ✅ GOOD - Use sorted() if you need the result
result = sorted(my_list)

# ✅ ALSO GOOD - sort() then use the list
my_list.sort()
# Now use my_list directly
```

### Mistake 3: Forgetting sort() Changes Original

```python
# ❌ BAD - Original is lost!
original = [3, 1, 2]
original.sort()
# Can't get back [3, 1, 2]!

# ✅ GOOD - Keep original safe
original = [3, 1, 2]
sorted_copy = sorted(original)
# original still [3, 1, 2]
```

### Mistake 4: Confusing count() and index()

```python
my_list = ["a", "b", "a", "c", "a"]

# count() = how many? → 3
my_list.count("a")  # Returns 3

# index() = where is first one? → 0
my_list.index("a")  # Returns 0
```

---

## 🎯 Practice Exercises

### Exercise 1: Safe Song Finder
Write a function that finds a song's position in a playlist safely.

```python
def find_song(playlist, song):
    """Return song position (0-based) or -1 if not found."""
    # Your code here
    pass
```

### Exercise 2: Duplicate Checker
Write a function that checks if an item appears more than once.

```python
def has_duplicates(items, target):
    """Return True if target appears more than once."""
    # Your code here (hint: use count!)
    pass
```

### Exercise 3: Safe Leaderboard
Write a function that returns a sorted leaderboard without modifying the original scores.

```python
def create_leaderboard(scores):
    """Return scores sorted highest to lowest. Don't modify original!"""
    # Your code here (hint: use sorted!)
    pass
```

### Exercise 4: Rank Finder
Write a function that returns a player's rank (1-based) on a leaderboard.

```python
def get_player_rank(leaderboard, player):
    """Return rank (1, 2, 3...) or 'Unranked' if not found."""
    # Your code here
    pass
```

---

## ✅ Exercise Solutions

```python
# Exercise 1
def find_song(playlist, song):
    if song in playlist:
        return playlist.index(song)
    return -1

# Exercise 2
def has_duplicates(items, target):
    return items.count(target) > 1

# Exercise 3
def create_leaderboard(scores):
    return sorted(scores, reverse=True)

# Exercise 4
def get_player_rank(leaderboard, player):
    if player in leaderboard:
        return leaderboard.index(player) + 1
    return "Unranked"
```

---

**Unit 4 - Lesson 1C Complete!** 🎉

Next up: **Lesson 1D - References vs Copies (THE GOTCHA!)** 😱
