#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = "https://shop.flipperzero.one/"


response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')


product = html.find('div', class_="featured-product__price")
sold_out = product.find('span', class_="price__badge--sold-out")


print(sold_out)




