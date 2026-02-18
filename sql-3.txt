SELECT Group_Name, COLLECTOR_CODE, Incentive
FROM (
    SELECT *,
           RANK() OVER(PARTITION BY Group_Name ORDER BY Incentive DESC) as rnk
    FROM ( [Query จากข้อ 2] )
) t
WHERE rnk = 1;