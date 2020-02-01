from selenium import webdriver
import time
#phan 路径
path=r'C:\Users\JiaTongBao\Desktop\phantomjs-2.1\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser=webdriver.PhantomJS(path)
url='https://movie.douban.com/typerank?type_name=爱情&type=13&interval_id=100:90&action='
browser.get(url)
time.sleep(5)
browser.save_screenshot(r'douban1.png')
#让browser执行简单JS代码，滚动条
js='document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(5)
browser.save_screenshot(r'douban2.png')
#可以捕获这个网页的源代码
html=browser.page_source
browser.quit()