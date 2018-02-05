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

## RIGHT JOIN

RIGHT JOIN 一般被译作右连接，也写作 RIGHT OUTER JOIN

右连接查询会返回右表（表 B）中所有记录，不管左表（表 A）中有没有关联的数据。在左表中找到的关联数据列也会被一起返回。

>示例查询

```bash
SELECT A.PK AS A_PK, B.PK AS B_PK,
       A.Value AS A_Value, B.Value AS B_Value
FROM Table_A A
RIGHT JOIN Table_B B
ON A.PK = B.PK;
```

>查询结果

```bash
+------+------+---------+---------+
| A_PK | B_PK | A_Value | B_Value |
+------+------+---------+---------+
|    1 |    1 | both ab | both ba |
| NULL |    3 | NULL    | only b  |
+------+------+---------+---------+
2 rows in set (0.00 sec)
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo61a4eo0nj20ia0a23zz.jpg)

## FULL OUTER JOIN

FULL OUTER JOIN 一般被译作外连接、全连接，实际查询语句中可以写作 FULL OUTER JOIN 或 FULL JOIN。外连接查询能返回左右表里的所有记录，其中左右表里能关联起来的记录被连接后返回。

```bash
mysql> SELECT *
    -> FROM Table_A
    -> LEFT JOIN Table_B
    -> ON Table_A.PK = Table_B.PK
    -> UNION ALL
    -> SELECT *
    -> FROM Table_A
    -> RIGHT JOIN Table_B
    -> ON Table_A.PK = Table_B.PK
    -> WHERE Table_A.PK IS NULL;
+------+---------+------+---------+
| PK   | Value   | PK   | Value   |
+------+---------+------+---------+
|    1 | both ab |    1 | both ba |
|    2 | only a  | NULL | NULL    |
| NULL | NULL    |    3 | only b  |
+------+---------+------+---------+
3 rows in set (0.00 sec)
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo619f8wyzj20la0aemyu.jpg)

## LEFT JOIN EXCLUDING INNER JOIN

返回左表有但右表没有关联数据的记录集

>示例查询

```bash
SELECT A.PK AS A_PK, B.PK AS B_PK,
       A.Value AS A_Value, B.Value AS B_Value
FROM Table_A A
LEFT JOIN Table_B B
ON A.PK = B.PK
WHERE B.PK IS NULL;
```

>查询结果

```bash
+------+------+---------+---------+
| A_PK | B_PK | A_Value | B_Value |
+------+------+---------+---------+
|    2 | NULL | only a  | NULL    |
+------+------+---------+---------+
1 row in set (0.01 sec)
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo61bqwdw1j20ge09mmyj.jpg)

## RIGHT JOIN EXCLUDING INNER JOIN

返回右表有但左表没有关联数据的记录集

>示例查询

```bash
SELECT A.PK AS A_PK, B.PK AS B_PK,
       A.Value AS A_Value, B.Value AS B_Value
FROM Table_A A
RIGHT JOIN Table_B B
ON A.PK = B.PK
WHERE A.PK IS NULL;
```

>查询结果

```bash
+------+------+---------+---------+
| A_PK | B_PK | A_Value | B_Value |
+------+------+---------+---------+
| NULL |    3 | NULL    | only b  |
+------+------+---------+---------+
1 row in set (0.00 sec)
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo61c98xb9j20h209gdh7.jpg)
