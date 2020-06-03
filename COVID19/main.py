from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

site = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun="

page = requests.get(site)
bsObject = BeautifulSoup(page.text, "html.parser")
# parseNews = bsObject.body.select("div.data_table.midd")
parse = bsObject.find_all('td')
# print(bsObject.prettify())
# print(parseNews)
print(parse)

# cnt = 1
# for article in parseNews:
#     print(cnt, " : ", article.get_text().strip())
#     cnt+=1
