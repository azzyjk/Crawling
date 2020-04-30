from selenium import webdriver

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://www.google.com')
browser.close()