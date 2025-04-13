-- 코드를 작성해주세요
WITH t AS (
    SELECT PARENT_ID, COUNT(1) AS cc
    FROM ECOLI_DATA
    GROUP BY 1
    )
SELECT 
    ed.ID, 
    IFNULL(t.cc, 0) AS CHILD_COUNT
FROM ECOLI_DATA ed 
    LEFT JOIN t
        ON ed.ID = t.PARENT_ID
ORDER BY 1
