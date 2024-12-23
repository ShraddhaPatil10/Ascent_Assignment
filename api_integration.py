import requests
import pandas as pd
from datetime import datetime, timedelta
import pymongo
import mysql.connector

API_KEY = 'jsVd7H3RswsiGR6kU8mpaVpz6NWIpWQ0X6s7IVeNrg7DQ6zPUyWXEpH5gAKBfyeC'
API_SECRET = 'XzVg3q6BHC2qLXbGIrgLJvfDw6pC6FS42S0rzjvFdA91fVnAQfp7t9pAh5TTvVdc'
BASE_URL = 'https://fapi.binance.com/fapi/v2/'
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['crypto_data']

def fetch_data(endpoint, params=None):
    headers = {
        'X-MBX-APIKEY': API_KEY
    }
    response = requests.get(BASE_URL + endpoint, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def fetch_account_info():
    data = fetch_data('account')
    db.binance_account.insert_one(data)

def fetch_trades():
    params = {'limit': 1000}
    trades = []
    while True:
        data = fetch_data('myTrades', params)
        if not data:
            break
        trades.extend(data)
        params['fromId'] = data[-1]['id'] + 1
    db.binance_trades.insert_many(trades)

def fetch_income():
    params = {'limit': 1000}
    income = []
    while True:
        data = fetch_data('income', params)
        if not data:
            break
        income.extend(data)
        params['fromId'] = data[-1]['id'] + 1
    db.binance_income.insert_many(income)

if __name__ == "__main__":
    fetch_account_info()
    fetch_trades()
    fetch_income()
