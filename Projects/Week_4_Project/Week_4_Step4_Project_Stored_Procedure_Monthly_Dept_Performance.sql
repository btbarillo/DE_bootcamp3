create or replace procedure Monthly_Dept_Performance(
    p_year INT, 
    p_month INT
)
language plpgsql
as $$
begin
-- Step 1: Idempotency (Delete old records for p_year and p_month)
    delete
from
	monthly_department_performance
where
	year_num = p_year
	and month_num = p_month;
-- Step 2: Insert transformed data
	insert
	into
	monthly_department_performance (
    year_num,
	month_num,
	department_id,
	department_name,
	total_visits,
	completed_visits,
	cancelled_or_noshow_visits,
	avg_wait_time_minutes,
	total_revenue,
	prev_month_revenue,
	ytd_revenue,
	department_revenue_rank,
	mom_revenue_growth_pct
)
   with cte_base_monthly as 
(
	select
		dd2.calendar_year ,
		dd2.calendar_month,
		dd.department_code ,
		dd.department_name,
		count(visit_id) as total_visits,
		SUM(case when fpv.visit_status ilike 'completed' then 1 else 0 end) as completed_visits,
		SUM(case when fpv.visit_status ilike 'No-Show' or fpv.visit_status ilike 'Walkout / Cancelled' then 1 else 0 end) as cancelled_or_noshow_visits,
		round(avg(fpv.wait_time_mins) , 2) as avg_wait_time_minutes,
		SUM (consultation_fee + lab_test_fees) as total_revenue
	from
		fact_patient_visits fpv
	join dim_department dd 
on
		fpv.department_key = dd.department_key
	join dim_date dd2 
on
		fpv.visit_date_key = dd2.date_key
	group by
		dd2.calendar_year,
		dd2.calendar_month,
		dd.department_code,
		dd.department_name
),
	cte_window_metrics as 
(
	select
		*,
		lag(total_revenue) over (partition by department_name
	order by
		calendar_year,
		calendar_month) as prev_month_revenue,
		sum(total_revenue) over (partition by department_name,
		calendar_year
	order by
		calendar_month ) as ytd_revenue,
		dense_rank() over (partition by calendar_year,
		calendar_month
	order by
		total_revenue desc) as department_revenue_rank
	from
		cte_base_monthly 
),
	cte_final_calculations as 
(
	select
		*,
		case
			when prev_month_revenue is null
				or prev_month_revenue = 0 then null
				else round(((total_revenue - prev_month_revenue) / prev_month_revenue) * 100, 2)
			end as mom_revenue_growth_pct
		from
			cte_window_metrics
)
select
	calendar_year,
	calendar_month,
	department_code,
	department_name,
	total_visits,
	completed_visits,
	cancelled_or_noshow_visits,
	avg_wait_time_minutes,
	total_revenue,
	prev_month_revenue,
	ytd_revenue,
	department_revenue_rank,
	mom_revenue_growth_pct
from
	cte_final_calculations
where
	calendar_year = p_year
	and calendar_month = p_month;
end;

$$;