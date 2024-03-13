-- this is a query to display the max temperature value of each state in the order of the state name
SELECT state, MAX(value) AS 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state
