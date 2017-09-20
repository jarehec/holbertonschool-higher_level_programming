## 0x0E. SQL - More queries

The focus of this project is to learn:
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What's a PRIMARY KEY
* What's a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

## Environment
* Ubuntu 14.04 LTS
## File Descriptions
* 0-privileges.sql
	* lists privileges for user_0d_1 and user_0d_2
* 1-create_user.sql
	* creates user user_0d_1
* 2-create_read_user.sql
	* creates hbtn_0d_2 database and user_0d_2 user
* 3-force_name.sql
	* creates the table force_name
* 4-never_empty.sql
	* creates the table id_not_null
* 5-unique_id.sql
	* creates the table unique_id
* 6-states.sql
	* creates the databse hbtn_0d_usa and the table states
* 7-cities.sql
	* creates the database hbtn_0d_usa and cities table
* 8-cities_of_california_subquery.sql
	* lists all the cities in California
* 9-cities_by_state_join.sql
	* lists all the cities in hbtn_0d_usa
* 10-genre_id_by_show.sql
	* lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
* 11-genre_id_all_shows.sql
	* lists all shows contained in the database hbtn_0d_tvshows 
* 12-no_genre.sql
	* lists all shows contained in hbtn_0d_tvshows without a genre linked
* 13-count_shows_by_genre.sql
	* lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
* 14-my_genres.sql
	* lists all genres of the show Dexter
* 15-comedy_only.sql
	* lists all Comedy shows in the database hbtn_0d_tvshows
* 16-shows_by_genre.sql
	* lists all shows, and all genres linked to that show in the database hbtn_0d_tvshows
