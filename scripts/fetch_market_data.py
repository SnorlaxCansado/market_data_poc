import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import logging

# Get the absolute path of the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# Set up paths relative to the project directory
log_dir = os.path.join(project_dir, '../logs')

# Ensure the logs folder exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging with the correct absolute path
log_file = os.path.join(log_dir, 'pipeline.log')
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = '461179b825c645877648bd3fd25d9a7f'
BASE_URL = 'http://api.marketstack.com/v1/eod'
SYMBOL = 'JBSS3.BVMF'

def fetch_stock_data():
    """
    Fetch stock data from Marketstack API for the last 3 days.
    Returns a pandas DataFrame.
    """
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=3)

    params = {
        'access_key': API_KEY,
        'symbols': SYMBOL,
        'date_from': start_date,
        'date_to': end_date
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            df = pd.DataFrame(data['data'])
            logging.info(f"Data fetched successfully for {SYMBOL}")
            return df
        else:
            logging.error("No data in response")
            return pd.DataFrame()  # Return empty DataFrame if no data
    else:
        logging.error(f"Failed to fetch data: {response.status_code}")
        return pd.DataFrame()

if __name__ == "__main__":
    stock_data = fetch_stock_data()

    if not stock_data.empty:
        print(stock_data.head())  # Display fetched data for verification
        # Save raw data to CSV
        data_dir = os.path.join(project_dir, '../data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        stock_data.to_csv(os.path.join(data_dir, 'market_data.csv'), index=False)
        logging.info("Data saved to market_data.csv")
    else:
        logging.warning("No data fetched.")
