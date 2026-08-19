-- Rewrite a slow query: remove SELECT *, add a WHERE filter, and identify two columns that should be indexed.

-- Before
SELECT * FROM orders o
JOIN customers c ON o.customer_id = o.customer_id;

-- Improve this query
SELECT 
    c.customer_id, 
    c.customer_name, 
    o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2026-01-01';


-- Analyze the query
EXPLAIN ANALYZE
SELECT 
    c.customer_id, 
    c.customer_name, 
    o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2026-01-01';

--- Two columns that should be indexed

CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_order_date ON orders(order_date);