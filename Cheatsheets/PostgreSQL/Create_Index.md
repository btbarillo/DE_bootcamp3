# CREATE INDEX — SQL Cheatsheet

## What It Does
Creates a fast lookup data structure (B-Tree) that allows the database engine to locate specific rows instantly without reading the entire table (**prevents Full Table / Sequential Scans**).

## Key Benefits
* **Accelerates Data Retrieval:** Dramatically reduces query execution time.
* **Optimizes Critical Clauses:** Speeds up `WHERE` filtering, `JOIN` conditions, and `ORDER BY` / `GROUP BY` operations.

## When to Use
* **Large Tables:** Tables with tens of thousands to millions of rows.
* **High-Frequency Columns:** Columns constantly used in `WHERE`, `ON` (joins), or `ORDER BY`.
* **High Cardinality:** Columns with many unique values (e.g., `user_id`, `order_date`, `email`).

## When to Avoid (Trade-offs)
* **Small Tables:** Full table scan is already fast; indexes add unnecessary overhead.
* **Heavy Write Workloads:** Slows down `INSERT`, `UPDATE`, and `DELETE` queries because the index must be rebuilt on every write.
* **Low Cardinality:** Columns with very few unique values (e.g., `is_active`, `gender`).

## Syntax Quick Reference

```sql
-- Single-Column Index
CREATE INDEX idx_table_column 
ON table_name (column_name);

-- Composite Index (Multi-Column)
CREATE INDEX idx_table_col1_col2 
ON table_name (column_1, column_2);

-- Drop Index
DROP INDEX idx_table_column;