from urllib.request import urlopen
from bs4 import BeautifulSoup
import pprint
import ssl

context = ssl._create_unverified_context()
pp=pprint.PrettyPrinter(indent=4)
html = urlopen("http://www.naver.com", context = context)
bsObject = BeautifulSoup(html, "html.parser")

for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))
