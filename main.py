from func import *

menu()
choose = int(input("Select number : "))

# context = makeCont()
# menu = urlopen(wSite, context=context)
# bsObject = BeautifulSoup(menu, "html.parser")
# parseImg = bsObject.find("div", class_="season_sp").find_all("img")
# print(parseImg)

# parseImg = menuFind(wSite)
# showMenu(parseImg)

if(choose == 1):
    html, classType = menuType("classic")
    parseImg = menuFind(html, classType)
elif(choose == 2):
    html, classType = menuType("w")
    parseImg = menuFind(html, classType)

showMenu(parseImg)