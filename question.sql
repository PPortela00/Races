/*---------------------------5 Questions ---------------------------*/
/* 1) Who run the fastest 10K race ever (name, birthdate, time) */
/* 2) What 10K race had the fastest average time (event, event date)? */
/* 3) What teams had more than 3 participants in the 2016 maratona (team)? */
/* 4) What are the 5 runners with more kilometers in total (name, birthdate, kms)? */
/* 5) What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)? */


/* 1) Who run the fastest 10K race ever (name, birthdate, time) */
SELECT name, birthdate, MIN(time) FROM runner
JOIN classification ON runner.r_id = classification.runner_id
JOIN event ON classification.event_id = event.e_id
WHERE distance = 10



/* 2) What 10K race had the fastest average time (event, event date)? */
SELECT event, e_year, MIN(time)
FROM (
SELECT event, e_year, AVG(o_time) as time FROM event
JOIN classification ON event.e_id = classification.event_id
GROUP BY e_id, event
)
HAVING distance = 10




/* 3) What teams had more than 3 participants in the 2016 maratona (team)? */
SELECT team
FROM classification
JOIN event ON classification.event_id = event.e_id
WHERE e_year = 2016 AND event = "maratona"
GROUP BY team
HAVING COUNT (id_runner) > 3




/* 4) What are the 5 runners with more kilometers in total (name, birthdate, kms)? */
SELECT name, b_date, SUM(distance) as kms
FROM runner JOIN classification ON runner.r_id = classification.runner_id
JOIN event ON classification.event_id = event.e_id
ORDER BY kms desc
fetch first 5 rows only





/* 5) What was the best time improvement in two consecutive maratona races (name,birthdate, improvement)? */
