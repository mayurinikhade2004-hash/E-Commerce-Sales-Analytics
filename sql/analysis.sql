-- E-Commerce Sales Analytics
-- SQL Business Analysis

-- 1. Total Revenue
SELECT ROUND(SUM(revenue), 2) AS total_revenue
FROM online_retail;

-- 2. Total Orders
SELECT COUNT(DISTINCT invoice_no) AS total_orders
FROM online_retail;

-- 3. Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM online_retail;

-- 4. Average Order Value
SELECT ROUND(
    SUM(revenue) / COUNT(DISTINCT invoice_no),
    2
) AS average_order_value
FROM online_retail;
-- 5. Monthly Revenue
SELECT
    TO_CHAR(invoice_date, 'YYYY-MM') AS year_month,
    ROUND(SUM(revenue), 2) AS monthly_revenue
FROM online_retail
GROUP BY year_month
ORDER BY year_month;


-- 6. Top 10 Products by Revenue
SELECT
    description,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM online_retail
GROUP BY description
ORDER BY total_revenue DESC
LIMIT 10;


-- 7. Top 10 Countries by Revenue
SELECT
    country,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM online_retail
GROUP BY country
ORDER BY total_revenue DESC
LIMIT 10;


-- 8. Top 10 Customers by Revenue
SELECT
    customer_id,
    ROUND(SUM(revenue), 2) AS total_revenue,
    RANK() OVER (
        ORDER BY SUM(revenue) DESC
    ) AS customer_rank
FROM online_retail
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;


-- 9. Customer Segmentation
WITH customer_revenue AS (
    SELECT
        customer_id,
        SUM(revenue) AS total_revenue
    FROM online_retail
    GROUP BY customer_id
)
SELECT
    CASE
        WHEN total_revenue < 5000 THEN 'Low Value'
        WHEN total_revenue < 10000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS customer_segment,
    COUNT(*) AS customer_count,
    ROUND(SUM(total_revenue), 2) AS segment_revenue
FROM customer_revenue
GROUP BY customer_segment
ORDER BY segment_revenue DESC;