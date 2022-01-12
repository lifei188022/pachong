import requests
query=input("输入一个你喜欢的明星:")
#url="https://www.sogou.com/web?query=周杰伦"
url=f'https://www.sogou.com/web?query={query}'
dic={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
resp=requests.get(url,headers=dic)  #处理了一个小小的反爬

print(resp)
print(resp.text)
