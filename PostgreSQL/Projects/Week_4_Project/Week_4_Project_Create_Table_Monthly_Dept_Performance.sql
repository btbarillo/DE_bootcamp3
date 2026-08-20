create table Monthly_Department_Performance
(
    summary_id SERIAL primary key, 
    year_num INT,
    month_num INT,
    department_id VARCHAR(15), 
    department_name VARCHAR(100),
-- Operational Counts
total_visits INT,
    completed_visits INT,
    cancelled_or_noshow_visits INT,
-- Financials & Averages
avg_wait_time_minutes numeric(10, 2),
    total_revenue numeric(12, 2),
-- Advanced Window Metrics
prev_month_revenue numeric(12, 2),
    mom_revenue_growth_pct numeric(8, 2),
    ytd_revenue numeric(14, 2),
    department_revenue_rank INT,
-- Audit Metadata
created_at TIMESTAMP default CURRENT_TIMESTAMP
);