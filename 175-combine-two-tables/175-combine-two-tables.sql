# Write your MySQL query statement below

SELECT firstName, LastName, city, state
FROM Person p
LEFT JOIN Address ad
    ON p.personId = ad.personId