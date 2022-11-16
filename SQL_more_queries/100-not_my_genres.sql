-- list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN
(SELECT t2.genre_id
FROM tv_shows t1
LEFT JOIN tv_show_genres t2
ON t1.id = t2.show_id
WHERE title = "Dexter")
ORDER BY name ASC;
