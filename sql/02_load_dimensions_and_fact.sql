-- Example ELT logic from staging table curated_orders.

INSERT INTO dim_customer (customer_key, customer_id, customer_name)
SELECT ROW_NUMBER() OVER (ORDER BY customer_id),
       customer_id, MAX(customer_name)
FROM curated_orders
GROUP BY customer_id;

INSERT INTO dim_product (product_key, product_id, product_name)
SELECT ROW_NUMBER() OVER (ORDER BY product_id),
       product_id, MAX(product_name)
FROM curated_orders
GROUP BY product_id;
