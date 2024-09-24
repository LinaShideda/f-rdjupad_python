from sqlalchemy import create_engine

def save_to_sql(df, db_url, table_name):
    engine = create_engine(db_url)
    
    try:
        # Saves DataFrame to a SQL table
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data saved to table {table_name} in database.")
    except Exception as e:
        print(f"Failed to save data to SQL: {e}")