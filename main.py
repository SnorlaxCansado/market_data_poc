import os
import pandas as pd
from scripts.fetch_market_data import fetch_stock_data
from scripts.transform_data import transform_data, save_to_excel
import logging

# Get the absolute path of the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# Set up paths relative to the project directory
log_dir = os.path.join(project_dir, 'logs')  # Directly pointing to the 'logs' folder inside the project directory
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging with the correct absolute path
log_file = os.path.join(log_dir, 'pipeline.log')
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    """
    Main function to run the data pipeline:
    1. Fetch market data
    2. Transform the data
    3. Save raw and transformed data to CSV
    4. Save transformed data to Excel
    """
    logging.info("Pipeline started...")
    
    # Step 1: Fetch market data
    logging.info("Fetching stock market data...")
    stock_data = fetch_stock_data()
    
    if not stock_data.empty:
        # Save raw data to CSV in 'data' folder
        data_dir = os.path.join(project_dir, 'data')  # Ensures 'data' folder is directly used
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        raw_csv_path = os.path.join(data_dir, 'market_data.csv')
        stock_data.to_csv(raw_csv_path, index=False)
        logging.info(f"Raw market data saved to {raw_csv_path}")
        print(f"Raw data saved to {raw_csv_path}")

        # Step 2: Transform the data
        logging.info("Transforming stock market data...")
        transformed_data = transform_data(stock_data)

        # Save transformed data to CSV in 'data' folder
        transformed_csv_path = os.path.join(data_dir, 'market_data_transformed.csv')
        transformed_data.to_csv(transformed_csv_path, index=False)
        logging.info(f"Transformed data saved to {transformed_csv_path}")
        print(f"Transformed data saved to {transformed_csv_path}")

        # Step 3: Save transformed data to Excel
        save_to_excel(transformed_data)
        logging.info(f"Transformed data saved to Excel in {os.path.join(data_dir, 'market_data_transformed.xlsx')}")
        print("Pipeline completed successfully! 🚀")
    else:
        logging.warning("No data fetched, skipping transformation.")
        print("No data fetched. Please check the logs for more information.")

if __name__ == "__main__":
    run_pipeline()