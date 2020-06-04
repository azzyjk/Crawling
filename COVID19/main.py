from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time

site = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun="

page = requests.get(site)
bsObject = BeautifulSoup(page.text, "html.parser")
parseLoc = bsObject.find_all('td')

parseLoc = str(parseLoc).replace("<td>","").replace("</td>","\n").replace("<br/>","\n")
lists = []
lists = parseLoc.split('\n')
for tst in lists:
    time.sleep(1)
    print(tst)
