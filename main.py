from func import *

# menu()
# choose = int(input("Select number : "))

html, classType = menuType("classic")

print(html)
print(classType)
print("##########################")

context = makeCont()
menu = urlopen(html, context=context)
bsObject = BeautifulSoup(menu, "html.parser")
parseImg = bsObject.find_all("img")
# print(bsObject)
print(parseImg)
# showMenu(parseImg)
# cnt = 1
# for menu in parseImg:
#     print("###############################################")
#     print(cnt, " : ", menu.get("ul"))
#     cnt+=1
