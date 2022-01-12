import re
# findall：匹配字符串中所有的符合正则的内容(返回的是列表)
result=re.findall('\d+','我的电话是10086，他的电话是8932')
#print((result))


# finditer:匹配字符串中所有的符合正则的内容(返回的是迭代器）,从迭代器中拿到内容需要group

# result=re.finditer('\d+','我的电话是10086，他的电话是8932')
# for i in result:
#     print(i.group())


# search 找到一个结果就返回，返回的是match对像，拿到数据需要group.
# result=re.search(r'\d+','我的电话是10086，他的电话是8932')
# print(result.group())


# match 从头开始匹配 找到一个结果就返回，返回的是match对像，拿到数据需要group.
# result=re.match(r'\d+','我的电话是10086，他的电话是8932')
# print(result.group())


# 预加载正则表达式
# obj=re.compile('\d+')
# result=obj.findall('我的电话是10086，他的电话是8932')
# print(result)



s="""
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='haha'><span id='2'>郭</span></div>
<div class='woo'><span id='3'>李林</span></div>
<div class='kee'><span id='4'>范思哲</span></div>
<div class='shengde'><span id='5'>胡说八道</span></div>
"""

# （?P<分组名字>正则）可以单独从正则切尔西的内容中进一步提取内容
obj=re.compile("<div class='.*?'><span id='\d+'>(?P<wahaha>.*?)</span></div>",re.S)  #re.S 让能匹配换行
# result=obj.findall(s)
result=obj.finditer(s)
for it in result:
    print(it.group("wahaha"))
