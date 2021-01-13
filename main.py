import requests
import urllib.request
from datetime import date
from bs4 import BeautifulSoup
from splinter import Browser


#date header
today = date.today()

#url link
url = "https://en.wikipedia.org/wiki/Special:Random"
# url = "https://en.wikipedia.org/wiki/List_of_Sonic_the_Hedgehog_printed_media" 
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

#re-directed url
current_url = soup.find("div", class_="printfooter")

#heading
heading = soup.find("h1", class_="firstHeading")

#table
has_table = False
if soup.find("table", class_="infobox vcard") != None:
    table = soup.find("table", class_="infobox vcard")
    has_table = True

#body
body = soup.select("div.mw-parser-output > p")

#lists
has_list = False
if soup.select("div.mw-parser-output > ul") != None:
    list_ = soup.select("div.mw-parser-output > ul")
    has_list = True



print('''
 =============
|| WIKIPEDIA ||
 =============
''')
print(f"Article Of The Day for {today} is: {heading.text}")
print()
if has_table:
    for row in table:
        print(row.text + " ")
        print()

print()
for p in body:
    print(p.text)
    if has_list:
        for li in list_:
            print(li.text)
    has_list = False
print()

print(current_url.text)