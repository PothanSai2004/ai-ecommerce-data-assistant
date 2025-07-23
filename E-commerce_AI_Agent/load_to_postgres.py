
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Database connection config
DB_NAME = "ecommerce"
DB_USER = "postgres"
DB_PASSWORD = "pothan2004"
DB_HOST = "localhost"
DB_PORT = "5432"

# Paths to CSV files
ad_sales_csv = "dataset\Product-Level Ad Sales and Metrics (mapped).csv"
total_sales_csv = "dataset\Product-Level Total Sales and Metrics (mapped).csv"
eligibility_csv = "dataset\Product-Level Eligibility Table (mapped).csv"

# Create connection using SQLAlchemy
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load CSVs
ad_sales_df = pd.read_csv(ad_sales_csv)
total_sales_df = pd.read_csv(total_sales_csv)
eligibility_df = pd.read_csv(eligibility_csv)

# Upload to PostgreSQL
print("Uploading ad_sales_metrics...")
ad_sales_df.to_sql("ad_sales_metrics", engine, if_exists="append", index=False)

print("Uploading total_sales_metrics...")
total_sales_df.to_sql("total_sales_metrics", engine, if_exists="append", index=False)

print("Uploading eligibility...")
eligibility_df.to_sql("eligibility", engine, if_exists="append", index=False)

print("All data loaded successfully!")
