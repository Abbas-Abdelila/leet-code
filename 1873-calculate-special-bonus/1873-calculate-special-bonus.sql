# Write your MySQL query statement below
SELECT employee_id, IF(employee_id%2 = 1 AND name not like "M%",salary, 0) as bonus
FROM Employees
Order by employee_id