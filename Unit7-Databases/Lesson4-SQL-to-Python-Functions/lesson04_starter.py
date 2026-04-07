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
    rows = cursor.fetchall() # List of tuples

    # for row in rows:
    #     print(row)
    # print(rows)


# ============================================================
# fetchone(): Get a single value
# How many total movies?
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    result = cursor.fetchone()
    # print(f"Total Movies: {result[0]}")
    
# Look up one movie by id.
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, rating FROM movies WHERE id = 1")
    movie = cursor.fetchone()
    # if movie:
    #     print(f"{movie[0]} ({movie[1]} - {movie[2]}/10)")
    # else:
    #     print("Movie not found!")
# ============================================================
# PARAMETERIZED QUERIES: ? placeholders
# Search by genre using user input (safe!)
# ============================================================
# genre = input("Enter a Genre:")
# with sqlite3.connect(DB_FILE) as conn:
#     cursor = conn.cursor()
#     cursor.execute("""SELECT title, rating FROM movies 
#                       WHERE genre = ? 
#                       ORDER BY rating DESC LIMIT 5""", (genre,))
#     rows = cursor.fetchall()
    
#     print(f"Top 5 {genre} movies:")
#     for row in rows:
#         print(f"  {row[0]} — {row[1]}/10")
#     print()



# ============================================================
# FUNCTION: add_movie(title, genre, rating, review)
# INSERT with ? placeholders
# ============================================================
def add_movie(title, genre, rating, review):
    """INSERT a new movie into the database"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO movies (title, genre, rating, review) VALUES (?, ?, ?, ?)
                       """, (title, genre, rating, review))
        print(f"✅ Added '{title}'")

add_movie("My test movie", "Comedy", 7.5, "Just a test")
# ============================================================
# FUNCTION: get_all_movies()
# SELECT all, return fetchall()
# ============================================================
def get_all_movies():
    """Get all movies sorted by rating(highest first)"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, title, genre, rating FROM movies
                       ORDER BY rating DESC
                       """)
        return cursor.fetchall()
    
movies = get_all_movies()
# Get the first 10 movies
for movie in movies[:10]:
    print(f"{movie[0]}: {movie[1]} {movie[2]} - {movie[3]}/10")



# ============================================================
# FUNCTION: search_movies(keyword)
# SELECT with LIKE ? — build the pattern in Python
# ============================================================
def search_movies(keyword):
    """Search movies by title keyword"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, title, genre, rating FROM movies
                       WHERE title LIKE ?""", (f"%{keyword}%",))
        return cursor.fetchall()

results = search_movies("cat")
print("=====SEARCH MOVIES=======")
for movie in results:
    print(f"{movie[0]}: {movie[1]} {movie[2]} - {movie[3]}/10")

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


