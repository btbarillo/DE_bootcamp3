SELECT c.customer_id, c.customer_name , o.order_date
FROM orders o
inner JOIN customers c
on o.customer_id = c.customer_id;
