## Partitioning & Clustering

In BigQuery, I applied both **Partitioning** and **Clustering** on the `fact_sales` table to optimize query performance.

<img width="782" height="487" alt="image" src="https://github.com/user-attachments/assets/ea5aac63-ffcf-4bcd-99fc-6ce3c9834354" />

### 1. Partitioning: `order_date`
* **Column:** `order_date` (Daily Partitioning)
* **Why:** 
  - Most analytical queries and business reports filter sales data by date ranges (e.g., daily, monthly, or quarterly revenue).
  - By partitioning on `order_date`, BigQuery cuts back unnecessary partitions and scans only the specific dates required by the query, significantly lowering memory consumption and query cost.

### 2. Clustering: `product_id`
* **Column:** `product_id`
* **Why:** 
  - `product_id` is a high-cardinality (meaning it  has a large number of distinct values) column frequently used in `WHERE` filtering conditions and `JOIN` operations (connecting `fact_sales` with `dim_product`).
  - Clustering organizes data within each date partition based on `product_id`, allowing BigQuery to quickly locate relevant blocks when running product-level analyses (e.g., Top Selling Products, Category Performance).

---
**Summary:** Combining daily partitioning on `order_date` with clustering on `product_id` ensures maximum query speed, optimal data organization, and cost efficiency for our analytical queries.
**Note: **: The CSVs used to create tables in BigQuery to rebuild `fact_sales`, `dim_customer`, and `dim_product` as physical tables can be found [here](https://github.com/btbarillo/DE_bootcamp3/tree/master/data/raw/Week_8)
