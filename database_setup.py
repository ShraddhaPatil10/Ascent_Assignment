import pymongo
import mysql.connector

def setup_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['crypto_data']
    db.create_collection('binance_account')
    db.create_collection('binance_trades')
    db.create_collection('binance_income')
    db.create_collection('crypto_prices')

def setup_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='yourusername',
        password='yourpassword',
        database='crypto_data'
    )
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS binance_account (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data JSON NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS binance_trades (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data JSON NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS binance_income (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data JSON NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            currency VARCHAR(255),
            date DATE,
            open DECIMAL(18, 8),
            close DECIMAL(18, 8),
            volume DECIMAL(18, 8)
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Uncomment the following line for MongoDB or MySQL setup
    # setup_mongodb()
    # setup_mysql()
