from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request

searchTerm = 'person'
header = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
url = "https://www.google.com/search?q="+searchTerm+"&source=lnms&tbm=isch"

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get(url)



# a = borwser.find
# for i in range(200):
#     browser.execute_script("window.scrollBy(0,10000)")

# for idx, el in enumerate(browser.find_elements_by_class_name("rg_ic")):
#     el.screenshot(str(idx) + ".png")


# cnt = 0
# succCnt = 0

# print(os.path)

# if not os.path.exists(searchTerm):
#     os.mkdir(searchTerm)

# for _ in range(500):
#     browser.execute_script("window.scrollBy(0,10000)")

# for x in browser.find_element_by_xpath('//div[contains(@class, "rg_meta")]'):
#     cnt += 1
#     print("Total Count : ", cnt)
#     print("Successful Count : ", succCnt)
#     print("URL : ", json.loads(x.get_attribute('innerHTML'))["ou"])
