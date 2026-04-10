"""
Unit 7, Lesson 5: Full Database App
=====================================
Build a complete menu-driven CRUD app with SQLite.
"""
import sqlite3
DB_FILE = "my_app.db"

# ============================================================
# init_db() — Create the table if it doesn't exist
# ============================================================
def init_db():
    """Create the movies table is it does not exist"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS movies (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           genre TEXT NOT NULL,
                           rating REAL,
                           review TEXT
                       )""")


# ============================================================
# add_movie() — Get input from user, INSERT into database
# ============================================================
def add_movie():
    """Get a movie info from the user and save to the database"""
    title = input("Title: ")
    genre = input("Genre: ")
    try:
        rating = float(input("Rating (1-10): "))
    except ValueError:
        print("❌ Rating must be a number!")
        return #early termination
    review = input("Short Review: ")
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO movies (title, genre, rating, review)
                       VALUES (?, ?, ?, ?)""", (title, genre, rating, review))
        print(f"✅ Added '{title}' ")


# ============================================================
# display_movies() — Format and print a list of movie tuples
# Reusable helper for view_all and search
# ============================================================
def display_movies(movies):
    """Display a list of movie tuples in a nice format"""
    if not movies:
        print(" No movies found!")
        return #Early termination
    for movie in movies:
        print(f"[{movie[0]}] {movie[1]} ({movie[2]})-{movie[3]}/10" + f" {movie[4]}" if movie[4] else "")
        # if movie[4]:
        #     print(f"    {movie[4]}")
    print(f"({len(movies)}) movies.")
 
# ============================================================
# view_all_movies() — SELECT all, display formatted
# ============================================================
def view_all_movies():
    """Makes a connection to the DB and shows all movies sorted by rating"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, title, genre, rating, review FROM movies
                       ORDER BY rating DESC""")
        movies = cursor.fetchall()
    display_movies(movies)


# ============================================================
# search_movies() — Search by title keyword with LIKE
# ============================================================
def search_movies():
    """Search movies by title keyword  """
    keyword = input("Search Title: ")
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, title, genre, rating, review FROM movies
                       WHERE title LIKE ?
                       ORDER BY rating DESC""", (f"%{keyword}%",))
        movies = cursor.fetchall()
    print(f"\n 🔍 Search Results:")
    display_movies(movies)
    
# ============================================================
# update_rating() — Show all(view all movies), pick an ID to update, UPDATE rating value
# ============================================================



# ============================================================
# delete_movie() — Show all(view all movies), pick an ID to, DELETE row
# ============================================================



# ============================================================
# view_stats() — COUNT, AVG, GROUP BY genre
# ============================================================
def view_stats():
    """Show database statistics."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM movies")
        total = cursor.fetchone()[0]
        
        if total == 0:
            print("\n📊 No movies in database yet.")
            return

        cursor.execute("SELECT ROUND(AVG(rating), 1) FROM movies")
        avg = cursor.fetchone()[0]

        cursor.execute("""
            SELECT genre, COUNT(*), ROUND(AVG(rating), 1)
            FROM movies GROUP BY genre ORDER BY COUNT(*) DESC
        """)
        genres = cursor.fetchall()

    print(f"\n📊 Stats: {total} movies, avg rating: {avg}/10")
    print("  Genre breakdown:")
    for g in genres:
        print(f"    {g[0]}: {g[1]} movies (avg {g[2]}/10)")


# ============================================================
# main() — Menu loop that ties everything together
# ============================================================
def main():
    init_db()
    #App Menu Loop
    while True:
        print("""
              🎞️  Movie Database
              1. Add a movie
              2. View All Movies
              3. Search Movies
              4. Updata a rating
              5. Delete a movie
              6. View Stats
              7. Quit
              """)
        choice = input("\n Choice:")
        if choice == "7":
            print("Goodbye! 👋")
            break
        elif choice == "1":
            add_movie()
        elif choice == "2":
            view_all_movies()
        elif choice == "3":
            search_movies()
# ============================================================
# Run the app
# ============================================================

if __name__ == "__main__":
    main()
