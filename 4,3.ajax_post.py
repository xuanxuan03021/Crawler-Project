import  urllib.request
import urllib.parse
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
url="https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"
number=20
start=(eval(input('请输入想要访问的页数：'))-1)*20
data={
    'start':start,
    'limit':number
}
#将字典转化成url
query_string=urllib.parse.urlencode(data)
#修改url
url+=query_string
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)
with open('douban.js','wb') as fp:
    fp.write(response.read())
file = open("douban.js")
print(json.load(file))