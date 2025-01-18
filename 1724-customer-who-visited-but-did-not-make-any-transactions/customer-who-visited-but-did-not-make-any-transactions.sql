select V.customer_id ,
        Count(V.visit_id )
    AS count_no_trans
From Visits as V
Left Join Transactions as T 
On V.visit_id = T.visit_id 
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;


