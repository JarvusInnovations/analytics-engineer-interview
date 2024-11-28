#!/usr/bin/env python3
import duckdb

def main():
    """Query and display the routes by mode analysis."""
    db_path = "data/analytics.db"
    con = duckdb.connect(db_path)

    try:
        # Query the mart model
        results = con.execute("""
            SELECT * FROM main_marts.mart_routes_by_mode
            ORDER BY agency_name, mode_name;
        """).fetchall()

        # Print header
        print("\nSEPTA Routes Analysis")
        print("-" * 80)
        print(f"{'Agency Name':<40} {'Mode':<25} {'Route Count':<10}")
        print("-" * 80)

        # Print results
        for row in results:
            print(f"{row[0]:<40} {row[1]:<25} {row[2]:<10}")

    finally:
        con.close()

if __name__ == "__main__":
    main()
