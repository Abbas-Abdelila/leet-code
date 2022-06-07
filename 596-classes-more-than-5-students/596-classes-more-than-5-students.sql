# Write your MySQL query statement below

SELECT c.class FROM Courses c
GROUP BY c.class 
Having count(c.student)>=5