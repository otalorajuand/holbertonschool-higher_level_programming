-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT t1.title, sum(t2.rate) as rating
FROM tv_shows t1
LEFT JOIN tv_show_ratings t2
ON t1.id = t2.show_id
GROUP BY t1.title
ORDER BY sum(t2.rate) DESC;