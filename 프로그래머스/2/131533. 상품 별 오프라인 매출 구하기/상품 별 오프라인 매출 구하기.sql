-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, 
        SUM(p.PRICE * os.SALES_AMOUNT) SALES
FROM OFFLINE_SALE os 
    JOIN PRODUCT p ON os.PRODUCT_ID = p.PRODUCT_ID
GROUP BY 1
ORDER BY 2 DESC, 1
