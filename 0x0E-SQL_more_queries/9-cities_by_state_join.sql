-- lists all cities contained in a database
-- records should display cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- use only one select statement

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id=states.id
ORDER BY cities.id ASC;
