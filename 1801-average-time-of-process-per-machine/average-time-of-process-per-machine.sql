-- WITH Processing_time AS (
--     SELECT 
--         machine_id,
--         process_id,
--         MAX(CASE WHEN activity_type = 'end' THEN timestamp END) -
--         MAX(CASE WHEN activity_type = 'start' THEN timestamp END) / 2 AS processing_time
--     FROM Activity
--     GROUP BY machine_id, process_id
-- )
-- SELECT machine_id , processing_time
-- FROM Processing_time
-- ORDER BY machine_id, process_id DESC;
SELECT machine_id, 
       ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
    SELECT machine_id, 
           process_id, 
           MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time,
           MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time
    FROM Activity
    GROUP BY machine_id, process_id
) AS ProcessTimes
GROUP BY machine_id;
