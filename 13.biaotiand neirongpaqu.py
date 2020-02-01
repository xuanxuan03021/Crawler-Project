import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re
#
# def hand(url,page):
#     url = url1 + str(page) + '.html'
#     headers={}
#     request = urllib.request.Request(url=url, headers=headers)
#     return  request

def get_text(a_herf):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    request=urllib.request.Request(url=a_herf,headers=headers)
    #发送请求，获得内容
    response=urllib.request.urlopen(request).read().decode()
    pattern=re.compile(r'<div class="neirong">(.*?)</div>',re.S)
    it=pattern.findall(response)
    #写一个正则将所有的图片去掉
    text=it[0]
    pat=re.compile(r'<img (.*?)>')
    text=pat.sub('',text)
   # exit()
    return text


def parse_content(content):
    pattern=re.compile(r'<h3><a href="(/jingdiangaoxiaoyulu/\d+/\d+/\d+\.html)">(.*?)</a></h3>',re.S)#转义一下.为\.
    #返回的格式是一个列表，包含多个元组，元祖的第一个元素正则表达式中第一项对应正则表达式中的第一个括号
    it=pattern.findall(content)
    #print(it)
    #遍历列表
    for href_title in it:
        #获取内容的链接
        a_herf='http://www.yikexun.cn'+href_title[0]
        title=href_title[1]
        print(a_herf)
        #向href发送请求，获取内容
        text=get_text(a_herf)
        #写入到文件里
        string='<h1>%s</h1>%s'%(title,text)
        with open ('lizhi.html','a',encoding='utf8') as fp: #爬每一页的时候，将内容追加到文件中#如果不设置encoding就是gdk
            fp.write(string)


ssl._create_default_https_context = ssl._create_unverified_context

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
start_page=int(input('请输入起始页码'))
end_page=int(input('请输入结束页码'))
url1='http://www.yikexun.cn/jingdiangaoxiaoyulu/list_9_'
for page in range(start_page,end_page+1):
    url=url1+str(page)+'.html'
    #print(url)
    request=urllib.request.Request(url=url,headers=headers)
    content=urllib.request.urlopen(request).read().decode()
    #print(content)
    #hand(url,page)
    #解析内容
    parse_content(content)