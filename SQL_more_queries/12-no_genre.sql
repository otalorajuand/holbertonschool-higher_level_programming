-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT t1.title, t2.genre_id
FROM tv_shows t1
LEFT JOIN  tv_show_genres t2
ON t1.id = t2.show_id
WHERE t2.genre_id IS NULL
ORDER BY t1.title ASC, t2.genre_id ASC;

