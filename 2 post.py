import  urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#获取postURL地址
post_url='https://fanyi.baidu.com/sug'
word=input("请输入您要查询的英文单词")
#构建post表单数据
form_data={
     "kw":word
}
#发送请求过程
headers={
    "User-Agent":" 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'"
}
request=urllib.request.Request(url=post_url,headers=headers)
#处理表单数据,将其变成url形式，并且变成二进制形式
form_data=urllib.parse.urlencode(form_data).encode()
#发送请求get方式需要拼接拼接 但是post不需要,加一个data参数
response = urllib.request.urlopen(request,data=form_data)
print(response.read().decode())