
## 准备数据

>douban_movie.csv

```bash
actor_count	actors	category	cover_url	id	is_playable	is_watched	rank	rating	regions	release_date	score	title	types	url	vote_count
19	[张国荣, 张丰毅, 巩俐, 葛优, 英达, 蒋雯丽, 吴大维, 吕齐, 雷汉, 尹治, 马明威, 费振翔, 智一桐, 李春, 赵海龙, 李丹, 童弟, 沈慧芬, 黄斐]	同性	https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p1910813120.jpg	1291546	True	False	1	[9.5, 50]	[中国大陆, 香港]	1993-01-01	9.5	霸王别姬	[剧情, 爱情, 同性]	https://movie.douban.com/subject/1291546/	629403
10	[伊恩·麦克莱恩, 德里克·雅各比, 弗朗西斯·德·拉·图瓦, 伊万·瑞恩, 玛西娅·沃伦, 菲利普-沃斯, 艾琳·阿特金斯, 弗兰西斯·巴贝, 阿利斯泰尔·布拉默, 理查德·加德]	同性	https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p2360539785.jpg	26700818	False	False	2	[9.3, 50]	[英国]	2016-06-19	9.3	极品基老伴：完结篇	[喜剧, 同性]	https://movie.douban.com/subject/26700818/	13516
5	[蒂莫西·柴勒梅德, 艾米·汉莫, 迈克尔·斯图巴, 阿蜜拉·卡萨, 艾斯特·加莱尔]	同性	https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p2494250616.jpg	26799731	False	False	3	[9.3, 50]	[意大利, 法国, 巴西, 美国]	2017-01-22	9.3	请以你的名字呼唤我	[爱情, 同性]	https://movie.douban.com/subject/26799731/	739
3	[张国荣, 梁朝伟, 张震]	同性	https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p465939041.jpg	1292679	False	False	4	[8.8, 45]	[香港, 日本, 韩国]	1997-05-30	8.8	春光乍泄	[剧情, 爱情, 同性]	https://movie.douban.com/subject/1292679/	240127
5	[赵文瑄, 归亚蕾, 金素梅, 郎雄, 米切尔·利希藤斯坦]	同性	https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p2173713676.jpg	1303037	False	False	5	[8.8, 45]	[台湾, 美国]	1993-08-04	8.8	喜宴	[剧情, 喜剧, 爱情, 同性, 家庭]	https://movie.douban.com/subject/1303037/	133193
5	[西格妮·韦弗, 瑞恩·凯利, 亨利·科泽尼, 丹·巴特勒, 奥斯汀·尼可斯]	同性	https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p1662271271.jpg	3154003	False	False	6	[8.8, 45]	[美国]	2009-01-24	8.8	天佑鲍比	[剧情, 传记, 同性]	https://movie.douban.com/subject/3154003/	28065
12	[大卫·鲍伊, 汤姆·康蒂, 坂本龙一, 北野武, 杰克·汤普森, 约翰尼·大仓, 阿利斯泰尔·布朗宁, 内田裕也, 金田龙之介, 内藤刚志, 户浦六宏, 三上宽]	同性	https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p2164311201.jpg	1303535	False	False	7	[8.7, 45]	[英国, 日本]	1983-05-28	8.7	战场上的快乐圣诞	[剧情, 战争, 同性]	https://movie.douban.com/subject/1303535/	26308
```

## 读取数据

### info()查看数据有哪些字段和字段对应的数据类型

```bash
# -*- coding: utf-8 -*-

import pandas as pd

movie_pd = pd.read_csv('../resources/douban_movie.csv', header=0, sep='\t')
print(movie_pd.info())
```

>运行结果

```bash
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3688 entries, 0 to 3687
Data columns (total 16 columns):
actor_count     3688 non-null int64
actors          3688 non-null object
category        3688 non-null object
cover_url       3688 non-null object
id              3688 non-null int64
is_playable     3688 non-null bool
is_watched      3688 non-null bool
rank            3688 non-null int64
rating          3688 non-null object
regions         3688 non-null object
release_date    3688 non-null object
score           3688 non-null float64
title           3688 non-null object
types           3688 non-null object
url             3688 non-null object
vote_count      3688 non-null int64
dtypes: bool(2), float64(1), int64(4), object(9)【电影数据共有 16 列，数据类型int64、bool、float64、object】
【列名：actor_count (主演的人数)、actors (主演列表)、category (分类)、cover_url (封面图片网址)、id (电影id)、is_playable (是否可以播放)、is_watched (是否可以观看)、rank (排名)、rating (评分, 含星级)、regions (制片国家)、release_date (上映日期)、score (评分)、title (电影标题)、types (类型, 多个)、url (电影详情页网址)、vote_count (评价的人数)】
memory usage: 410.7+ KB
None
```

### describe()对数值型变量进行统计性描述

```bash
# -*- coding: utf-8 -*-

import pandas as pd

movie_pd = pd.read_csv('../resources/douban_movie.csv', header=0, sep='\t')
print('获取定量数据\n', movie_pd.describe())
```

>运行结果

```bash
获取定量数据
        actor_count            id         rank        score     vote_count
count  3688.000000  3.688000e+03  3688.000000  3688.000000    3688.000000
mean      8.418655  3.655456e+06   124.189534     8.522587   71773.012744
std       6.067463  6.095063e+06   116.329492     0.394342  119190.948797
min       0.000000  1.291543e+06     1.000000     7.300000     305.000000
25%       4.000000  1.296384e+06    36.000000     8.300000    3513.000000
50%       7.000000  1.307067e+06    87.000000     8.500000   15786.000000
75%      12.000000  2.150085e+06   177.000000     8.800000   85188.000000
max      54.000000  2.710254e+07   534.000000     9.700000  875424.000000
【列出个数、均值、方差、最小值、最大值和四分位数】
```

### head(n)/tail(n)显示数据前/后n行

```bash
# -*- coding: utf-8 -*-

import pandas as pd

movie_pd = pd.read_csv('../resources/douban_movie.csv', header=0, sep='\t')
print('获取前五行数据\n：',movie_pd.head())
# print('获取后五行数据\n：',movie_pd.tail())
```

>运行结果

```bash
获取前五行数据：
：    actor_count                                             actors category  \
0           19  [张国荣, 张丰毅, 巩俐, 葛优, 英达, 蒋雯丽, 吴大维, 吕齐, 雷汉, 尹治, 马...       同性   
1           10  [伊恩·麦克莱恩, 德里克·雅各比, 弗朗西斯·德·拉·图瓦, 伊万·瑞恩, 玛西娅·沃伦,...       同性   
2            5        [蒂莫西·柴勒梅德, 艾米·汉莫, 迈克尔·斯图巴, 阿蜜拉·卡萨, 艾斯特·加莱尔]       同性   
3            3                                     [张国荣, 梁朝伟, 张震]       同性   
4            5                     [赵文瑄, 归亚蕾, 金素梅, 郎雄, 米切尔·利希藤斯坦]       同性   

                                           cover_url        id is_playable  \
0  https://img3.doubanio.com/view/movie_poster_co...   1291546        True   
1  https://img3.doubanio.com/view/movie_poster_co...  26700818       False   
2  https://img3.doubanio.com/view/movie_poster_co...  26799731       False   
3  https://img3.doubanio.com/view/movie_poster_co...   1292679       False   
4  https://img3.doubanio.com/view/movie_poster_co...   1303037       False   

  is_watched  rank     rating            regions release_date  score  \
0      False     1  [9.5, 50]         [中国大陆, 香港]   1993-01-01    9.5   
1      False     2  [9.3, 50]               [英国]   2016-06-19    9.3   
2      False     3  [9.3, 50]  [意大利, 法国, 巴西, 美国]   2017-01-22    9.3   
3      False     4  [8.8, 45]       [香港, 日本, 韩国]   1997-05-30    8.8   
4      False     5  [8.8, 45]           [台湾, 美国]   1993-08-04    8.8   

       title                 types  \
0       霸王别姬          [剧情, 爱情, 同性]   
1  极品基老伴：完结篇              [喜剧, 同性]   
2  请以你的名字呼唤我              [爱情, 同性]   
3       春光乍泄          [剧情, 爱情, 同性]   
4         喜宴  [剧情, 喜剧, 爱情, 同性, 家庭]   

                                          url  vote_count  
0   https://movie.douban.com/subject/1291546/      629403  
1  https://movie.douban.com/subject/26700818/       13516  
2  https://movie.douban.com/subject/26799731/         739  
3   https://movie.douban.com/subject/1292679/      240127  
4   https://movie.douban.com/subject/1303037/      133193  
```

## Pandas DataFrame

```bash
# -*- coding: utf-8 -*-

import pandas as pd

movie_pd = pd.read_csv('../resources/douban_movie.csv', header=0, sep='\t')
print(type(movie_pd))
```

>运行结果

```bash
<class 'pandas.core.frame.DataFrame'>
```

```bash
Pandas的基本数据结构是DataFrame
DataFrame类似于Excel中的表，表有行标题和列标题
```

```bash
movie_count    total_vote     average_score
BJ          126         1762312            8.6
SH          138         2083123            8.3
TJ           95          891212            7.9
CQ           88          762310            8.1
【在Pandas中，列名相当于列标题movie_count、total_vote、average_score，而行标题BJ、SH、TJ、CQ就相当于索引】
```

### 按列创建DataFrame

```bash
# -*- coding: utf-8 -*-

import pandas as pd

temp_dict = {
    'score': [8.9, 8.2, 9.3],
    'category': ['悬疑', '动作', '爱情']
}

temp_pd = pd.DataFrame(temp_dict)
print(temp_pd)
```

>运行结果

```bash
category  score
0       悬疑    8.9
1       动作    8.2
2       爱情    9.3
```

### 按行创建DataFrame

```bash
# -*- coding: utf-8 -*-

import pandas as pd

row1 = [8.9, '悬疑']
row2 = [8.2, '动作']
row3 = [9.3, '爱情']
temp_pd = pd.DataFrame([row1, row2, row3], columns=['score', 'category'])
print(temp_pd)
```

>运行结果

```bash
score category
0    8.9       悬疑
1    8.2       动作
2    9.3       爱情
```

### index索引、columns列名 、values值

```bash
# -*- coding: utf-8 -*-

import pandas as pd

row1 = [8.9, '悬疑']
row2 = [8.2, '动作']
row3 = [9.3, '爱情']
temp_pd = pd.DataFrame([row1, row2, row3], columns=['score', 'category'])
print(temp_pd)
print('获取长度：',len(temp_pd))
print('获取索引：',temp_pd.index)
print('获取列：',temp_pd.columns)
print('获取值：',temp_pd.values)
```

>运行结果

```bash
   score category
0    8.9       悬疑
1    8.2       动作
2    9.3       爱情
获取长度： 3
获取索引： RangeIndex(start=0, stop=3, step=1)
获取列： Index(['score', 'category'], dtype='object')
获取值： [[8.9 '悬疑']
 [8.2 '动作']
 [9.3 '爱情']]
```

## 数据筛选

### 按一行或多行筛选

```bash
# -*- coding: utf-8 -*-

import pandas as pd

movie_pd = pd.read_csv('../resources/douban_movie.csv', header=0, sep='\t')

# 按照索引进行筛选
print(movie_pd.loc[0])
# print(movie_pd.loc[range(10)])
# print(movie_pd.loc[[1, 3, 8]])
```

>运行结果

```bash
actor_count                                                    19
actors          [张国荣, 张丰毅, 巩俐, 葛优, 英达, 蒋雯丽, 吴大维, 吕齐, 雷汉, 尹治, 马...
category                                                       同性
cover_url       https://img3.doubanio.com/view/movie_poster_co...
id                                                        1291546
is_playable                                                  True
is_watched                                                  False
rank                                                            1
rating                                                  [9.5, 50]
regions                                                [中国大陆, 香港]
release_date                                           1993-01-01
score                                                         9.5
title                                                        霸王别姬
types                                                [剧情, 爱情, 同性]
url                     https://movie.douban.com/subject/1291546/
vote_count                                                 629403
Name: 0, dtype: object
```

### 按一列或多列筛选

```bash
# -*- coding: utf-8 -*-

import pandas as pd

movie_pd = pd.read_csv('../resources/douban_movie.csv', header=0, sep='\t')

# 筛选电影数据的标题title和评分score
print(movie_pd['title'])
print(movie_pd[['title', 'score']])
```

>运行结果

```bash
0                  霸王别姬
1             极品基老伴：完结篇
2             请以你的名字呼唤我
3                  春光乍泄
4                    喜宴
5                  天佑鲍比
6              战场上的快乐圣诞
7                   莫里斯
8                   冬之蝉
9                  摇滚芭比
10                  断背山
11             达拉斯买家俱乐部
12                 费城故事
13                   面子
14                英伦性丑闻
15                 模仿游戏
16                迷恋荷尔蒙
17                 烈焰焚币
18                隐藏的恋情
19                    蓝
20                 单身男子
21                天鹅绒金矿
22                 菲洛梅娜
23                 迷情站台
24                   艾草
25                人生密密缝
26                 蓝色大门
27                 爱在暹罗
28               阿黛尔的生活
29                 金枝玉叶
             ...       
3658               大开眼戒
3659              云上的日子
3660                洛丽塔
3661           女性瘾者：第一部
3662           女性瘾者：第二部
3663                 偷香
3664               活色生香
3665                 定理
3666           性、谎言和录像带
3667             露西亚的情人
3668            捆着我，绑着我
3669    厨师、大盗、他的太太和她的情人
3670             萨玛利亚女孩
3671               色情男女
3672               白日美人
3673              唐朝豪放女
3674              情迷六月花
3675               同船爱歌
3676               风月奇谭
3677                振荡器
3678                 原罪
3679            性工作者十日谈
3680              爱你九周半
3681                 不忠
3682                 红字
3683             爱的那点性事
3684                不羁夜
3685                 雏妓
3686             你妈妈也一样
3687                十日谈
Name: title, dtype: object
                title  score
0                霸王别姬    9.5
1           极品基老伴：完结篇    9.3
2           请以你的名字呼唤我    9.3
3                春光乍泄    8.8
4                  喜宴    8.8
5                天佑鲍比    8.8
6            战场上的快乐圣诞    8.7
7                 莫里斯    8.7
8                 冬之蝉    8.7
9                摇滚芭比    8.7
10                断背山    8.6
11           达拉斯买家俱乐部    8.6
12               费城故事    8.6
13                 面子    8.6
14              英伦性丑闻    8.6
15               模仿游戏    8.5
16              迷恋荷尔蒙    8.5
17               烈焰焚币    8.5
18              隐藏的恋情    8.5
19                  蓝    8.5
20               单身男子    8.4
21              天鹅绒金矿    8.4
22               菲洛梅娜    8.4
23               迷情站台    8.4
24                 艾草    8.4
25              人生密密缝    8.4
26               蓝色大门    8.3
27               爱在暹罗    8.3
28             阿黛尔的生活    8.3
29               金枝玉叶    8.3
...               ...    ...
3658             大开眼戒    7.7
3659            云上的日子    7.7
3660              洛丽塔    7.7
3661         女性瘾者：第一部    7.7
3662         女性瘾者：第二部    7.7
3663               偷香    7.7
3664             活色生香    7.7
3665               定理    7.7
3666         性、谎言和录像带    7.6
3667           露西亚的情人    7.6
3668          捆着我，绑着我    7.6
3669  厨师、大盗、他的太太和她的情人    7.6
3670           萨玛利亚女孩    7.5
3671             色情男女    7.5
3672             白日美人    7.5
3673            唐朝豪放女    7.5
3674            情迷六月花    7.5
3675             同船爱歌    7.5
3676             风月奇谭    7.5
3677              振荡器    7.5
3678               原罪    7.4
3679          性工作者十日谈    7.4
3680            爱你九周半    7.4
3681               不忠    7.4
3682               红字    7.4
3683           爱的那点性事    7.4
3684              不羁夜    7.4
3685               雏妓    7.4
3686           你妈妈也一样    7.4
3687              十日谈    7.4

[3688 rows x 2 columns]
```

### 按一行一列或多行多列同时筛选

```bash
# -*- coding: utf-8 -*-

import pandas as pd

movie_pd = pd.read_csv('../resources/douban_movie.csv', header=0, sep='\t')
print(movie_pd.loc[5, 'actors'])  # 筛选出索引值是5的行，
print(movie_pd.loc[[1, 5, 8], ['title', 'actors']])
print(type(movie_pd['title']))
print(type(movie_pd[['title']]))
```

>运行结果

```bash
[西格妮·韦弗, 瑞恩·凯利, 亨利·科泽尼, 丹·巴特勒, 奥斯汀·尼可斯]
       title                                             actors
1  极品基老伴：完结篇  [伊恩·麦克莱恩, 德里克·雅各比, 弗朗西斯·德·拉·图瓦, 伊万·瑞恩, 玛西娅·沃伦,...
5       天佑鲍比            [西格妮·韦弗, 瑞恩·凯利, 亨利·科泽尼, 丹·巴特勒, 奥斯汀·尼可斯]
8        冬之蝉                              [森川智之, 三木真一郎, 森久保祥太郎]
<class 'pandas.core.series.Series'>
<class 'pandas.core.frame.DataFrame'>
```

### 多个有相同索引的 Series 就可以组成一个 DataFrame

```bash
# -*- coding: utf-8 -*-

import pandas as pd

# 多个有相同索引的 Series 就可以组成一个 DataFrame
# pd.Series()中可以传入一个列表进去，name 是 Series 本身的一个属性，index 表示索引，values 表示对应的值
temp_series = pd.Series([1, 4, 6, 10], name='simple_count')
print(temp_series)
print(temp_series.index)
print(temp_series.values)
```

```bash
0     1
1     4
2     6
3    10
Name: simple_count, dtype: int64
RangeIndex(start=0, stop=4, step=1)
[ 1  4  6 10]
```
