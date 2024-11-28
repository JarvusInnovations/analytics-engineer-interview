#!/usr/bin/env python3
import os
import requests
import duckdb
import pandas as pd
import zipfile
import io
from pathlib import Path

def ensure_directories():
    """Create necessary directories if they don't exist."""
    Path("data/raw/gtfs").mkdir(parents=True, exist_ok=True)

def download_gtfs_data():
    """Download the latest SEPTA GTFS feed."""
    url = 'https://github.com/septadev/GTFS/releases/latest/download/gtfs_public.zip'
    print(f"Downloading GTFS feed from {url}...")

    response = requests.get(url)
    response.raise_for_status()

    output_path = "data/raw/gtfs/septa_gtfs.zip"
    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"Downloaded GTFS to {output_path}")
    return output_path

def extract_nested_tables(zip_path):
    """Extract routes.txt and agency.txt from nested GTFS zip files."""
    all_tables = {'routes': [], 'agency': []}

    with zipfile.ZipFile(zip_path, 'r') as outer_zip:
        # Process each nested zip file
        for nested_zip_name in outer_zip.namelist():
            print(f"Processing {nested_zip_name}...")
            mode = 'bus' if 'bus' in nested_zip_name.lower() else 'rail'

            # Read nested zip file
            with outer_zip.open(nested_zip_name) as nested_file:
                nested_zip_data = io.BytesIO(nested_file.read())

                with zipfile.ZipFile(nested_zip_data) as nested_zip:
                    # Extract routes.txt and agency.txt
                    for filename in ['routes.txt', 'agency.txt']:
                        with nested_zip.open(filename) as f:
                            df = pd.read_csv(io.BytesIO(f.read()))
                            # Add source information
                            df['data_source'] = mode
                            # Add to appropriate list
                            key = filename.replace('.txt', '')
                            all_tables[key].append(df)

    # Combine all dataframes
    combined_tables = {
        'routes': pd.concat(all_tables['routes'], ignore_index=True),
        'agency': pd.concat(all_tables['agency'], ignore_index=True)
    }

    return combined_tables

def get_mode_name(route_type):
    """Map GTFS route_type to human-readable mode name."""
    mode_names = {
        0: 'Tram/Streetcar/Light rail',
        1: 'Subway/Metro',
        2: 'Rail',
        3: 'Bus',
        4: 'Ferry',
        5: 'Cable tram',
        6: 'Aerial lift',
        7: 'Funicular',
        11: 'Trolleybus',
        12: 'Monorail'
    }
    return mode_names.get(route_type, 'Unknown')

def load_to_duckdb(tables):
    """Load the GTFS data into DuckDB with transformations."""
    db_path = "data/analytics.db"
    con = duckdb.connect(db_path)

    try:
        routes_df = tables['routes']
        agency_df = tables['agency']

        # Add mode_name to routes
        routes_df['mode_name'] = routes_df['route_type'].apply(get_mode_name)

        # Create tables
        con.execute("""
            CREATE OR REPLACE TABLE raw_gtfs_routes AS
            SELECT * FROM routes_df
        """)

        con.execute("""
            CREATE OR REPLACE TABLE raw_gtfs_agency AS
            SELECT * FROM agency_df
        """)

        print(f"Data loaded successfully into {db_path}")

    finally:
        con.close()

def main():
    """Main execution function."""
    print("Starting GTFS data ingestion process...")

    # Create necessary directories
    ensure_directories()

    # Download the GTFS feed
    zip_path = download_gtfs_data()

    # Extract and process tables
    print("Processing GTFS data...")
    tables = extract_nested_tables(zip_path)

    # Load into DuckDB
    print("Loading data into DuckDB...")
    load_to_duckdb(tables)

    print("GTFS data ingestion complete!")

if __name__ == "__main__":
    main()
