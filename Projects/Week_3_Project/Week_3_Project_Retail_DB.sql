-- Determine out which product categories have the most stock in store and see their average prices, sorted from highest inventory to lowest.

select c.category_id, c.category_name, 
sum(p.stock_quantity ) as total_number_items,
round(avg(p.unit_price ),2) as avg_retail_price
from categories c
join products p
on c.category_id = p.category_id
group by c.category_name, c.category_id
order by total_number_items DESC;


-- Calculate the total capital tied up in wholesale inventory for each supplier by multiplying item stock quantities by their respective unit supply costs.

select s.supplier_id, s.supplier_name,
sum(p.stock_quantity*ps.supply_cost ) as supply_cost_per_supplier
from suppliers s
join product_suppliers ps
on s.supplier_id = ps.supplier_id
join products p
on ps.product_id = p.product_id
group by s.supplier_name, s.supplier_id
order by supply_cost_per_supplier DESC; 


-- Determine items bought from multiple suppliers to know which products have backup vendors if one supplier fails


select p.product_id, p.product_name, 
count(ps.supplier_id ) as count_per_supplier
from products p
join product_suppliers ps 
on p.product_id = ps.product_id
group by p.product_id
having count(ps.supplier_id ) > 1;


-- Identify products that are not linked to any supplier to find inventory items at risk of stockouts if orders are placed.
select p.product_name, p.stock_quantity
from products p
left join product_suppliers ps 
on p.product_id =ps.product_id 
where ps.product_id is NULL


-- Count products supplied per vendor, including those with zero items, to flag inactive suppliers for procurement review.

select s.supplier_id, s.supplier_name, count(ps.product_id) as count_per_product
from suppliers s
left join product_suppliers ps  
on s.supplier_id = ps.supplier_id 
group by s.supplier_name, s.supplier_id 
order by count_per_product ASC


-- Measure total product count per category, including empty categories, to highlight gaps where new inventory needs to be added.

SELECT c.category_id, c.category_name, 
    COUNT(p.product_id) AS total_products
FROM categories c 
LEFT JOIN products p 
    ON c.category_id = p.category_id
GROUP BY c.category_id, c.category_name 
ORDER BY total_products ASC;






