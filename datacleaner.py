import pandas as pd

def clean_data(df):
    # Removes null values and duplicates
    df_cleaned = df.dropna()  # Removes rows with null values
    df_cleaned = df_cleaned.drop_duplicates()  # Removes duplicates
    
    # Further processing or formatting of columns
    df_cleaned['title'] = df_cleaned['title'].str.strip()  # Trims whitespace in the 'title' column
    
    return df_cleaned