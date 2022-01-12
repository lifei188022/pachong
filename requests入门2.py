import requests
url="https://fanyi.baidu.com/sug"
s=input("请输入英文单词:")
dic={"kw":s}
resp=requests.post(url,data=dic)
print(resp.json() )