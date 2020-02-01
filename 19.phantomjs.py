from selenium import webdriver
import time
#phan 路径
path=r'/Users/humengxuan/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs'
browser=webdriver.PhantomJS(path)
url='http://www.baidu.com'
browser.get(url)
browser.save_screenshot(r'baidu.png')

time.sleep(3)
#查找input 输入框
my_input= browser.find_element_by_id('kw')

#往框里写字

my_input.send_keys('美女')
browser.save_screenshot(r'mwinv.png')
#查找搜索按钮返回的是列表
#'bg s_btn'只写s_btn就行可能不识别空格吧~
button=browser.find_elements_by_class_name('s_ipt')[0]
button.click()
time.sleep(3)

browser.save_screenshot(r'meinv.png')



time.sleep(3)
browser.quit()