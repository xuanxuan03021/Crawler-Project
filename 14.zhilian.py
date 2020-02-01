import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# http://sou.zhaopin.com/jobs/searchresult.ashx


class ZhilianSpider(object):

    url='http://sou.zhaopin.com/jobs/searchresult.ashx?'#类属性
    def __init__(self,jl,kw,start_page,end_page):
        #将上面的参数都保存为自己的成员属性
        self.jl=jl
        self.kw=kw
        self.start_page=start_page
        self.end_page=end_page
        #定义一个空列表,用来存放所有的工作信息
        self.items=[]

    def handle_request(self,page):#拼接url 生成请求对象

        data={
            'jl':self.jl,
            "kw":self.kw,
            "p":page
        }

        url_now=self.url+urllib.parse.urlencode(data)
        #不可以直接写url前面要加self，或者用类名调用
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        }

        request = urllib.request.Request(url=url_now,headers=headers )
        return request
#解析内容
    def parse_content(self,content):
        soup=BeautifulSoup(content,'lxml')
        #找到所有的table，因为一个工作岗位就是一个table，遍历这个table列表，然后通过table对象的select，find方法去找每一条记录的具体信息
        table_list=soup.select("#newlist_list_content_table > table")[1:]
        for table in table_list:
            zwmc=table.select('.zwmc>div>a')[0].text
            #公司名称
            gsmc= table.select('.gsmc>a')[0].text
            #职位月薪
            zwyx =table.select('.zwyx')[0].text
            #获取发布时间
            gxsj=table.select('.gxsj>span')[0].text
            #存放到字典
            item={
                '职位名称':zwmc,
                '公司名称':gsmc,
                '职位月薪':zwyx,
                '工作地点':gzdd,
                '更新时间':gxsj,
            }
            #在存放到列表当中
            self.items.append(item)




    #    爬取程序
    def run(self):
        for page in range(self.start_page,self.end_page+1):
            request=self.handle_request(page)#成员方法可以直接访问成员属性self.jl,self.kw,不用写
            content=urllib.request.urlopen(request).read().decode()
            self.parse_content(content)
            with open('zhilian.text','w',encoding='utf8') as fp:
                fp.writable(str(self.items))
def main():
    jl = input('请输入工作地点：')
    kw=input("请输入关键字：")
    start_page=int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
#    for page in range(start_page,end_page+1):
#创建对象，启动爬取程序
    spider =ZhilianSpider(jl,kw,start_page,end_page)
    spider.run()



if __name__ == '__main__':
    main()
