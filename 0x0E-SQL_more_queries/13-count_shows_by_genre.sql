-- this script counts number of shows by genres
SELECT tv_genres.genre AS genre,
       (SELECT COUNT(*) FROM tv_show_genres WHERE tv_show_genres.genre_id = tv_genres.id) AS number_of_shows
FROM tv_genres
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

