# Write your MySQL query statement below

SELECT p.firstName, p.LastName, ad.city, ad.state
FROM Person p
LEFT JOIN Address ad
    ON p.personId = ad.personId