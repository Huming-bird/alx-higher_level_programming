-- this script lists all cities contained in the DB
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.states_id = states.id
ORDER BY cities.id ASC;
