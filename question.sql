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
