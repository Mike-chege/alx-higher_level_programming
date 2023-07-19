-- This script lists the number of records with the same value
-- In the table second_table
SELECT score, COUNT(*) AS "number"
FROM second_table GROUP BY score
ORDER BY score DESC;
