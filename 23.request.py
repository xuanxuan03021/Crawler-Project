import requests

url='http://www.baidu.com/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
r=requests.get(url,headers=headers)

#print(r.encoding)
r.encoding='utf8'
print(r.text)