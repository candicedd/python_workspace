import urllib.request
from bs4 import BeautifulSoup

start_url = "https://www.navitime.co.jp/?ctl=0050"

page = urllib.request.urlopen(start_url)

soup = BeautifulSoup(page,features="lxml")

pref_list = []

# step1, get prefeture names and links
for pref in soup.find_all("li", class_="pref-item"):
    for link in pref.find_all("a"):
        pref_list.append(link.get("href"))


print (pref_list)

# step 2, get city names and links
for link in pref_list:
    print (link, file=open("link","a", encoding="utf8"))