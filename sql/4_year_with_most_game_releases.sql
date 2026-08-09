
-- Years Sorted by Game Release Count

SELECT
	EXTRACT(YEAR FROM releasedate::DATE) AS YEAR,
	COUNT(*) AS game_count


FROM apps

WHERE 
	releasedate IS NOT NULL
	AND releasedate <> ''
	
GROUP BY
	YEAR
	
ORDER BY
	game_count DESC;

-- Top 15 Games From 2025
	
SELECT
	name,
	player_count

FROM apps

WHERE 
	releasedate IS NOT NULL
	AND releasedate <> ''
	AND EXTRACT(YEAR FROM releasedate::DATE) = '2025'
	
ORDER BY 
	player_count DESC

LIMIT 15

