

import requests
from bs4 import BeautifulSoup

# URL der Seite, die Sie abrufen möchten
url = 'https://bdornauer.github.io/uibk_sales_shop'

# Abrufen der Inhalte der Webseite
data = requests.get(url)


# Verarbeitung des HTML-Inhalts mit BeautifulSoup
html = BeautifulSoup(data.text, 'html.parser')
articles = html.select('.product-section')

#print(articles[0])

#create empty list
extracted_article_information = []

for article in articles:
    title = article.select(' .product-name')[0].get_text()

for article in extracted_article_information:
    print("title: ", article["title"])