
# 定位到2022改掉片
# 从2022必看片中提取到子页面的地址
# 请求页面的链接地址，拿到我们想要下载的地址
from base64 import decode
import requests
domain="https://www.dytt89.com/"
resp=requests.get(domain,verify=False)  #verify=False 去掉安全验证
resp.encoding='gb2312'
page_content=resp.text
print(page_content)