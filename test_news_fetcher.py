import pandas as pd
import unittest
from api import fetch_news
from datacleaner import clean_data

class TestAPI(unittest.TestCase):
    
    def test_fetch_news(self):
        api_key = '5e0dcc5594ec49d5bbe68f66b98e3c5d'
        df = fetch_news(api_key, query='technology')
        self.assertIsNotNone(df, "API data should not be None")
        self.assertGreater(len(df), 0, "API data should not be empty")

    def test_clean_data(self):
        raw_data = {'title': ['  Test Article 1  ', 'Test Article 2', 'Test Article 2', None],
                    'description': ['Desc 1', 'Desc 2', 'Desc 2', 'Desc 3']}
        df = pd.DataFrame(raw_data)
        
        cleaned_df = clean_data(df)
        self.assertEqual(len(cleaned_df), 2, "Dataframe should have 2 rows after cleaning")
        self.assertNotIn(None, cleaned_df['title'], "Null values should be removed")

if __name__ == '__main__':
    unittest.main()