--SELECT title, rating FROM movies
--WHERE genre = 'Action' AND rating > 8
--ORDER BY rating DESC;

--How many Movies total?
--SELECT COUNT(*) FROm movies;

--Average rating of all moviesmovies
--SELECT ROUND(AVG(rating),1) FROM movies;

CREATE TABLE IF NOT EXISTS my_movies (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    title   TEXT NOT NULL,
    genre   TEXT NOT NULL,
    rating  REAL,
    year    INTEGER,
    review  TEXT
);