-- this query to display the average temp in Fahrenheit in DESC order
SELECT city, AVG(value) AS `avg_temp`
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
