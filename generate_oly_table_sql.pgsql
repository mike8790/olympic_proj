
CREATE TABLE all_olympics AS 
SELECT country_all AS country
FROM (SELECT DISTINCT atlanta_1996.country, 
sydney_2000.country, athens_2004.country,
beijing_2008.country, london_2012.country,
rio_2016.country,
average_rank.country, COALESCE(atlanta_1996.country, 
sydney_2000.country, athens_2004.country,
beijing_2008.country, london_2012.country,
rio_2016.country,
average_rank.country) AS country_all
FROM average_rank
FULL JOIN atlanta_1996 ON atlanta_1996.country = average_rank.country
FULL JOIN sydney_2000 ON sydney_2000.country = COALESCE(atlanta_1996.country, average_rank.country)
FULL JOIN athens_2004 ON athens_2004.country = COALESCE(atlanta_1996.country, sydney_2000.country, average_rank.country)
FULL JOIN beijing_2008 ON beijing_2008.country = COALESCE(atlanta_1996.country, sydney_2000.country, athens_2004.country, average_rank.country)
FULL JOIN london_2012 ON london_2012.country = COALESCE(atlanta_1996.country, sydney_2000.country, athens_2004.country, beijing_2008.country, average_rank.country)
FULL JOIN rio_2016 ON rio_2016.country = COALESCE(atlanta_1996.country, sydney_2000.country, athens_2004.country, beijing_2008.country, london_2012.country, average_rank.country)) AS country_all;

CREATE TABLE oly_rank_and_data AS 
SELECT all_olympics.country, 
tokyo_2020.rank, 
rio_2016.rank,
london_2012.rank,
beijing_2008.rank,
athens_2004.rank, 
sydney_2000.rank, 
atlanta_1996.rank,
FROM all_olympics
LEFT JOIN tokyo_2020 ON all_olympics.country = tokyo_2020.country
LEFT JOIN rio_2016 ON all_olympics.country = rio_2016.country
LEFT JOIN london_2012 ON all_olympics.country = london_2012.country
LEFT JOIN beijing_2008 ON all_olympics.country = beijing_2008.country
LEFT JOIN athens_2004 ON all_olympics.country = athens_2004.country
LEFT JOIN sydney_2000 ON all_olympics.country = sydney_2000.country
LEFT JOIN atlanta_1996 ON all_olympics.country = atlanta_1996.country;