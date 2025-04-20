-- 코드를 작성해주세요
WITH RECURSIVE generation_cte AS (
    -- 부모가 없는 root는 1세대
    SELECT 
        ID,
        PARENT_ID,
        1 AS generation
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 부모의 세대 + 1
    SELECT 
        ed.ID,
        ed.PARENT_ID,
        cte.generation + 1
    FROM ECOLI_DATA ed
    JOIN generation_cte cte ON ed.PARENT_ID = cte.ID
)

SELECT 
    COUNT(*) AS COUNT,
    generation AS GENERATION
FROM generation_cte gc
WHERE NOT EXISTS (
    SELECT 1
    FROM ECOLI_DATA ed2
    WHERE ed2.PARENT_ID = gc.ID
)
GROUP BY GENERATION