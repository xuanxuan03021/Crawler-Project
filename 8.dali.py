import urllib.request
import urllib.parse
import ssl
#代码配置handler其实是船舰一个handler，将要用的IP和端口号传进去，之后打开一个opener进行发送请求
ssl._create_default_https_context = ssl._create_unverified_context
#创建handler
url='https://www.baidu.com/s?wd=ip'
handler=urllib.request.ProxyHandler({'http':'110.86.139.164	:9999'})
#创建opener
opener=urllib.request.build_opener(handler)
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
request = urllib.request.Request(url, headers=headers)
response=opener.open(request)
with open('ip.html', 'wb')as fp:
    fp.write(response.read())
