#验证码下载到本地，自己输入
#如果验证码不对的话，可能是form——data里面有随机生成的值，需要先访问页面，将值拿出来，或者他会识别cookie，就需要建立一个会话
#tesseract光学识别，但是准确度不高
#爬取古诗文网
#或者可以付钱进行识别，云打码，

import requests

from lxml import etree

s=requests.session()


url1='https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
url='https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }


#获取验证码
r1=s.get(url=url1,headers=headers)
print(r1.content)
text=r1.content
tree=etree.HTML(text)
yanzhengma_url='https://so.gushiwen.org'+tree.xpath('//div[@class="mainreg2"]/img[@id="imgCode"]/@src')[0]
r2=s.get(url=yanzhengma_url,headers=headers)
with open('yaznzhengma.png','wb')as fp:
    fp.write(r2.content)
code=input('哥们帮忙输一下验证码')

form_data={
    '__VIEWSTATE': 'rZB3ouf7lmppujgPFyWq8tnYYcpwzoouSAXZrA7QBBYs/vxVrdtdatvpxcnVLHQGLLhZKXf7HBKI5etyDRXlIy2Kvee7dzEF+izu9lS00U5Tzy+imoNp5rE0s5s=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': '',
    'email':'949507143@qq.com',
    'pwd': '1234567',
    'code': code,
    'denglu':'登录'
}

r=s.post(url=url,headers=headers,data=form_data)
print(r.content)
wode_url='https://so.gushiwen.org/user/collect.aspx'

r=s.post(url=wode_url,headers=headers)
with open ('gushiwen_wode.html','wb')as fp:
    fp.write(r.content)


