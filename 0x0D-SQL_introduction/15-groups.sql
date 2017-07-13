-- lists the number of records with the same score
SELECT score, COUNT(*) member FROM second_table GROUP BY score HAVING member > 1 ORDER BY score DESC;
