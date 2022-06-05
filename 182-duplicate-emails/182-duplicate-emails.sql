# Write your MySQL query statement below

SELECT email as Email 
FROM Person
group by email
Having count(*) > 1