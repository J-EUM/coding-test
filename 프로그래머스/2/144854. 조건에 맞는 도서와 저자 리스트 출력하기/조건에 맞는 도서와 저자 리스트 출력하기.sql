-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK b
    JOIN AUTHOR a USING(AUTHOR_ID)
WHERE b.CATEGORY = '경제'
ORDER BY 3