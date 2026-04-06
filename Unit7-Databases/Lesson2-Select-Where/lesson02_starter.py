"""Unit 7, Lesson 2: SELECT & WHERE"""
import sqlite3
DB_FILE = "movies.db"

# ============================================================
# HELPER: Run a query and print results
# Write this first — we'll use it for every query.
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
# QUERY 1: SELECT all movies
# ============================================================
run_query(DB_FILE,"SELECT * FROM movies;")

# Specific Columns Only
run_query(DB_FILE,"SELECT title, genre, rating FROM movies;")

# ============================================================
# QUERY 2-4: WHERE — Filter by genre, rating, year
# ============================================================
run_query(DB_FILE,"""SELECT title, rating FROM movies
                     WHERE genre = 'Action'
                  """)
run_query(DB_FILE,"""SELECT title, rating FROM movies
                     WHERE rating > 9
                  """)


# ============================================================
# QUERY 5-7: AND / OR — Combine conditions
# ============================================================
run_query(DB_FILE,"""SELECT title, rating FROM movies
                     WHERE rating >= 9 AND genre = 'Action'
                  """)




# ============================================================
# QUERY 8-10: ORDER BY + LIMIT — Sort and cap results
# ============================================================
# Top 5 highest rated movies
run_query(DB_FILE,"""SELECT title, genre, rating FROM movies
                     ORDER BY rating DESC
                     LIMIT 5
                  """)


# 10 newest movies
run_query(DB_FILE,"""SELECT title, genre, rating FROM movies
                     ORDER BY year DESC
                     LIMIT 10
                  """)

# Top 5 action movies
run_query(DB_FILE,"""SELECT title, genre, rating FROM movies
                     WHERE genre = 'Action'
                     ORDER BY rating DESC
                     LIMIT 5
                  """)
# ============================================================
# QUERY 11-13: LIKE — Text search
# ============================================================

# contains 'spider'
run_query(DB_FILE,"""SELECT title, year FROM movies
                     WHERE title LIKE '%spider%'
                  """)
#starts with "The"
run_query(DB_FILE,"""SELECT title, genre FROM movies
                     WHERE title LIKE 'The%'
                     ORDER BY title 
                     LIMIT 10
                  """)
# ============================================================
# QUERY 14-17: Aggregates — COUNT, AVG, GROUP BY
# ============================================================
run_query(DB_FILE,"""SELECT COUNT(*) FROM movies; """)
run_query(DB_FILE,"""SELECT ROUND(AVG(rating),1) FROM movies; """)
run_query(DB_FILE,"""SELECT MAX(rating) FROM movies; """)
run_query(DB_FILE,"""SELECT MIN(year) FROM movies; """)




# ============================================================
# QUERY 18: The "Impossible with CSV" query
# Top 3 genres by average rating with count
# ============================================================




# ============================================================
# CHALLENGES: Try these on your own!
#
# 1. All Horror movies rated above 7, sorted by rating (highest first)
# 2. The 5 oldest movies in the database
# 3. How many movies were made after 2020?
# 4. All movies with "love" in the title
# 5. Which genre has the most movies?
# ============================================================


