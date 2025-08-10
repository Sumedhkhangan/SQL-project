# SQLite Solution for Walmart Data Analysis
# This resolves the ConnectionRefusedError by using SQLite instead of MySQL/PostgreSQL

import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# Load the cleaned data
df = pd.read_csv('walmart_clean_data.csv')

print("Data loaded successfully!")
print(f"Shape: {df.shape}")

# SQLite Connection (No server required - works offline)
engine_sqlite = create_engine("sqlite:///walmart_database.db")

try:
    # Test the connection
    with engine_sqlite.connect() as conn:
        print("SQLite Connection Successful!")
        print("Database file: walmart_database.db")
except Exception as e:
    print(f"SQLite Connection Error: {e}")

# Load data into SQLite database
df.to_sql(name='walmart', con=engine_sqlite, if_exists='replace', index=False)
print("Data successfully loaded into SQLite database!")

# Verify data was loaded
with engine_sqlite.connect() as conn:
    result = conn.execute("SELECT COUNT(*) FROM walmart")
    count = result.fetchone()[0]
    print(f"Total records in database: {count}")
    
    # Show first few records
    result = conn.execute("SELECT * FROM walmart LIMIT 5")
    print("\nFirst 5 records:")
    for row in result:
        print(row)

# Example SQL queries
print("\n=== Sample SQL Queries ===")

with engine_sqlite.connect() as conn:
    # Total sales by city
    result = conn.execute("""
        SELECT city, SUM(total) as total_sales 
        FROM walmart 
        GROUP BY city 
        ORDER BY total_sales DESC
    """)
    print("\nTotal sales by city:")
    for row in result:
        print(f"{row[0]}: ${row[1]:,.2f}")
    
    # Top categories
    result = conn.execute("""
        SELECT category, COUNT(*) as count 
        FROM walmart 
        GROUP BY category 
        ORDER BY count DESC 
        LIMIT 5
    """)
    print("\nTop 5 categories:")
    for row in result:
        print(f"{row[0]}: {row[1]} sales")

print("\nSQLite solution completed successfully!")
print("No ConnectionRefusedError - SQLite works offline!") 