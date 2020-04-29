from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

html = urlopen("http://www.myashley.co.kr/Menu/SaladBar/Menu08.aspx", context=context)
bsObject = BeautifulSoup(html, "html.parser")
parseImg = bsObject.body.find_all('img')

for menu in parseImg:
     print(menu.get('alt'))
