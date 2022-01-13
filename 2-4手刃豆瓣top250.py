# 拿到原代码
# 通过re提取信息
# 需要名字，年份，评价，评分
import requests,re,csv
url="https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
resp=requests.get(url,headers=headers)

page_content = resp.text 
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
r'</span>.*?<div class="bd">.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'
r'.*?<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>'
r'.*?<span>(?P<pingjia>.*?)人评价',re.S)

result=obj.finditer(page_content)
f=open("data.csv",mode="w")
csvwiter=csv.writer(f)
for it in result:
    
    #print(it.group("name").strip(),it.group("year").strip(),it.group("pingfen".strip())
    #,it.group("pingjia").strip())
    dic=it.groupdict()
    dic['year']=dic['year'].strip()
    csvwiter.writerow(dic.values())
f.close()
print("over")


 