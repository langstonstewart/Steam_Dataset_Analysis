
SELECT
	developer,
	COUNT(*) AS no_of_games_developed


FROM apps

WHERE 
	developer IS NOT NULL
	AND developer <> ''
	
GROUP BY 
	developer
	
ORDER BY 
	no_of_games_developed DESC
	
	
LIMIT 15
	