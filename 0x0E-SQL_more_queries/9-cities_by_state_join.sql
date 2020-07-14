-- lists all cities contained in the database

SELECT id, name, states.name
FROM cities
JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
