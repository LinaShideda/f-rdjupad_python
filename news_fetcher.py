import requests
import pandas as pd

def fetch_news_data(api_key, query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        df = pd.DataFrame(articles)
        return df, url
    else:
        raise Exception(f"Failed to fetch news: {response.status_code}")