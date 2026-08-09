
-- Genres Sorted By Popularity

SELECT
	genre,
	SUM(player_count) AS player_count

FROM apps

WHERE
	genre IS NOT NULL
	AND genre <> ''

GROUP BY 
	genre
	
ORDER BY 
	player_count DESC;

