select p.product_name,s.year , s.price from Product AS p
Right join Sales AS s
on s.product_id = p.product_id ;