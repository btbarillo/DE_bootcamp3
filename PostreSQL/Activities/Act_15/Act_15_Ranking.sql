CREATE TABLE salesman_revenue (
    salesman_id INT PRIMARY KEY,
    salesman_name VARCHAR(100) NOT NULL,
    total_revenue DECIMAL(10, 2) NOT NULL
);

INSERT INTO salesman_revenue (salesman_id, salesman_name, total_revenue) VALUES
(1, 'Marcus Vance', 125000.00),
(2, 'Sarah Jenkins', 98000.50),
(3, 'David Chen', 142000.00),
(4, 'Elena Rostova', 89000.25),
(5, 'James Wilson', 165000.00),
(6, 'Priya Patel', 110000.75),
(7, 'Carlos Gomez', 75000.00),
(8, 'Chloe Dubois', 134000.00),
(9, 'Liam O''Connor', 62000.50),
(10, 'Hannah Abbott', 155000.00),
(11, 'Alex Rivera', 118000.00),
(12, 'Nina Kowalski', 105000.25),
(13, 'Brian Taylor', 148000.00),
(14, 'Samantha Reed', 51000.00),
(15, 'Derek Miller', 129000.50);



--- Use ROW_NUMBER() to assign a top 10 ranking to salesmen based on their total revenue.


WITH ranking_top_10_salesman AS (
    SELECT 
        salesman_name, 
        total_revenue,
        ROW_NUMBER() OVER (ORDER BY total_revenue DESC) AS ranking_salesman
    FROM salesman_revenue
)
SELECT * 
FROM ranking_top_10_salesman
WHERE ranking_salesman <= 10;

