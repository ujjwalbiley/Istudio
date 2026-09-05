-- DROP DATABASE data_analytics;
CREATE DATABASE data_analytics;
USE data_analytics;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    salary INT,
    hire_date DATE
);

INSERT INTO employees VALUES
(1, 'Aarav', 'Electronics', 55000, '2022-01-10'),
(2, 'Bhavya', 'Fashion', 48000, '2021-05-15'),
(3, 'Chirag', 'Electronics', 52000, '2023-03-20'),
(4, 'Diya', 'Fashion', 72000, '2020-07-01'),
(5, 'Eshan', 'Electronics', 60000, '2022-11-12'),
(6, 'Farah', 'Grocery', 45000, '2023-08-05'),
(7, 'Gaurav', 'Fashion', 85000, '2019-04-22'),
(8, 'Hina', 'Grocery', 42000, '2024-01-18'),
(9, 'Ishan', 'Grocery', 55000, '2022-09-10'),
(10, 'Jiya', 'Electronics', 78000, '2020-12-01');

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    emp_id INT,
    product VARCHAR(50),
    amount INT,
    sale_date DATE
);

INSERT INTO sales VALUES
(101, 1, 'Laptop', 110000, '2025-02-03'),
(102, 2, 'Saree', 22500, '2025-02-05'),
(103, 3, 'Headphones', 15000, '2025-02-06'),
(104, 4, 'Shoes', 6600, '2025-02-07'),
(105, 5, 'Smartphone', 128000, '2025-02-09'),
(106, 1, 'Tablet', 18000, '2025-02-11'),
(107, 6, 'Rice', 1600, '2025-02-12'),
(108, 7, 'Watch', 7000, '2025-02-14'),
(109, 8, 'Oil', 2700, '2025-02-15'),
(110, 3, 'Mouse', 7192, '2025-02-18');

SELECT * FROM employees;

SELECT * FROM employees
WHERE department = 'Fashion';

SELECT * FROM employees
ORDER BY salary DESC;

SELECT name FROM employees
WHERE salary BETWEEN 50000 AND 70000;

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

SELECT e.emp_id, e.name, s.product, s.amount
FROM employees e
INNER JOIN sales s
ON e.emp_id = s.emp_id;

SELECT e.emp_id, e.name, SUM(s.amount) AS total_sales
FROM employees e
INNER JOIN sales s
ON e.emp_id = s.emp_id
GROUP BY e.emp_id, e.name;

SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

-- CRUD Opertaion
-- Insert
INSERT INTO employees
VALUES (11, 'Kavya', 'Fashion', 50000, '2025-03-01');

SELECT * FROM employees;

-- Update
UPDATE employees
SET salary = salary * 1.10
WHERE emp_id IN (6,8,9);

SELECT * FROM employees;

-- Delete
DELETE FROM employees
WHERE emp_id = 11;

SELECT * FROM employees;