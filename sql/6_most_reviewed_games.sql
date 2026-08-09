WITH review_data AS (

	SELECT
	name,
	total_reviews,
	total_positive,
	total_negative,  
	ROUND((total_positive::NUMERIC / (total_positive::NUMERIC + total_negative::NUMERIC)) * 100, 2) AS positive_review_score
	
FROM apps

WHERE
	total_positive > 0
	AND total_negative > 0
ORDER BY 
	total_reviews DESC

LIMIT 25)


-- By Review Score
SELECT *

FROM review_data 

ORDER BY

	positive_review_score DESC
