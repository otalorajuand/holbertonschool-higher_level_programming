SELECT city, avg(value) AS avg_temp
FROM temperatures
WHERE MONTH BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
