-- this query to list the cities of california that can be found in the DB
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = "California"
)
ORDER BY cities.id ASC;
