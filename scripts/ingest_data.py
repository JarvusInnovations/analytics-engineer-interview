#!/usr/bin/env python3
import os
import requests
import duckdb
import pandas as pd
from pathlib import Path

def ensure_directories():
    """Create necessary directories if they don't exist."""
    Path("data/raw").mkdir(parents=True, exist_ok=True)

def download_data():
    """Download the bus shelters CSV file."""
    url = "https://opendata.arcgis.com/api/v3/datasets/c2dfc18b429049e5aa4e9afdbebd3c3f_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1"
    response = requests.get(url)
    response.raise_for_status()

    output_path = "data/raw/bus_shelters.csv"
    with open(output_path, "wb") as f:
        f.write(response.content)
    return output_path

def load_to_duckdb(csv_path):
    """Load the CSV data into DuckDB."""
    # Initialize DuckDB connection
    db_path = "data/analytics.db"
    con = duckdb.connect(db_path)

    try:
        # Read CSV into pandas DataFrame
        df = pd.read_csv(csv_path)

        # Create raw table in DuckDB
        con.execute("""
            CREATE TABLE IF NOT EXISTS raw_bus_shelters AS
            SELECT * FROM df
        """)

        print(f"Data loaded successfully into {db_path}")

    finally:
        con.close()

def main():
    """Main execution function."""
    print("Starting data ingestion process...")

    # Create necessary directories
    ensure_directories()

    # Download the data
    print("Downloading data...")
    csv_path = download_data()
    print(f"Data downloaded to {csv_path}")

    # Load into DuckDB
    print("Loading data into DuckDB...")
    load_to_duckdb(csv_path)

    print("Data ingestion complete!")

if __name__ == "__main__":
    main()
