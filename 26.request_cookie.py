
import requests
#新建一个会话
#之后所有的操作都是用S进行 s.get s.post
s=requests.session()

url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20191051430376'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }

form_data={
'email': '18742508754',
'icode': '',
'origURL': 'http://www.renren.com/home',
'domain': 'renren.com',
'key_id': '1',
'captcha_type': 'web_login',
'password': '4a606e4e3f3861652c6017d9b0b1c68bae2e3f846827c13219e4c5aa58235c47',
'rkey': 'ec70890e3b23f6eef5aa824c0816f629',

}
r=s.post(url=url,headers=headers,data=form_data)
print(r.text)
get_url='http://www.renren.com/972367841/profile'
r2=s.get(url=get_url,headers=headers,data=form_data)
print(r2 .text)