CREATE TABLE apps (
    appid INT PRIMARY KEY,
    name VARCHAR(255),
    releasedate VARCHAR(100),
    is_free BOOLEAN,
    price_usd NUMERIC(10, 2),
    genre VARCHAR(100),
    achievement_count INT,
    developer VARCHAR(255),
    publisher VARCHAR(255),
    player_count INT,
    review_score INT,
    review_score_desc VARCHAR(100),
    total_positive INT,
    total_negative INT,
    total_reviews INT
);