
import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re
import os
import time
def download_image(content):
    pattern=re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>',re.S)#正则表达式要一个一个严格的对上，要的用小括号扩起来,re.S在单航模式的时候.可以匹配换行符，再多行格式是不能匹配换行符
    ret=pattern.findall(content)
    print(ret)#列表格式
    #便利列表，下载图片
    for image in ret:
        #处理图片的URL格式
        image_src='https:'+image
        #创建文件夹
        dirname='qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filename=image_src.split('/')[-1]
        filepath=dirname+'/'+filename
        print('%s图片下载开始'%filename)
        urllib.request.urlretrieve(image_src,filepath)
        print('%s图片下载结束' % filename)
        #发送请求，下载图片



ssl._create_default_https_context = ssl._create_unverified_context

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
url='https://www.qiushibaike.com/pic/page/'
start_page=int(input('请输入起始页码'))
end_page=int(input('请输入结束页码'))
for page in range(start_page,end_page+1):
    print('第%s页正在下载'%page)
    url2=url+str(page)+'/'
    print(url2)
    request=urllib.request.Request(url=url2,headers=headers)
    #发送请求对象
    content=urllib.request.urlopen(request).read().decode()
    #解析内容，提取所有的图片链接下载图片
    download_image(content)
    print('第%s页下载结束' % page)
    time.sleep(2)

