# Write your MySQL query statement below

SELECT distinct user_id, count(*) as followers_count
FROM Followers
group by user_id
order by user_id, count(*)