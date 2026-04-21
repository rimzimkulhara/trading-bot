import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("API_SECRET")
    )

    # 🔥 IMPORTANT FIX (Futures Testnet endpoint)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
