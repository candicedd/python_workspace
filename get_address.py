import urllib.request
from bs4 import BeautifulSoup

start_url = "https://www.navitime.co.jp/?ctl=0050"

page = urllib.request.urlopen(start_url)

soup = BeautifulSoup(page)

print (soup.prettify())
