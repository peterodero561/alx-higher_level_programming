-- lists all shows contained in the hbtn_0d_shows
-- Results must be sorted in ascending order by tv_shows.title
-- and tv_show_genres.genre_id
-- if show does not have genre diplay null
-- use only one select statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
