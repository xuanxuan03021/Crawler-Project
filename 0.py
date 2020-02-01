import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}

url="http://www.baidu.com"
request=urllib.request.Request(url,headers=headers)

response=urllib.request.urlopen(request)#要在最后加/才是完整的url
print(response.read().decode())
#这种方式直接在头部user-agent就说是自己是爬虫，有些就直接拦截
