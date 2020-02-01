import urllib.request
import urllib .parse
import os
import ssl
import urllib.error

ssl._create_default_https_context = ssl._create_unverified_context
url='https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6%E8%B4%B4%E5%90%A7&rsv_spt=1&rsv_iqid=0x969cdd75002e0929&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&r_enter=1&rsv_dl=ts_0&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E7%25BF%25BB%25E8%25AF%2591&rsv_t=1786oALZEbn53CK4tWXKBDnoSIyaIjhB4dMsh0g9zQJmfwyAazCASeCtFTpz33rFiLJT&inputT=3003&rsv_sug3=21&rsv_sug1=16&rsv_sug7=100&rsv_pq=b8672b7a004a76af&rsv_sug2=1&prefixsug=%25E7%2599%25BE%25E5%25BA%25A6ties&rsp=0&rsv_sug4=364'
try:
    response=urllib.request.urlopen(url)
    print(response)
#except Exception as e:
   # print(e)
except urllib.error.HTTPError as e:
    print(e)
    print(e.code)#捕获状态吗
except urllib.error.URLError as e:
    print(e)