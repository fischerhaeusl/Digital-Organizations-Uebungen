

import requests
from bs4 import BeautifulSoup
import re

# URL der Seite, die Sie abrufen möchten
url = 'https://bdornauer.github.io/uibk_sales_shop'

# Abrufen der Inhalte der Webseite
response = requests.get(url)
html_content = response.text

# Verarbeitung des HTML-Inhalts mit BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Finden aller Elemente mit Preisen
prices = soup.find_all(text=re.compile(r'€'))

# Extrahieren und Ausdrucken der gefundenen Preise
for price in prices:
    print(price)