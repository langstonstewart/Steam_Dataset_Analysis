
-- Top 15 Free To Play

WITH top_15_ftp AS  (

	SELECT
	name,
	player_count,
	is_free

FROM apps

WHERE
	player_count IS NOT NULL
	AND is_free
ORDER BY
	player_count DESC

LIMIT 15),

-- Top 15 Pay To Play

top_15_ptp AS (

	SELECT
	name,
	player_count,
	price_usd,
	is_free

FROM apps

WHERE
	player_count IS NOT NULL
	AND NOT is_free
ORDER BY
	player_count DESC

LIMIT 15),


-- Compare the 30 Games Together

top_30_combined AS (
	SELECT
	name,
	player_count,
	CASE
		WHEN is_free THEN 'Free-To-Play'
		ELSE 'Paid'
	END AS free_or_paid

FROM top_15_ftp 

UNION

SELECT
	name,
	player_count,
	CASE
		WHEN is_free THEN 'Free-To-Play'
		ELSE 'Paid'
	END AS free_or_paid

FROM top_15_ptp 

ORDER BY 
	player_count DESC)

	
-- Calculate the average player count between free-to-play and pay-to-play to see which option players prefer
	
SELECT
	free_or_paid,
	AVG(player_count)::INTEGER

FROM top_30_combined 

GROUP BY 
	free_or_paid 
	
	

