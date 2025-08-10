# Copy this code into a new cell in your project.ipynb notebook

# SQLite Connection (No server required - works offline)
import sqlite3

# Create SQLite database connection
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
    for row in result:
        print(row) 