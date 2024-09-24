import pandas as pd
from datacleaner import clean_data  # Only import clean_data from datacleaner

# Creates a sample DataFrame for testing
sample_data = {
    'title': ['Article 1', 'Article 2', None, '  Article 3  ', 'Article 2'],
    'content': ['Content 1', 'Content 2', 'Content 3', 'Content 4', 'Content 2']
}
df = pd.DataFrame(sample_data)

def test_clean_data():
    cleaned_df = clean_data(df)
    assert isinstance(cleaned_df, pd.DataFrame)  # Checks if the result is a DataFrame
    assert cleaned_df.shape[0] == 3  # Expects 3 rows after cleaning
    assert cleaned_df['title'].iloc[2] == 'Article 3'  # Ensures whitespace is trimmed
    assert cleaned_df['title'].duplicated().sum() == 0  # Ensures there are no duplicates

# Runs the test
if __name__ == "__main__":
    test_clean_data()
    print("All tests passed!")