-- This script displays the top 3 cities temperature
-- during July and August in descending order
SELECT city, avg_temp FROM (SELECT city, AVG(value) AS "avg_temp"
	FROM tempertatures
	WHERE month = 7 OR month = 8
	GROUP BY city
	ORDER BY AVG(value) DESC) results LIMIT 3;
