import pandas as pd
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
    original_price = article.select(' .product-original-price')[0].get_text()
    Discounted_prices = article.select(' .product-discounted-price')[0].get_text()
    Image_URL = article.select(' .product-img')[0]["src"]

    extracted_article_information.append({"title": title, "original price": original_price, "Discounted price": Discounted_prices, "Image URL": Image_URL})

for article in extracted_article_information:
    print("title: ", article['title'])
    print("original price: ", article['original price'])
    print("Discounted price: ", article['Discounted price'])
    print("Image URL: ", article['Image URL'])
    print("\n")

df = pd.DataFrame(extracted_article_information)
print(df)
speicherort = "C:\\Users\\Adrian\\OneDrive - uibk.ac.at\\Digital Organisations_AS\\extracted_articles.csv"
df.to_csv(speicherort, index=False)