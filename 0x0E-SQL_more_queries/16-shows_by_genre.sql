--  lists all shows, and all genres linked to that show, from the database

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id;
