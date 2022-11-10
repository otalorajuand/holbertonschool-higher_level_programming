-- displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending).
SELECT city, avg(temperature) AS avg_temp
FROM temperature
ORDER BY temperature;
