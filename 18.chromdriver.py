from selenium import webdriver
import time
#模拟浏览器对象，通过对象去操作浏览器
path=r'/Users/humengxuan/Desktop/chromedriver'

browser = webdriver.Chrome(executable_path=path)
#print(browser)

url='http://www.baidu.com/'
browser.get(url)

time.sleep(3)


#查找input 输入框
my_input= browser.find_element_by_id('kw')

#往框里写字

my_input.send_keys('美女')

#查找搜索按钮返回的是列表
#'bg s_btn'只写s_btn就行可能不识别空格吧~
button=browser.find_elements_by_class_name('s_btn')[0]
button.click()
time.sleep(3)
#print(browser)
image=browser.find_elements_by_class_name('op-img-address-link-imgs')[2]
image.click()
