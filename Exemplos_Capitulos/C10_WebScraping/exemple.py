import requests
import bs4

with open('exemple.html') as exepleFile:
    exepleSoup = bs4.BeautifulSoup(exepleFile, 'html.parser')
elems = exepleSoup.select('span')
for item in elems:
    print(item.getText())
