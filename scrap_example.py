from bs4 import BeautifulSoup
import requests
import pandas as pd

"""
url = "https://www.theverge.com/"
page = requests.get(url)

titles = list()
links  = list()

# Obtener los Titulos
soup = BeautifulSoup(page.content, "html.parser")
news = soup.find_all('h2',class_="c-entry-box--compact__title")
for i in news:
    titles.append(i.text)

# Obtener los links
for each_news in news:
    obj_soup = BeautifulSoup(str(each_news), 'html.parser')
    a = obj_soup.find('a')
    links.append(a['href'])

print(titles)
print(links)
"""


url = "https://techcrunch.com/"
page = requests.get(url)

titles = list()
links  = list()

# Obtener los Titulos
soup = BeautifulSoup(page.content, "html.parser")
news = soup.find_all('a',class_="post-block__title__link")
for i in news:
    titles.append(i.text)

# Obtener los links
for each_news in news:
    obj_soup = BeautifulSoup(str(each_news), 'html.parser')
    a = obj_soup.find('a')
    links.append(a['href'])

print(titles)
print(links)
