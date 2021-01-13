import requests
import urllib.request
from datetime import date
from bs4 import BeautifulSoup

#date header
today = date.today()

#url link
url = "https://en.wikipedia.org/wiki/Special:Random"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

#heading
heading = soup.find("h1", class_="firstHeading")

#body
body = soup.select("div.mw-parser-output > p")

print(f"Article Of The Day for {today} is: {heading.text}")
print()
for p in body:
    print(p.text)