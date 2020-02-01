import requests



word='qwrr'
url='http://www.baidu.com/s?'#网上的地址去掉参数，用http
#参数学成一个字典
data={
    'ie':'utf-8',
    'wd': word ,
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
r=requests.get(url,headers=headers,params=data)#proxies= 代理名称
with open('ip.html', 'wb')as fp:
    fp.write(r.content)#字节类型，字符串类型是r.text
    #r.headers 查看相应头部
    #r.status_code 查看状态码
    #r.encoding 查看编码格式
    #r.url 查看所请求的u r l
    #r.json()查看json 格式数据
