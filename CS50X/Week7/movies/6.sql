SELECT AVG(rating) from movies
JOIN ratings
ON movies.id = ratings.movie_id
WHERE year = 2012;

