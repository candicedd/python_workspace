import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os

# without eliminating possible duplicates, there should be in total ??? entries/items.

# after running this script,
# results without eliminating possible duplicates will be stored in file 'address_list', it is a tree structure
# e.g.,
# - prefecture1
#    - city1
#        - block1
#        - block2
#        - ...
#        - blockN
#    - city2
#        - block1
#        - block2
#        - ...
#        - blockN
#    - ...
#    - cityN
#        - block1
#        - block2
#        - ...
#        - blockN
# - ...
# - prefectureN
#    - city1
#        - block1
#        - block2
#        - ...
#        - blockN
#    - city2
#        - block1
#        - block2
#        - ...
#        - blockN
#    - ...
#    - cityN
#        - block1
#        - block2
#        - ...
#        - blockN

results_file = "address_list"

home_url = "https://www.navitime.co.jp"
start_url = "https://www.navitime.co.jp/?ctl=0050"

if os.path.isfile(results_file):
    os.remove(results_file)

# first level address in Japan 都道府県 とどうふけん
prefecture_link_dictionary = {} # prefecture_name_kanji:link
prefecture_name_dictionary = {} # prefecture_name_kanji:hiragana

# second level address in Japan 市／町 し／ちょう
city_link_dictionary = {} # city_name_kanji:link
city_name_dictionary = {} # city_name_kanji:hiragana

# third level address in Japan 町 ちょう
block_link_dictionary = {} # block_name_kanji:link
block_name_dictionary = {} # block_name_kanji:hiragana

# fourth level address in Japan 番地／丁目 ばんち／ちょうめ
# do we also possibly need that?

# get prefeture names and links
prefecture_page = urllib.request.urlopen(start_url)
prefecture_soup = BeautifulSoup(prefecture_page,features="lxml")
prefecture_page.close()

for prefecture in prefecture_soup.find_all("li", class_="pref-item"):
    for link in prefecture.find_all("a"):
        prefecture_link_dictionary[link.string] = link.get("href")
        prefecture_name_dictionary[link.string] = ""

        # get city names and links
        url = prefecture_link_dictionary[link.string]
        # convert iri to plain ascii uri
        url = urllib.parse.urlsplit(url)
        url = list(url)
        url[2] = urllib.parse.quote(url[2])
        url = urllib.parse.urlunsplit(url)
        # open webpage
        city_page = urllib.request.urlopen(url)
        city_soup = BeautifulSoup(city_page, features="lxml")
        city_page.close()

        prefecture_name_dictionary[link.string] = city_soup.find("div", class_="left left_contents").find("span").string
        print (link.string + " " + city_soup.find("div", class_="left left_contents").find("span").string)
        print (link.string + " " + city_soup.find("div", class_="left left_contents").find("span").string, file=open(results_file, "a", encoding="utf8"))

        for city_list in city_soup.find_all("div", class_="address_list"):
            for city in city_list.find_all("li", class_="left"):
                city_link_dictionary[city.a.string] = home_url + city.a.get("href")
                city_name_dictionary[city.a.string] = city.span.string
                print (city.a.string + " " + city.span.string)
                print (city.a.string + " " + city.span.string, file=open(results_file, "a", encoding="utf8"))

                # get block names and links
                block_page = urllib.request.urlopen(home_url + city.a.get("href"))
                block_soup = BeautifulSoup(block_page, features="lxml")
                block_page.close()

                for block_list in block_soup.find_all("div", class_="address_list"):
                    for block in block_list.find_all("li", class_="left"):
                        block_link_dictionary[block.a.string] = home_url + block.a.get("href")
                        # consumes too many memories, comment out
                        # block_name_dictionary[block.a.string] = block.span.string
                        print (block.a.string + " " + block.span.string)
                        print (block.a.string + " " + block.span.string, file=open(results_file, "a", encoding="utf8"))

