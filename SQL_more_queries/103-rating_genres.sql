-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT t1.name, sum(t3.rate) AS rating
FROM tv_genres t1
LEFT JOIN tv_show_genres t2
ON t1.id = t2.genre_id
LEFT JOIN tv_show_ratings t3
ON t2.show_id = t3.show_id
GROUP BY t1.name
ORDER BY sum(t3.rate) DESC;
