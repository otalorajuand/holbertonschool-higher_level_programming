--  lists all genres from hbtn_0d_tvshows and displays the number
-- of shows linked to each.
SELECT t3.name, count(*) AS number_of_shows
FROM tv_shows t1
LEFT JOIN  tv_show_genres t2
ON t1.id = t2.show_id
LEFT JOIN tv_genres t3
ON t2.genre_id = t3.id
WHERE t2.genre_id IS NOT NULL
GROUP BY t3.name;
