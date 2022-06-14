from bs4 import BeautifulSoup
import requests
import pandas as pd

import re


# ブランド名、検索件数によるスクレイピング
def sea(brand, limit):
    url = 'https://www.buyma.com/r/{}'.format(brand)
    limit_ = int(limit)
    limit_ *= 2

    # 検索件数分URL取得
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.select('.js-track-search-action.js-ecommerce-item-click', limit=int(limit_))

    # 出力型
    df = pd.DataFrame({
        '画像':[],
        '商品名':[],
        'カテゴリ１':[],
        'カテゴリ２':[],
        'カテゴリ３':[],
        'ブランド':[],
        'テーマ':[],
        '価格':[],
    },)

    # 検索件数分データ加工
    for index, item in enumerate(items):
        if index%2 == 0:
            res = requests.get('https://www.buyma.com' + item.attrs['href'])
            soup = BeautifulSoup(res.text, 'html.parser')
            # 画像
            folda = 'pic_' + str(int(index/2)+1)
            # 商品名
            title = soup.find('h1').text
            # カテゴリ1
            categori1 = soup.find_all('a', attrs={'class': 'ulinelink'})[4].text
            # カテゴリ2
            categori2 = soup.find_all('a', attrs={'class': 'ulinelink'})[5].text
            # カテゴリ3
            categori3 = soup.find_all('a', attrs={'class': 'ulinelink'})[6].text
            # ブランド
            brand = soup.select_one('.ulinelink').text
            # テーマ
            if soup.find('a', attrs={'data-vt': re.compile('.*theme.*')}):
                theme = soup.find('a', attrs={'data-vt': re.compile('.*theme.*')}).text
            else:
                theme = 'null'
            # 価格
            price = soup.select_one('.price_txt').text
            
            # データ代入
            df.loc[int(index/2+1)] = [folda, title, categori1, categori2, categori3, brand, theme, price]

    # df.to_csv("BUYMA.csv")
    return df

    