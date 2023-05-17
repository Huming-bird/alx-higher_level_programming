-- this script lists all citites of CA found in the DB
SELECT `id`, `name` FROM cities
WHERE state_id = (
  SELECT id FROM states
  WHERE name = 'California'
)
ORDER BY id ASC;
