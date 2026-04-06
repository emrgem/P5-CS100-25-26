"""
Unit 7, Lesson 4: Python + SQLite
===================================
"""
import sqlite3
DB_FILE = "movies.db"

# ============================================================
# BASIC PATTERN: connect → cursor → execute → fetch
# SELECT 5 movies and print them
# ============================================================
print("=== Basic Pattern: 5 Movies ===")
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, rating FROM movies LIMIT 5")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print()


# ============================================================
# fetchone(): Get a single value
# How many total movies? Look up one movie by id.
# ============================================================



# ============================================================
# PARAMETERIZED QUERIES: ? placeholders
# Search by genre using user input (safe!)
# ============================================================



# ============================================================
# FUNCTION: add_movie(title, genre, rating, review)
# INSERT with ? placeholders
# ============================================================



# ============================================================
# FUNCTION: get_all_movies()
# SELECT all, return fetchall()
# ============================================================




# ============================================================
# FUNCTION: search_movies(keyword)
# SELECT with LIKE ? — build the pattern in Python
# ============================================================




# ============================================================
# YOUR TURN: Write these two functions
#
# FUNCTION: update_rating(movie_id, new_rating)
#   - UPDATE rating WHERE id = ?
#   - Print confirmation with rowcount
#
# FUNCTION: delete_movie(movie_id)
#   - DELETE FROM movies WHERE id = ?
#   - Print confirmation with rowcount
# ============================================================




# ============================================================
# TEST YOUR FUNCTIONS
# Call each function to verify it works
# ============================================================


