-- script that lists all score and name records
SELECT `score`,`name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY `score` DESC
