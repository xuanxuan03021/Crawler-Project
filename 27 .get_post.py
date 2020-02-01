import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup


s=requests.session()
url='http://account.chinaunix.net/login'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
#访问登陆页面获取hash值
r=s.get(url=url,headers=headers)
#生成soup对象，获取值
soup=BeautifulSoup(r.text,'lxml')
token=soup.select('input[name=_token]')[0]['value']
print(token)
#利用刚刚获取到的token发送post请求
post_url='http://account.chinaunix.net/login/login'
form_data={
              'username': 'xuanxuan',
              'password': '12345erf43',
              '_token': token,
               '_t': '1574823063092'
}
r=s.post(url=url,headers=headers)
url3=''
r=s.get(url=url3,headers=headers)