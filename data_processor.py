class DataProcessor:
    def clean_data(self, data):
        # Removes None values and duplicates
        cleaned_data = [item for item in data if item is not None]
        cleaned_data = list(set(cleaned_data))  # Removes duplicates
        return cleaned_data

    def process_clean_data(self, data):
        cleaned_data = self.clean_data(data)
        # Processes logic 
        return cleaned_data