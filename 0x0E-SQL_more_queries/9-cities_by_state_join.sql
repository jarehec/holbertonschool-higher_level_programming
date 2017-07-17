-- lists all the cities in hbtn_0d_usa
SELECT cities.id,cities.name,states.name FROM cities LEFT JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;
