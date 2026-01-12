USE PRACTICE;
CREATE TABLE IF NOT EXISTS ORDERS(O_ID INT PRIMARY KEY, C_NAME VARCHAR(10),PRODUCT VARCHAR(15),QUANTITY INT,PRICE INT);
INSERT INTO ORDERS (O_ID, C_NAME, PRODUCT, QUANTITY, PRICE) 
VALUES
(1001, 'Jitendra', 'Laptop', 1, 12000),
(1002, 'Mustafa', 'Smartphone', 2, 10000),
(1003, 'Dhwani', 'Headphone', 1, 1500),
(1004, 'Rahul', 'Smartwatch', 3, 7000),
(1005, 'Ayesha', 'Laptop', 6, 12000),
(1006, 'Zara', 'Tablet', 4, 8000),
(1007, 'Sohan', 'Smartphone', 7, 11000),
(1008, 'Tanu', 'Headphone', 5, 1500),
(1009, 'Ravi', 'Smartwatch', 2, 7000),
(1010, 'Pooja', 'Smartphone', NULL, 10000);
SELECT * FROM ORDERS WHERE SUM(QUANTITY)>5;
SELECT *,QUANTITY*PRICE AS TOTAL_PRICE FROM ORDERS ORDER BY TOTAL_PRICE  DESC;
SELECT DISTINCT(C_NAME) FROM ORDERS;
SELECT SUM(PRICE) FROM ORDERS WHERE QUANTITY IS NULL;
Select c_name, sum(quantity) as total_quantity from orders group by c_name;
Select * from orders where product like '%phone%';
Select o_id, c_name, product, quantity, price from orders where price between 1500 and 12000;
Select max(price) from orders;
