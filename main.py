import requests

class DataProcessor:
    def clean_data(self, data):
        # Removes None values
        cleaned_data = [item for item in data if item is not None]
        # Removes duplicates based on article title
        seen_titles = set()
        unique_articles = []
        
        for article in cleaned_data:
            title = article['title']
            if title not in seen_titles:
                seen_titles.add(title)
                unique_articles.append(article)
        
        return unique_articles

    def process_clean_data(self, data):
        cleaned_data = self.clean_data(data)
        # Processes logic 
        return cleaned_data

def fetch_technology_articles(api_key):
    url = f'https://newsapi.org/v2/everything?q=technology&apiKey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        # Returns a list of dictionaries with title and published date
        return [
            {
                'title': article['title'],
                'publishedAt': article['publishedAt']
            } 
            for article in articles
        ]
    else:
        print("Failed to fetch articles:", response.status_code)
        return []

def main():
    API_KEY = '5e0dcc5594ec49d5bbe68f66b98e3c5d'  
    dp = DataProcessor()
    
    tech_articles = fetch_technology_articles(API_KEY)
    processed_data = dp.process_clean_data(tech_articles)

    # Displays processed data with a specific message
    print("Different articles on technology:")
    for article in processed_data:
        print(f"- Title: {article['title']}, Published at: {article['publishedAt']}")

if __name__ == "__main__":
    main()
