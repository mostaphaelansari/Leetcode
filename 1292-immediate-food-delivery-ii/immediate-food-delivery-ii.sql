WITH FirstOrders AS (
    SELECT 
        customer_id,
        MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
),
ClassifiedOrders AS (
    SELECT 
        f.customer_id,
        CASE 
            WHEN d.order_date = d.customer_pref_delivery_date THEN 'immediate'
            ELSE 'scheduled'
        END AS type_delivery
    FROM FirstOrders f
    JOIN Delivery d
    ON f.customer_id = d.customer_id AND f.first_order_date = d.order_date
),
TypeCounts AS (
    SELECT 
        type_delivery,
        COUNT(*) AS count_delivery
    FROM ClassifiedOrders
    GROUP BY type_delivery
)
SELECT 
    ROUND(
        (SELECT count_delivery FROM TypeCounts WHERE type_delivery = 'immediate') * 100.0 /
        (SELECT SUM(count_delivery) FROM TypeCounts),
        2
    ) AS immediate_percentage;
