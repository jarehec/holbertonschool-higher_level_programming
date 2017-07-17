-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, genre_id FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
