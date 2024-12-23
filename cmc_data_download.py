import requests
import pandas as pd
from datetime import datetime, timedelta
import pymongo

CMC_URLS = {
    'Bitcoin': 'https://coinmarketcap.com/currencies/bitcoin/historical-data/',
    'Tether': 'https://coinmarketcap.com/currencies/tether/historical-data/',
    'Ethereum': 'https://coinmarketcap.com/currencies/ethereum/historical-data/'
}

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['crypto_data']

def download_cmc_data(currency):
    url = CMC_URLS[currency]
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    params = {
        'start': int(start_date.timestamp()),
        'end': int(end_date.timestamp())
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def store_cmc_data():
    for currency in CMC_URLS.keys():
        data = download_cmc_data(currency)
        db.crypto_prices.insert_many(data)

if __name__ == "__main__":
    store_cmc_data()
