import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup




def handle_title():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    url='http://365yg.com/'
    r=requests.get(url=url,headers=headers)
    with open('shipin','wb')as fp:
        fp.write(r.content)
    exit()
    soup=BeautifulSoup(r.text,'lxml')
    #获取链接
    title_href=soup.select('.title-box>a')
    print(title_href)
    #遍历链接
    for title in title_href:
        herf='http://365yg.com'+title['href']
        #获取标题
        title_text=title.text
        # 发送请求
       # handler_herf(url)

def main():

     handle_title()

if __name__ == '__main__':
    main()
