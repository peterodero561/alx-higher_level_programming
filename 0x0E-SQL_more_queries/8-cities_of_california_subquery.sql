-- lists all the cities in California that can befound in the database
-- the states able contain only one record where name=California
-- results must be sorted in ascending order by cities.id
-- not allowed to use join

SELECT cities.id, cities.name
FROM cites
WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name='California')
ORDER BY cities.id ASC;
