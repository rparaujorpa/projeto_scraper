# Cole este conteúdo no scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

dados = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()
    dados.append({'Título': title, 'Preço': price})

df = pd.DataFrame(dados)
df.to_excel('resultados.xlsx', index=False)
print("Arquivo 'resultados.xlsx' gerado com sucesso!")

