import time
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}


def parse_navigation ():
    url = 'https://dalian.8684.cn'

    r = requests.get(url=url, headers=headers)
#解析内容获取导航的链接
    tree=etree.HTML(r.text)
    #查找一数字类型开头的所有链接
    num_list=tree.xpath('//div[@class="list"]/a/@href')
    num_list=num_list[:22]
  #  print(num_list)
    return  num_list



def parse_sanji(text):
    tree=etree.HTML(text)
    bus_num=tree.xpath('//div[@class="info"]/h1/text()')
    print(bus_num)
    bus_time=tree.xpath('//ul[@class="bus-desc"]/li/text()')
    print(bus_time)
    zongzhanshu=tree.xpath('//div[@class="total"]/text()')
    print(zongzhanshu)
    item={
        'bus_number':bus_num,
        'bus_time':bus_time,
    }



def parse_erji_route(text):
    tree=etree.HTML(text)
    route=tree.xpath('//div[@class="list clearfix"]/a/@href')
    print(route)
    for route1 in route:
        url='https://dalian.8684.cn'+route1
        r=requests.get(url=url,headers=headers)
        parse_sanji(r.text)
        exit()





def parse_erji(navigation_list):
    #遍历列表，依次发送请求
    for navigate in navigation_list:
        url='https://dalian.8684.cn'+navigate
        r=requests.get(url=url,headers=headers)
        #获取每一路公交的URL
        parse_erji_route(r.text)
        exit()


    pass

def main():
    navigation_list=  parse_navigation()
    content = parse_erji(navigation_list)


if __name__ == '__main__':
    main()
