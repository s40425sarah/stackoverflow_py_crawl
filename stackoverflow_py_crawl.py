import requests
from bs4 import BeautifulSoup

r = requests.get("https://stackoverflow.com/questions/tagged/python")
stackoverflow = r.text
soup = BeautifulSoup(stackoverflow)

lis = soup.find_all("div", class_="question-summary")
newsArray = []

for div in lis:
    s = {'link': div.find('div', class_="summary").find('h3').find('a').attrs['href'],'title':div.find('div', class_="summary").find('h3').find('a',class_ ="question-hyperlink").text}
    newsArray.append(s)
    print(s)

