-- this is a script to list all records of the second_table of the DB 
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
