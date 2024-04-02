SELECT title, rating
FROM movies JOIN ratings
ON movies.id = ratings.movie_id
WHERE year = 2010 and rating NOT NULL
ORDER BY rating DESC, title ASC;
