-- lists all the cities of California that can be found in the database

SELECT *
FROM states
WHERE name = 'California'
ORDER BY cities.id;
