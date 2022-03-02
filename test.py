"""
@AUTHOR Halaspec 

Before execute this script please install pip and lxml parser
"""

import requests
from bs4 import BeautifulSoup 

url = "https://halaspec.github.io/Web/" #MyWebSite :p

response = requests.get(url)

if(response.ok):
    soup = BeautifulSoup(response.text, 'lxml')
    print(str(soup('title')) + "\n" + "Links from my website :"+ "\n")
    links = soup.find_all('a')
    for a in links :
        if a['class'] == ['cv'] :
            print("https://halaspec.github.io/Web/"+str(a['href'])+ "\n")
        else:
            print(str(a['href'])+ "\n")