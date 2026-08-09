SELECT
	name,
	player_count 

FROM apps

WHERE
	player_count IS NOT NULL
ORDER BY
	player_count DESC


LIMIT 25