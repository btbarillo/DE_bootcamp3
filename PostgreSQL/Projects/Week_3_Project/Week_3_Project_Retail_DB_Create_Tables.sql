-- 1. Create Categories Table
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- 2. Create Suppliers Table
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(150) NOT NULL,
    contact_email VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);

-- 3. Create Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category_id INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- 4. Create Product_Suppliers Junction Table
CREATE TABLE product_suppliers (
    product_id INT NOT NULL,
    supplier_id INT NOT NULL,
    supply_cost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (product_id, supplier_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);

-- 1. Insert Categories
INSERT INTO categories (category_id, category_name, description) VALUES
(1, 'Electronics', 'Gadgets, devices, and electronic accessories'),
(2, 'Apparel', 'Clothing, footwear, and wearable accessories'),
(3, 'Home & Kitchen', 'Furniture, cookware, and home appliances');

-- 2. Insert Suppliers
INSERT INTO suppliers (supplier_id, supplier_name, contact_email, phone) VALUES
(10, 'TechSupply Co.', 'sales@techsupply.com', '555-0192'),
(20, 'Global Apparel Ltd.', 'orders@globalapparel.com', '555-0143'),
(30, 'HomeGoods Wholesale', 'contact@homegoods.com', '555-0188');

-- 3. Insert Products
INSERT INTO products (product_id, product_name, category_id, unit_price, stock_quantity) VALUES
(101, 'Wireless Headphones', 1, 99.99, 150),
(102, 'Smart Watch', 1, 199.50, 45),
(103, 'Cotton T-Shirt', 2, 19.99, 300),
(104, 'Denim Jeans', 2, 49.99, 120),
(105, 'Coffee Maker', 3, 79.00, 80);

-- 4. Insert Product_Suppliers (Junction Data)
INSERT INTO product_suppliers (product_id, supplier_id, supply_cost) VALUES
(101, 10, 55.00), -- Wireless Headphones supplied by TechSupply
(102, 10, 120.00), -- Smart Watch supplied by TechSupply
(103, 20, 8.50),   -- Cotton T-Shirt supplied by Global Apparel
(104, 20, 22.00),  -- Denim Jeans supplied by Global Apparel
(105, 30, 40.00),  -- Coffee Maker supplied by HomeGoods
(101, 30, 58.00);  -- Wireless Headphones ALSO supplied by HomeGoods


-- 1. New Categories (IDs 4 and 5)
INSERT INTO categories (category_id, category_name, description) VALUES
(4, 'Books & Stationery', 'Paper goods, books, and office supplies'),
(5, 'Sports & Outdoors', 'Fitness gear, outdoor equipment, and activewear');

-- 2. New Suppliers (IDs 40 and 50)
INSERT INTO suppliers (supplier_id, supplier_name, contact_email, phone) VALUES
(40, 'Apex Logistics', 'info@apexlogistics.com', '555-0199'),
(50, 'Vanguard Imports', 'support@vanguard.com', '555-0211');

-- 3. New Products (IDs 106, 107, 108)
INSERT INTO products (product_id, product_name, category_id, unit_price, stock_quantity) VALUES
(106, 'Bluetooth Speaker', 1, 45.00, 60),
(107, 'Ergonomic Desk Chair', 3, 249.99, 25),
(108, 'Fitness Tracker', 1, 89.99, 10);

-- 4. New Product-Supplier Link (Product 103 -> Supplier 10)
INSERT INTO product_suppliers (product_id, supplier_id, supply_cost) VALUES
(103, 10, 9.00);