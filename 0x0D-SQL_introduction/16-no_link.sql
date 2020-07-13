-- SELECT score and name
-- name should be not NULL and Records should be listed by descending score order

SELECT score, name FROM second_table where name is not NULL ORDER BY score DESC; 
