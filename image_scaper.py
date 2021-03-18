# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:35:40 2021

@author: nijum
"""

from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}
search =input("Search for:")
params ={"q":search}
r= requests.get("https://www.bing.com/images/search",params=params)
soup=BeautifulSoup(r.text,"html.parser")
#results=soup.find("ol",{"id":"b_results"})
link =soup.findAll("a",{"class":"thumb"})
#print(link)

for item in link:
    item_obj=requests.get(item.attrs["href"], stream=True)
    print(item.attrs["href"])
    title =item.attrs["href"].split("/")[-1]
    try:
       img=Image.open(BytesIO(item_obj.content))
       img.save("./image/"+title,img.format)
    except:
        print("could not save")
    