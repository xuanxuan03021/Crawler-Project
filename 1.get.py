import ssl
import urllib.request
import urllib.parse
word=input('请输入你想要搜索的内容：')
url='http://www.baidu.com/s?'#网上的地址去掉参数，用http
#参数学成一个字典
data={
    'ie':'utf-8',
    'wd': word ,
}
query_string=urllib.parse.urlencode(data)
url +=query_string
print(url)
#发送请求
#而当目标网站使用的是自签名的证书时就会抛出一个 urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)> 的错误消息，

context = ssl._create_unverified_context()
response = urllib.request.urlopen(url,context=context).read()
with open ('word.html','wb')as fp:
    fp.write(response)