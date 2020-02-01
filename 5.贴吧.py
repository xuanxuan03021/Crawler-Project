#输入吧名，输入起始页码，输入结束页码,当前文件夹下创建一个吧名命名的一个html
import urllib.request
import urllib .parse
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url='http://tieba.baidu.com/f?ie=utf-8&'
ba_name=input('请输入要爬去的吧名：')
start_page=int(input('请输入要爬取的起始页码：'))
end_page=int(input('请输入要爬去的结束页码：'))
#创建文件夹
os.mkdir(ba_name)
#循环依次爬取每一页
for page in range(start_page,end_page+1):
    data={
        'kw':ba_name,
        'pn':(page+1)*50
          }
    data2=urllib.parse.urlencode(data)
    url_t=url+data2
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    print('开始爬取{} 页'.format(page))
    request = urllib.request.Request(url_t, headers=headers)
    response=urllib.request.urlopen(request)
    filename=ba_name+'_'+str(page)+'.html'
    filepath=ba_name+'/'+filename
    with open(filepath,'wb')as fp:
        fp.write(response.read())
    print('结束爬取{} 页'.format(page))