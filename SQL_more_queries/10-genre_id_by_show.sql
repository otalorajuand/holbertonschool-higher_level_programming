-- lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked.
SELECT t2.title, t1.genre_id
FROM tv_show_genres t1
LEFT JOIN tv_shows t2
ON t1.genre_id = t2.id
ORDER BY t2.title ASC, t1.genre_id ASC;
