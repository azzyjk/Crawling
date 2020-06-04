from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

site = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun="

page = requests.get(site)
bsObject = BeautifulSoup(page.text, "html.parser")
parseLoc = bsObject.find_all('td')

parseLoc = str(parseLoc).replace("<td>","").replace("</td>","\n")

print(parseLoc)
