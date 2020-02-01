import urllib.request
import urllib.parse
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019811630329'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
form_data={
    'email': '18742508754',
    'icode':'',
    'origURL':'http://www.renren.com/972367841',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type':'web_login',
    'password': 'b1f64d1e0fd3cf1f59adfa23c28847297884ba4961485b2feae6fe430ca4b1d0',
    'rkey':'78e300be68f8cb06fa5904452e2c096a',
    'f':''

}
#创建一个cookie jar的对象
cj=http.cookiejar.CookieJar()
#通过一个cookiejar 来创建一个handler
handler=urllib.request.HTTPCookieProcessor(cj)
#创建一个opener
opener=urllib.request.build_opener(handler)

request = urllib.request.Request(url, headers=headers)
form_data=urllib.parse.urlencode(form_data).encode()
response=opener.open(request,data=form_data)
print(response.read().decode())

#with open('renren.html', 'wb')as fp:
    #fp.write(response.read().decode())
#登陆完后请求访问登陆后的页面
get_url='http://www.renren.com/972367841/profile'
request = urllib.request.Request(get_url, headers=headers)
response=opener.open(request)#因为上一次登陆，他将cookie自动保存在response里面了

with open('renren.html', 'wb')as fp:
    fp.write(response.read())