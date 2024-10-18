import os
from dotenv import load_dotenv
import ccxt

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

# Fetch recent price data for BTC/USDT
btc_data = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)
print(btc_data)
