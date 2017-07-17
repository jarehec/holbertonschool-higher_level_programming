-- lists all the cities in California
SELECT id,name FROM cities WHERE state_id = (SELECT id FROM states WHERE states.name="California") ORDER BY cities.id ASC;
