-- displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending).
mysql -u username -p hbtn_0c_0 < temperatures.sql;

SELECT city, avg(temperature) AS avg_temp
FROM temperatures
ORDER BY temperature;
