from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

site = "https://news.naver.com/"

page = requests.get(site)
bsObject = BeautifulSoup(page.text, "html.parser")
parseNews = bsObject.body.select("div.hdline_article_tit")

cnt = 1
for article in parseNews:
    print(cnt, " : ", article.get_text().strip())
    cnt+=1
