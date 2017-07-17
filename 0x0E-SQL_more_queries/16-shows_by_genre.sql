--  lists all shows, and all genres linked to that show in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;
