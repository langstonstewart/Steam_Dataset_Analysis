
-- Top 25 Developers by Average Game Price

SELECT
	developer,
	AVG(price_usd)::NUMERIC(10,2) AS average_price


FROM apps

WHERE 
	developer IS NOT NULL
	AND developer <> ''
	AND price_usd IS NOT NULL
	
GROUP BY 
	developer
	
ORDER BY 
	average_price DESC
	
	
LIMIT 25
	