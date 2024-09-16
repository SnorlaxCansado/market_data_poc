# Market Data Proof of Concept

## Overview

This Proof of Concept (PoC) demonstrates a simple pipeline for fetching stock market data from an API, transforming the data, and saving it in both CSV and Excel formats. The project is designed to be lightweight and uses Python, pandas, and the requests library.

## Folder Structure

- **config/**: Reserved for configuration files (e.g., API keys)
- **data/**: Contains output CSV and Excel files
- **logs/**: Tracks logs for each pipeline run
- **notebooks/**: For experimentation and exploratory data analysis
- **scripts/**: Core pipeline logic for fetching and transforming data
- **tests/**: Unit tests for the project
- **README.md**: Project documentation
- **requirements.txt**: Python dependencies
- **venv/**: Virtual environment for dependency isolation

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/market_data_poc.git
    cd market_data_poc
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the pipeline**:
    The pipeline will fetch stock data, transform it, and save the results in CSV and Excel files:
    ```bash
    python main.py
    ```

5. **Logs**: Pipeline run logs can be found in the `logs/` folder.

## Future Work
- Further optimizations in data transformation and storage.
- Integration with cloud services for scaling.