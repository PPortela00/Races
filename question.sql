/*---------------------------5 Questions ---------------------------*/
/* 1) Who run the fastest 10K race ever (name, birthdate, time) */
/* 2) What 10K race had the fastest average time (event, event date)? */
/* 3) What teams had more than 3 participants in the 2016 maratona (team)? */
/* 4) What are the 5 runners with more kilometers in total (name, birthdate, kms)? */
/* 5) What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)? */


/* 1) Who run the fastest 10K race ever (name, birthdate, time) */
SELECT name, b_date, MIN(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
                    JOIN runner ON runner_id = r_id
WHERE distance.distance = 10
GROUP BY r_id
HAVING MIN(o_time) <= ALL (SELECT MIN(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
                    JOIN runner ON runner_id = r_id
WHERE distance.distance = 10
GROUP BY r_id)



/* 2) What 10K race had the fastest average time (event, event date)? */
SELECT event, e_year
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
WHERE distance.distance = 10
GROUP BY e_id
HAVING AVG(o_time) <= ALL (SELECT AVG(o_time)
FROM classification JOIN event ON event_id = e_id
                    JOIN distance ON event.distance = d_id
WHERE distance.distance = 10
GROUP BY e_id)



/* 3) What teams had more than 3 participants in the 2016 maratona (team)? */
SELECT team
FROM classification JOIN event ON event_id = e_id
WHERE e_year = 2016 AND event.event = 'maratona' AND team <> 'nan'
GROUP BY team
HAVING COUNT (*) > 3




/* 4) What are the 5 runners with more kilometers in total (name, birthdate, kms)? */
SELECT name, b_date, SUM(distance.distance) AS total_kms
FROM classification JOIN runner ON runner_id = r_id
                    JOIN event ON event_id = e_id
                    JOIN distance on event.distance = d_id
GROUP BY r_id
HAVING SUM(distance.distance) IN (
SELECT SUM(distance.distance)
FROM classification JOIN runner ON runner_id = r_id
                    JOIN event ON event_id = e_id
                    JOIN distance on event.distance = d_id
GROUP BY r_id
ORDER BY SUM(distance.distance) DESC
LIMIT 5
)
ORDER BY SUM(distance.distance) DESC





/* 5) What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)? */
SELECT name, b_date, GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) AS improvement
FROM (

SELECT name, b_date, o_time_2012 - o_time_2013 AS dif_1213, o_time_2013 - o_time_2014 AS dif_1314, o_time_2014 - o_time_2015 AS dif_1415, o_time_2015 - o_time_2016 AS dif_1516
FROM (SELECT name, b_date, o_time AS o_time_2012, e_year
      FROM classification JOIN event ON event_id = e_id
                    JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2012) AS year_2012 
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2013, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2013) AS year_2013 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2014, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2014) AS year_2014 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2015, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2015) AS year_2015 USING(name, b_date)
FULL OUTER JOIN (SELECT name, b_date, o_time AS o_time_2016, e_year
      FROM classification JOIN event ON event_id = e_id
                          JOIN runner ON runner_id = r_id
      WHERE event.event = 'maratona'
      GROUP BY r_id, o_time, e_year
      HAVING e_year = 2016) AS year_2016 USING(name, b_date)

) AS differences

GROUP BY name, b_date, improvement

HAVING GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) IS NOT NULL

ORDER BY GREATEST(dif_1213, dif_1314, dif_1415, dif_1516) DESC

LIMIT 1




/* 6) How many runners have more than 50 years old? */
/* 7) How many runners are in each age class? */
/* 8) Which runner has more 1st places? */
/* 9) What are the events with less then 42km distance? */
