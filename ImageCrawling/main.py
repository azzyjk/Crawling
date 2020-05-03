from selenium import webdriver
import os

searchTerm = '사과'
url = "https://www.google.com/search?q="+searchTerm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome('/usr/local/bin/Chromedriver')


browser.get(url)
temp = browser.find_elements_by_class_name("rg_i")

if not os.path.exists(searchTerm):
    os.mkdir(searchTerm)

cnt = 0
for i in temp:
    i.screenshot("./"+searchTerm+"/"+str(cnt)+".png")
    cnt+=1

