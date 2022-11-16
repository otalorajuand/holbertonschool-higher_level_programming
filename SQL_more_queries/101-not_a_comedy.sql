-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title 
FROM tv_shows
WHERE id NOT IN
(SELECT t2.show_id
FROM tv_genres t1
LEFT JOIN tv_show_genres t2
ON t1.id = t2.genre_id
WHERE name = "Comedy")
ORDER BY title ASC;