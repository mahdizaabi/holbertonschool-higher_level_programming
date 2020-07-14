-- lists all cities contained in the database

SELECT cities.id, citites.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
