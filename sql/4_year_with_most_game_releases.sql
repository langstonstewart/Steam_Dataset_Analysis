
-- Total Concurrent Player Count by Release Year, With Year-Over-Year Percent Change

SELECT
	EXTRACT(YEAR FROM releasedate::DATE) AS YEAR,
	SUM(player_count) AS total_player_count,
	ROUND(((SUM(player_count) - LAG(SUM(player_count)) OVER (ORDER BY EXTRACT(YEAR FROM releasedate::DATE))) / LAG(SUM(player_count)) OVER (ORDER BY EXTRACT(YEAR FROM releasedate::DATE)) * 100), 2) AS percent_change

FROM apps

WHERE 
	releasedate IS NOT NULL
	AND releasedate <> ''
	AND EXTRACT(YEAR FROM releasedate::DATE) <= 2025
	
GROUP BY
	YEAR
	
ORDER BY
	year ASC

