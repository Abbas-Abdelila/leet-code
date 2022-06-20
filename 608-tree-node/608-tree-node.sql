# Write your MySQL query statement below

SELECT 
    tr.id, 
    IF(ISNULL(tr.p_id), "Root",
    IF(tr.id in (SELECT p_id FROM TREE ), "Inner","Leaf")) as type
FROM Tree tr
ORDER BY tr.id