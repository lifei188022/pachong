from urllib.request import urlopen
url = "http://www.baidu.com"
#url="http://cacti.idccun.com"
resp = urlopen(url)

with open("mybaidu.html",mode="w",encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))

print("over")

open(file)

