from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_stock_prices():
    url = 'http://finance.yahoo.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='tablesorter')

    headers = []
    data = []

    if table:
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) == 2:
                headers.append(columns[0].get_text().strip())
                data.append(columns[1].get_text().strip())

    return headers, data

@app.route('/')
def index():
    headers, data = scrape_stock_prices()
    return render_template('index.html', headers=headers, data=data)

if __name__ == '__main__':
    app.run(port=8080)

