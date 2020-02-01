import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url='http://www.baidu.com/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
#创建一个handler
handler=urllib.request.HTTPHandler()
#创建一个openner,opener是一个对象，发送请求时不用urlopen 直接调用opener的一个方法
opener=urllib.request.build_opener(handler)
request = urllib.request.Request(url, headers=headers)
response=opener.open(request)
print(response.read().decode())