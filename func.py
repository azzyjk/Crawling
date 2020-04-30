from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

classicSite = "http://www.myashley.co.kr/Menu/SaladBar/Menu09.aspx"
wSite = "http://www.myashley.co.kr/Menu/SaladBar/Menu08.aspx"

def menu():
    print("1. Ashely classic menu")
    print("2. Ashely w menu")

def makeCont():
    return ssl._create_unverified_context()

def menuFind(html, classType):
    context = makeCont()
    menu = urlopen(html, context=context)
    bsObject = BeautifulSoup(menu, "html.parser")
    parseImg = bsObject.find("div", class_=classType).find_all("img")
    return parseImg

def showMenu(parseImg):
    cnt = 1
    for menu in parseImg:
        print(cnt, " : ", menu.get("alt"))
        cnt+=1

def menuType(grade):
    if (grade == "classic"):
        html = classicSite
        classType = "saladbar_menu"
    elif (grade == "w"):
        html = wSite
        classType = "season_sp"
    return html, classType