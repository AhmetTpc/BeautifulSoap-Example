import os
import random
import urllib.request
import requests
from bs4 import BeautifulSoup

def url_getir():
    #veri çekmek istediğimz url örnek olarak aşşağıdaki link kullanıldı.
    Url = "https://www.koctas.com.tr/mobilya/sandalyeler/c/109007?q=:relevance&page=4"
    Craw = requests.get(Url)
    soup = BeautifulSoup(Craw.text, 'html.parser')
    images = soup.find_all("img")
    if not (os.path.exists("Chair")):
        os.mkdir("Chair")
    f = open(os.path.join("Chair", "url.txt"), "a")
    for image in images:
        link = image['src']
        if link.startswith("h"):
            f.write(link + "\n")
    print("url'ler getirildi")

def kaydet():
    dosya = open(os.path.join("Chair", "url.txt"), "r")
    if not (os.path.exists("img")):
        os.mkdir("img")
    for satir in dosya:
        urllib.request.urlretrieve(satir, "img/" + str(random.randrange(1,999999999)) + ".jpg")
    print("getirilen urllerden resimler kaydedildi")

url_getir()
kaydet()
