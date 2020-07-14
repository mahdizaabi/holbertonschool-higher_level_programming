-- lists all the cities of California that can be found in the database
-- use of subquery to retrieve the id corresponding to the table(state)s
SELECT id, name
FROM cities
WHERE state_id = (SELECT ID FROM states WHERE name='California')
ORDER BY id ASC;
