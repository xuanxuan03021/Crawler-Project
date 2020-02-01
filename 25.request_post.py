import requests
from lxml import etree

url='https://cn.bing.com/ttranslatev3?isVertical=1&&IG=8466BC99692F4A5DBED8917057FD3897&IID=translator.5028.2'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    }

form_data={
'fromLang': 'auto-detect',
'text':'lion',
'to': 'zh-Hant',
}
r=requests.post(url=url,headers=headers,data=form_data)