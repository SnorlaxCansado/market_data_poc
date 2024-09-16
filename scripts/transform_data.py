import pandas as pd
import os
import logging

# Get the absolute path of the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))

def transform_data(df):
    """
    Clean and transform the stock data DataFrame.
    - Replace NaN values with 0
    - Rearrange columns in the correct order
    - Converts 'date' column to 'dd/mm/yyyy' format
    """
    if df.empty:
        print("Empty DataFrame received, skipping transformation.")
        return df
    
    # Replace NaN values with 0
    df.fillna(0, inplace=True)

    # Convert 'date' to datetime and format as 'dd/mm/yyyy'
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%d/%m/%Y')

    # Define the desired column order
    column_order = ['date', 'exchange', 'symbol', 'dividend', 'open', 'high', 'low', 'close', 'volume',
                    'adj_high', 'adj_low', 'adj_close', 'adj_open', 'adj_volume', 'split_factor']
    
    # Ensure all expected columns exist in the DataFrame (in case any are missing in the raw data)
    for col in column_order:
        if col not in df.columns:
            df[col] = 0  # Add missing columns and fill with 0
    
    # Reorder columns
    df = df[column_order]

    print(f"Data after transformation:\n{df.head()}")
    return df

def save_to_excel(df):
    """
    Save the transformed DataFrame into an Excel file.
    """
    data_dir = os.path.join(project_dir, '../data')
    
    # Save DataFrame to Excel file
    excel_path = os.path.join(data_dir, 'market_data_transformed.xlsx')
    
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Market Data', index=False)
        worksheet = writer.sheets['Market Data']
        worksheet.column_dimensions['A'].width = 12  # Date column width
        worksheet.column_dimensions['B'].width = 15  # Exchange column width
    
    logging.info(f"Transformed data saved to Excel: {excel_path}")
    print(f"Data saved to {excel_path}")

if __name__ == "__main__":
    # Set up logging
    log_file = os.path.join(project_dir, '../logs/pipeline.log')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Load data from CSV
    data_dir = os.path.join(project_dir, '../data')
    df = pd.read_csv(os.path.join(data_dir, 'market_data.csv'))

    # Transform the data
    transformed_df = transform_data(df)

    # Save transformed data to CSV
    csv_path = os.path.join(data_dir, 'market_data_transformed.csv')
    transformed_df.to_csv(csv_path, index=False)
    logging.info(f"Transformed data saved to CSV: {csv_path}")
    print(f"Transformed data saved to {csv_path}")

    # Save the transformed data to Excel file
    save_to_excel(transformed_df)