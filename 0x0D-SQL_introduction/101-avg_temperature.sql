-- This script displays the average temperature(fahrenheit)
-- By city ordered by temperature (descending)
SELECT city,
AVG(value) AS "avg_temp" FROM temperatures GROUP BY city
ORDER BY AVG(value) DESC;
