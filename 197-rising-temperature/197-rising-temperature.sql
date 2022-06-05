# Write your MySQL query statement below

SELECT A.id as Id
FROM Weather A, Weather B
WHERE datediff (A.recordDate, B.recordDate) = 1
AND A.temperature > B.temperature