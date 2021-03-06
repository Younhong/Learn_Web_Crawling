import requests
from bs4 import BeautifulSoup

r=requests.get("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100")
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find("ul",{"class":"type06_headline"})

def getImageSrc():
    dl = all.find_all("dl")
    for item2 in dl:
        try:
            img = item2.find("dt", {"class": "photo"}).find("img")
            print(img['src'])
        except:
            print("No image")

def getLinkAndTitle():
    dl = all.find_all("dl")
    for item2 in dl:
        link = item2.find("dt", {"class": ""}).find("a")
        print(link['href'])
        print(link.text.replace("\t", "").replace("\n", "")[1:len(link.text) + 1])

def getContent ():
    dl = all.find_all("dl")
    for item2 in dl:
        try:
            content = item2.find("dd")
            print(content.text.replace("\t", "").replace("\n", "").split("...")[0])
            print(content.find("span",{"class": "writing"}).text)
            print(content.find("span", {"class": "date"}).text)
        except:
            print("No Content")


getImageSrc()
getLinkAndTitle()
getContent()
