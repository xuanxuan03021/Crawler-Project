import urllib.request
import urllib.parse
import time
import json
from lxml import etree



item_list=[]

def handle_request(url,page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
    url=url.format(page)
    print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request

def parse_content(content):
    tree=etree.HTML(content)
    #抓取内容
    list_box=tree.xpath('//ul[@class="list-box"]/li')
    print(list_box)
    #爬取没有CLASS属性的LI？
    # 我选则一个一个
    i=1
    t=0
    for list in list_box:
        if i%3==0:
            del list_box[i-t-1]
            t = t + 1
        i+=1
    print(list_box)

    for list in list_box:
        title=list.xpath('./div[@class="head"]/h2/text()')
        text= list.xpath('./div[@class="content"]/a//text()')
        # print(title)
        print(text)
        #text='/n'.join(text)
        item={
            '标题':title,
             "内容": text,
        }
        item_list.append(item)





def main():
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    url="http://www.haoduanzi.com/category/?1-{}.html"
    for page in range(start_page,end_page+1):
        request=handle_request(url,page)
        content=urllib.request.urlopen(request).read().decode()
        parse_content(content)
    with open('suanzi.txt','w',encoding='utf8') as fp:
        fp.write(str(item_list))

if __name__ == '__main__':
    main()

