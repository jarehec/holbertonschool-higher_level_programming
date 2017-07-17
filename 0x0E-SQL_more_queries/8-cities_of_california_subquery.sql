-- lists all the cities in California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE states.name="California");
