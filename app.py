from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_stock_prices():
    url = "https://finance.yahoo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stocks_data = []

    for row in soup.select('.yfinlist tbody tr'):
        name = row.select_one('.data-col1').get_text(strip=True)
        price = row.select_one('.data-col2 span').get_text(strip=True)
        change = row.select_one('.data-col4 span').get_text(strip=True)
        stocks_data.append({'name': name, 'price': price, 'change': change})

    return stocks_data

@app.route('/')
def index():
    stocks = get_stock_prices()
    return render_template('index.html', stocks=stocks)

if __name__ == '__main__':
    app.run(port=8080)

