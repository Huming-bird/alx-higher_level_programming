-- this sccript lists the no of record with same score in a group
SELECT `score`, COUNT(*) AS `number` FROM `second_table`
GROUP BY `score` ORDER BY `number` DESC;
