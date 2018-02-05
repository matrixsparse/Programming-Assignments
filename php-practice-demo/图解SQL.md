# 图解SQL

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo60wo3lt2j214y0uaahg.jpg)

## INNER JOIN

INNER JOIN 一般被译作内连接。内连接查询能将左表（表 A）和右表（表 B）中能关联起来的数据连接后返回

>示例查询

```bash
SELECT A.PK AS A_PK, B.PK AS B_PK,
       A.Value AS A_Value, B.Value AS B_Value
FROM Table_A A
INNER JOIN Table_B B
ON A.PK = B.PK;
```

>查询结果

```bash
+------+------+---------+---------+
| A_PK | B_PK | A_Value | B_Value |
+------+------+---------+---------+
|    1 |    1 | both ab | both ab |
+------+------+---------+---------+
1 row in set (0.00 sec)
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fo6163xn0nj20fa0am3zp.jpg)

## LEFT JOIN

LEFT JOIN 一般被译作左连接，也写作 LEFT OUTER JOIN

左连接查询会返回左表（表 A）中所有记录，不管右表（表 B）中有没有关联的数据。在右表中找到的关联数据列也会被一起返回

>示例查询

```bash
SELECT A.PK AS A_PK, B.PK AS B_PK,
       A.Value AS A_Value, B.Value AS B_Value
FROM Table_A A
LEFT JOIN Table_B B
ON A.PK = B.PK;
```

>查询结果

```bash
+------+------+---------+---------+
| A_PK | B_PK | A_Value | B_Value |
+------+------+---------+---------+
|    1 |    1 | both ab | both ba |
|    2 | NULL | only a  | NULL    |
+------+------+---------+---------+
2 rows in set (0.00 sec)
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo615goac2j20i009wdha.jpg)
