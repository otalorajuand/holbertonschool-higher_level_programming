-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t1.title
FROM tv_shows t1
LEFT JOIN  tv_show_genres t2
ON t1.id = t2.show_id
LEFT JOIN tv_genres t3
ON t2.genre_id = t3.id
WHERE t3.name = 'Comedy'
ORDER BY t1.title ASC;
