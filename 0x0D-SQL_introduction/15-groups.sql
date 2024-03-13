-- lists the numberof records with the same score in taable second_table

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
