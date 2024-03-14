-- this query to display list of cities contained in the DB hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
