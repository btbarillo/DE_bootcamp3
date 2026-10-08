## Optimization Strategy (Partitioning & Clustering)

In BigQuery, I applied both **Partitioning** and **Clustering** on the `fact_sales` table to optimize query performance.

### 1. Partitioning: `order_date`
* **Column:** `order_date` (Daily Partitioning)
* **Why:** 
  - Most analytical queries and business reports filter sales data by date ranges (e.g., daily, monthly, or quarterly revenue).
  - By partitioning on `order_date`, BigQuery cuts back unnecessary partitions and scans only the specific dates required by the query, significantly lowering memory consumption and query cost.

### 2. Clustering: `product_id`
* **Column:** `product_id`
* **Why:** 
  - `product_id` is a high-cardinality column frequently used in `WHERE` filtering conditions and `JOIN` operations (connecting `fact_sales` with `dim_product`).
  - Clustering organizes data within each date partition based on `product_id`, allowing BigQuery to quickly locate relevant blocks when running product-level analyses (e.g., Top Selling Products, Category Performance).

---
**Summary:** Combining daily partitioning on `order_date` with clustering on `product_id` ensures maximum query speed, optimal data organization, and cost efficiency for our analytical queries.
