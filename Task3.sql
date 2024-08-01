CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATETIME,
    status VARCHAR(50)
);

CREATE TABLE inventory (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT
);

CREATE TABLE inventory_updates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT,
    update_time DATETIME
);

INSERT INTO inventory (product_name, quantity) VALUES 
('Product A', 100),
('Product B', 200);

INSERT INTO orders (customer_id, product_id, quantity, order_date, status) VALUES 
(1, 1, 2, '2024-08-01 10:00:00', 'Pending');

SELECT * FROM orders WHERE order_id = order_id;

SELECT * FROM inventory WHERE product_id = product_id;

SELECT * FROM inventory_updates WHERE product_id = product_id ORDER BY update_time DESC;

SELECT 
    o.order_id, 
    o.product_id, 
    o.quantity AS ordered_quantity, 
    i.quantity AS inventory_quantity 
FROM 
    orders o 
JOIN 
    inventory i ON o.product_id = i.product_id 
WHERE 
    o.order_id = order_id;







