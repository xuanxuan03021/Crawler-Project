import urllib.request
import urllib.parse
import time
import json
from lxml import etree
import os


def handle_request(url,page,url2):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    #由于第一页和后面的页码不一样，所以要进行判断
    if page ==1:
        url=url
    else: url = url2.format(page)
    request=urllib.request.Request(url=url,headers=headers)
    return request
#解析内容，下载图片
def parse_content(content):
    tree=etree.HTML(content)
    #检查的时候从第一个表达式开始测，一步一步加
    image_list=tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    print(image_list)
    #懒加载：用到的时候再加载，只在用户能看到的地方显示，在滑动的时候显示  网页显示一个图片就要发送一次请求
    #实现<img src2='图片'>没有用src所以 浏览器不识别，就不会加载，当用户滑动到图片是JS就会自动加载添加一个SRC让浏览器识别，所以单独搜索SRC的时候就不会出现
    for imag_src in image_list:
        download_image(imag_src)


def download_image(image_src):
    dirpath='xinggan'
    #创建一个文件
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    filename=os.path.basename(image_src)#返回文件名
    filepath=os.path.join(dirpath,filename)
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    request=urllib.request.Request(url=image_src,headers=headers)
    response=urllib.request.urlopen(request)
    with open (filepath,'wb') as fp:
        fp.write(response.read())




def main():
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    url='http://sc.chinaz.com/tupian/xingganmeinvtupian.html'
    url2="http://sc.chinaz.com/tupian/xingganmeinvtupian_{}.html"
    for page in range(start_page,end_page+1):
        request=handle_request(url,page,url2)
        content=urllib.request.urlopen(request).read().decode()
     #   print(content)
        parse_content(content)
   # with open('suanzi.txt','w',encoding='utf8') as fp:
    #    fp.write(str(item_list))

if __name__ == '__main__':
    main()