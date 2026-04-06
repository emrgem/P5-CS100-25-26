"""
Unit 7, Lesson 3: UPDATE & DELETE
==================================
Learn to change and remove data in your database.

Instructions:
1. Follow along as we write each section together
2. Run this file after each step: python lesson04.py
3. We work on a COPY of movies.db so we can safely break things
"""

import sqlite3
import shutil

# Make a fresh copy every time we run (safe to experiment!)
shutil.copy("movies.db", "movies_practice.db")
DB_FILE = "movies_practice.db"


# ============================================================
# HELPER: Run a query and print results
# ============================================================

def run_query(db, sql):
    """Run a query and print results."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print(f"({len(rows)} rows)\n")



# ============================================================
# UPDATE: Change one column
# Change The Dark Knight's rating to 9.5
# Show before and after
# ============================================================
print("====Before Update====")
run_query(DB_FILE, """
            SELECT title, rating FROM movies WHERE title = 'The Dark Knight'
          """)
run_query(DB_FILE, """
            UPDATE movies SET rating = 9.5 WHERE title = 'The Dark Knight'
          """)
print("====After Update====")
run_query(DB_FILE, """
            SELECT title, rating FROM movies WHERE title = 'The Dark Knight'
          """)

# ============================================================
# UPDATE: Change multiple columns at once
# Change The Matrix's genre and rating
# ============================================================




# ============================================================
# THE GOLDEN RULE: UPDATE without WHERE
# ⚠️ Watch what happens when you forget WHERE
# (comment this out after running once!)
# ============================================================




# ============================================================
# DELETE: Remove a row by title
# Delete a movie, check the count before and after
# ============================================================
print("=== Before Delete ===")
run_query(DB_FILE, "SELECT COUNT(*) FROM movies")

with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE title = 'Pinocchio'")
    print(f"🗑 Deleted ({cursor.rowcount} row)\n")

print("=== After Delete ===")
run_query(DB_FILE, "SELECT COUNT(*) FROM movies")



# ============================================================
# DELETE: Remove rows by condition
# Delete all movies rated below 5.5
# ============================================================
# Delete all movies rated below 5.5
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE rating < 5.5")
    print(f"🗑 Deleted {cursor.rowcount} low-rated movies\n")

run_query(DB_FILE, "SELECT COUNT(*) FROM movies")




# ============================================================
# DELETE by ID: The safest way
# Find a movie's id first, then delete by id
# ============================================================

run_query(DB_FILE, "SELECT id, title, rating FROM movies WHERE rating < 6 LIMIT 5")

with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    # Get the first low-rated movie's id
    cursor.execute("SELECT id FROM movies WHERE rating < 6 LIMIT 1")
    result = cursor.fetchone()
    if result:
        movie_id = result[0]
        cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
        print(f"🗑️ Deleted movie id {movie_id} ({cursor.rowcount} row)\n")


print("=== Verify it's gone ===")
run_query(DB_FILE, "SELECT COUNT(*) FROM movies")


# ============================================================
# CHALLENGES: Try these on your own!
#
# 1. Change the genre of "Jaws" from "Horror" to "Thriller"
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET genre = 'Thriller' WHERE title = 'Jaws'")
run_query(DB_FILE, "SELECT title, genre FROM movies WHERE title = 'Jaws' ")
# 2. Give all Animation movies a rating boost of +0.2D
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET rating = rating + 0.2 WHERE genre = 'Animation' ")
run_query(DB_FILE, "SELECT title, rating FROM movies WHERE genre = 'Animation' ")
# 3. Delete all movies from before 1970
run_query(DB_FILE, "SELECT title, year FROM movies WHERE year < 1970")
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE year < 1970")
    print(f"🗑️ Deleted {cursor.rowcount} old movies\n")


# 4. Find all movies with a NULL review, then delete them
print("=== Challenge 4: Delete movies with NULL review ===")
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE review IS NULL")
    print(f"🗑️ Deleted {cursor.rowcount} movies with no review\n")



# 5. How many movies are left? (SELECT COUNT)
# ============================================================

print("=== Challenge 5: How many left? ===")
run_query(DB_FILE, "SELECT COUNT(*) FROM movies")


