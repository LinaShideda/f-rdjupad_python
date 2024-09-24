import requests
import pandas as pd
import logging

def fetch_news(api_key, query='space'):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses
        news_data = response.json()

        if news_data['status'] == 'ok':
            logging.info("Fetched global news data successfully.")
            return pd.json_normalize(news_data['articles'])  # Normalises the JSON data to a DataFrame
        else:
            logging.error(f"Failed to fetch news: {news_data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching news: {e}")
        return None