# Write your MySQL query statement below

SELECT e1.name as Employee
FROM EMPLOYEE e1, EMPLOYEE e2
WHERE e1.managerId = e2.id
AND e1.salary > e2.salary