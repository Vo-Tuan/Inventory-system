CREATE table inventory(
ProductID INT PRIMARY KEY,
ProductName VarChar(80),
Quantity INT,
Price INT,
log DATETIME
);

SELECT
ProductID,
ProductName,
Quanitity,
Price,
CASE
	WHEN Quantity > 1 THEN Quantity * Price
	ELSE Price
END AS SumPrice
FROM inventory;
