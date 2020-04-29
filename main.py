from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

html = urlopen(
    "http://www.myashley.co.kr/Menu/SaladBar/Menu08.aspx", context=context)
bsObject = BeautifulSoup(html, "html.parser")
parseImg = bsObject.find("div", class_="season_sp").find_all("img")

cnt = 1
for menu in parseImg:
    print(cnt," : ", menu.get('alt'))
    cnt+=1