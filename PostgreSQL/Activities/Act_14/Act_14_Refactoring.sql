-- 1. Create the Customers table

CREATE TABLE customers (

customer_id INT PRIMARY KEY,

customer_name VARCHAR(100) NOT NULL,

email VARCHAR(100)

);

-- 2. Create the Orders table (referencing customers)

CREATE TABLE orders (

order_id INT PRIMARY KEY,

customer_id INT NOT NULL,

store_location VARCHAR(100) NOT NULL,

amount DECIMAL(10, 2) NOT NULL,

order_date DATE NOT NULL,

FOREIGN KEY (customer_id) REFERENCES customers(customer_id)

);

-- Insert all customers
INSERT INTO customers (customer_id, customer_name, email) VALUES
(101, 'Alice Johnson', 'alice@example.com'),
(102, 'Bob Smith', 'bob@example.com'),
(103, 'Charlie Brown', 'charlie@example.com'),
(104, 'Diana Prince', 'diana@example.com'),
(105, 'Evan Wright', 'evan@example.com');

-- Insert all orders
INSERT INTO orders (order_id, customer_id, store_location, amount, order_date) VALUES
(1, 101, 'Downtown', 150.50, '2026-01-10'),
(2, 102, 'Uptown', 200.00, '2026-01-11'),
(3, 101, 'Downtown', 320.25, '2026-01-12'),
(4, 103, 'Westside', 85.00, '2026-01-12'),
(5, 102, 'Uptown', 145.75, '2026-01-13'),
(6, 101, 'Westside', 210.00, '2026-01-14'),
(7, 104, 'Downtown', 650.00, '2026-01-15'),
(8, 105, 'Uptown', 520.75, '2026-01-16'),
(9, 101, 'Westside', 890.50, '2026-01-17');




-- Write a CTE that finds all orders > $500, then query from that CTE.

WITH orders_more_500 AS (
    SELECT order_id, customer_id, store_location, amount, order_date
    FROM orders
    WHERE amount > 500
)
SELECT * 
FROM orders_more_500
ORDER BY amount DESC;
