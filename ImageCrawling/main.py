from selenium import webdriver

searchTerm = '라이언'
url = "https://www.google.com/search?q="+searchTerm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome('/usr/local/bin/Chromedriver')


browser.get(url)
temp = browser.find_elements_by_class_name("rg_i")

picture = temp[0]

picture.screenshot("test.png")
