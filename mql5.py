import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
url = 'https://www.mql5.com/en/market/mt5/expert/paid?Rating=on&HasReviews=on'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
product = soup.find_all('div', {'class':'product-card__wrapper'})
for item in product:
    nama = item.find('span', {'class':'product-card__title-wrapper'}).text.strip()
    price = item.find('a', {'class':'product-card__price'}).text.strip()
    developer = item.find('div', {'class':'product-card__author'}).text.strip()
    list_item = {'Nama Software':nama,
                 'Harga Software':price,
                 'Developer':developer
                 }
    data.append(list_item)

df = pd.DataFrame(data)
print(df)
df.to_csv('software_mql5.csv', index=False, encoding='utf-8')



