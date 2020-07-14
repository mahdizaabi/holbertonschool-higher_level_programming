-- lists all the cities of California that can be found in the database

SELECT name, id
FROM cities
WHERE state_id=1;
ORDER BY id ASC;
