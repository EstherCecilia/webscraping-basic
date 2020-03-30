# -*- coding: cp1252 -*-
import requests
from bs4 import BeautifulSoup


# Coletar e analisar a primeira página
page = requests.get('http://example.webscraping.com/')
soup = BeautifulSoup(page.text, 'html.parser')



# Pegar o texto de todas as instâncias da tag <a> dentro de Soup
artist_name_list_items = soup.find_all('a')



# Criar loop para imprimir todos os nomes de artistas
for artist_name in artist_name_list_items:
    print(artist_name.get('href'))

