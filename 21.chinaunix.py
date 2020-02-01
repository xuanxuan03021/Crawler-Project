import urllib.request
import urllib.parse

url='http://account.chinaunix.net/login/login'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }
form_data={
              'username': 'xuanxuan',
              'password': '12345erf43',
              '_token': 'D9hjYEQ9k1wriP9U7RtXyiagxnm0nW7zfwAzl16y',
               '_t': '1574823063092'
}
#formdata 中可能会有formharsh，请求当不同时间打开这个页面，他的值会变，所以要手动获取
#直接抓包，获取post地址，发送请求就可以登陆成功
#但现在有的参数需要在网页上获取，就先要用get请求登陆到页面，用xpath和ba获取，加到表单里来，然后发送post请求
form=urllib.parse.urlencode(form_data).encode()
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request=request,data=form)
print(response.read().decode('gbk'))