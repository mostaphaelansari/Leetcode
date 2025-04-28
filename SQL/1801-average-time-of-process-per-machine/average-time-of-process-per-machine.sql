With ProcessTimes as(
    select machine_id,
           process_id,
           MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time,
           MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time
    From Activity
    group by machine_id,process_id
)
SELECT machine_id, 
       ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM ProcessTimes
GROUP BY machine_id;