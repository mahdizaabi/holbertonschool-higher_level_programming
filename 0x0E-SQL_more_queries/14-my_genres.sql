-- lists all genres of the show Dexter.

SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id

JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;




SELECT tv_genres.name
FROM tv_genres
Join tv_show_genres 
ON tv_show_genres.genre_id = tv_genres.id
SELECT tv_shows.title
FROM tv_shows
Join  tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
