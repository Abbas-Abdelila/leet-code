# Write your MySQL query statement below

SELECT score, dense_rank() over (order by score desc) as "rank"
From Scores 
order by score desc