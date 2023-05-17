-- this script lists all citites of CA found in the DB
USE hbtn_0d_usa;

SELECT * FROM cities
WHERE state_id = (
  SELECT id FROM states
  WHERE name = 'California'
)
ORDER BY id ASC;
