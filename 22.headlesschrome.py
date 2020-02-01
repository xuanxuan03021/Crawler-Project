#headlesschrome  无界面的谷歌浏览器
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#驱动路径
path=r'/Users/humengxuan/Desktop/chromedriver'
#创建浏览器对象
browser=webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
#上网
url='http://www.baidu.com'
browser.get(url=url)
time.sleep(3)
browser.save_screenshot('baidu123.png')
browser.quit()