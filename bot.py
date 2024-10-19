import os
from dotenv import load_dotenv
import ccxt
import time

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

# Set up connection to Binance
exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_API_SECRET,
    'enableRateLimit': True,
})
exchange.options['adjustForTimeDifference'] = True

# Fetch recent price data for BTC/USDT
btc_data = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)

# Column headers
print(f"{'Timestamp':<20} {'Open':<10} {'High':<10} {'Low':<10} {'Close':<10} {'Volume':<10}")

# Loop through the data and format it
for entry in btc_data:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry[0] / 1000))
    open_price = entry[1]
    high_price = entry[2]
    low_price = entry[3]
    close_price = entry[4]
    volume = entry[5]
    
    print(f"{timestamp:<20} {open_price:<10} {high_price:<10} {low_price:<10} {close_price:<10} {volume:<10}")
