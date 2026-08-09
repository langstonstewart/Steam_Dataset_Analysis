
SELECT
	EXTRACT(YEAR FROM releasedate::DATE) AS YEAR,
	AVG(price_usd)::NUMERIC(10,2) AS average_price,
	ROUND(((AVG(price_usd) - LAG(AVG(price_usd)) OVER (ORDER BY EXTRACT(YEAR FROM releasedate::DATE))) / LAG(AVG(price_usd)) OVER (ORDER BY EXTRACT(YEAR FROM releasedate::DATE)) * 100), 2) AS percent_change

FROM apps

WHERE 
	releasedate IS NOT NULL
	AND releasedate <> ''
	AND price_usd IS NOT NULL
	
GROUP BY
	YEAR
	
ORDER BY
	year ASC
	