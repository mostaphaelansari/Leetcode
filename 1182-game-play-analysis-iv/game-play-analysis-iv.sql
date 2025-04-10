# Write your MySQL query statement below
SELECT ROUND(
    (SELECT COUNT(DISTINCT t1.player_id) * 1.0
     FROM (
         SELECT player_id, MIN(event_date) AS first_login 
         FROM Activity 
         GROUP BY player_id
     ) t1
     JOIN Activity t2 
     ON t1.player_id = t2.player_id 
     AND t2.event_date = DATE_ADD(t1.first_login, INTERVAL 1 DAY)
    ) 
    / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity)
, 2) AS fraction;