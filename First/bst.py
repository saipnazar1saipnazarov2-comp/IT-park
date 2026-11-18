import requests
from bs4 import BeautifulSoup

url = requests.get("https://sinoptik.ua/ru/pohoda/urhench")
malumot = BeautifulSoup(url.content, 'html.parser')
a = malumot.select('.google-anno-skip')

for i in a:
    shahar = i.select("._8X9sSr2b")[0].text
    kun = i.select(".xM6dxfW4")[0].text
    Ob_havo = i.select(".oOVtmpFl")[0].text
    print(f"Shahar: {shahar}\n Kun: {kun}\n Ob_havo: {Ob_havo}")

for i in a:
    shahar2 = i.select("._8X9sSr2b")[0].text
    kun2 = i.select(".xM6dxfW4")[2].text
    Ob_havo2 = i.select(".oOVtmpFl")[2].text
    print(f"Shahar: {shahar2}\n Kun: {kun2}\n Ob_havo: {Ob_havo2}")

for i in a:
    shahar3 = i.select("._8X9sSr2b")[0].text
    kun3 = i.select(".xM6dxfW4")[3].text
    Ob_havo3 = i.select(".oOVtmpFl")[3].text
    print(f"Shahar: {shahar3}\n Kun: {kun3}\n Ob_havo: {Ob_havo3}")

for i in a:
    shahar4 = i.select("._8X9sSr2b")[0].text
    kun4 = i.select(".xM6dxfW4")[4].text
    Ob_havo4 = i.select(".oOVtmpFl")[4].text
    print(f"Shahar: {shahar4}\n Kun: {kun4}\n Ob_havo: {Ob_havo4}")

for i in a:
    shahar5 = i.select("._8X9sSr2b")[0].text
    kun5 = i.select(".xM6dxfW4")[5].text
    Ob_havo5 = i.select(".oOVtmpFl")[5].text
    print(f"Shahar: {shahar5}\n Kun: {kun5}\n Ob_havo: {Ob_havo5}")

for i in a:
    shahar6 = i.select("._8X9sSr2b")[0].text
    kun6 = i.select(".xM6dxfW4")[6].text
    Ob_havo6 = i.select(".oOVtmpFl")[6].text
    print(f"Shahar: {shahar6}\n Kun: {kun6}\n Ob_havo: {Ob_havo6}")

# import requests
# from bs4 import BeautifulSoup 

# url = requests.get("https://sinoptik.ua/ru/pohoda/urhench")
# malumot = BeautifulSoup(url.content,'html.parser')
# a = malumot.select('.google-anno-skip')
# for i in a:
#     shaxar = i.select("._8X9sSr2b")[0].text
#     kun = i.select(".xM6dxfW4")[0].text
#     Ob_Havo = i.select(".oOVtmpFl")[1].text
# print(f"Shaxar {shaxar}\nKun {kun}\nOb-Havo {Ob_Havo}")




























