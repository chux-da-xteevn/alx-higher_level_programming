-- this query lists the record with same score value
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
