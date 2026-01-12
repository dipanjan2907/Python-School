USE PRACTICE;
CREATE TABLE IF NOT EXISTS PRODUCT (PCode CHAR(3) PRIMARY KEY, PName Varchar(30), UPrice INT, Manufacturer VARCHAR(20));
INSERT INTO Product (PCode, PName, UPrice, Manufacturer) VALUES ('P01','Washing Powder',120,'Surf'), ('P02','Toothpaste', 54,'Surf');
INSERT INTO Product (PCode, PName, UPrice, Manufacturer) VALUES ('P03','Soap',25,'Lux'), ('P05','Soap', 38,'Dove'),('P06','Shampoo',245,'Dove');
SELECT PCode, PName, UPrice FROM PRODUCT ORDER BY PName DESC;
SELECT PCode, PName, UPrice FROM PRODUCT  ORDER BY PName DESC, UPrice ASC;
ALTER TABLE PRODUCT ADD DISCOUNT FLOAT;
UPDATE Product SET DISCOUNT =0;
UPDATE PRODUCT SET DISCOUNT=UPrice*0.1 WHERE UPrice>100;
UPDATE PRODUCT SET UPRICE=UPRICE+(0.12*UPrice) WHERE Manufacturer='Dove';
SELECT Manufacturer, COUNT(PName) FROM Product GROUP BY Manufacturer;
SELECT PName, avg(UPrice) FROM Product GROUP BY Pname;
SELECT DISTINCT Manufacturer FROM Product;
SELECT COUNT(DISTINCT PName) FROM Product;
 SELECT 
    PName, MAX(UPrice), MIN(UPrice)
FROM
    Product
GROUP BY PName;
SELECT * FROM PRODUCT;