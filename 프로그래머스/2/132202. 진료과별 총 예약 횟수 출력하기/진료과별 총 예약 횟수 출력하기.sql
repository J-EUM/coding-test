-- 코드를 입력하세요
SELECT MCDP_CD AS "진료과코드", 
        COUNT(1) AS "5월예약건수"
FROM APPOINTMENT
WHERE LEFT(APNT_YMD, 7) = "2022-05"
--        AND APNT_CNCL_YN != "Y"
GROUP BY MCDP_CD
ORDER BY 2, 1;