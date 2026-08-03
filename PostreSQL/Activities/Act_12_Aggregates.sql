SELECT store_location, sum(amount) AS total_amount
FROM orders
GROUP BY store_location
order by total_amount;

