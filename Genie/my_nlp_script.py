import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from tqdm import tqdm

# Ensure NLTK resources are downloaded
nltk.download('punkt')

# Define transportation modes for categorization
category_keywords = {
    'Public': ['public', 'bus', 'train', 'subway', 'tram', 'metro', 'public transport', 'trolley', 'streetcar',
               'light rail', 'commuter train', 'public bus', 'shuttle', 'minibus', 'transit'],
    'Private': ['private', 'car', 'motorcycle', 'scooter', 'bike', 'bicycle', 'motorbike', 'SUV', 'pickup truck',
                'sedan', 'coupe', 'convertible', 'private vehicle', 'personal car', 'electric scooter'],
    'Maritime': ['boat', 'ship', 'ferry', 'yacht', 'sailboat', 'motorboat', 'canoe', 'kayak', 'vessel',
                 'cruise ship', 'fishing boat', 'water taxi', 'paddle boat', 'sailing ship'],
    'Aerospace': ['airplane', 'jet', 'helicopter', 'aircraft', 'commercial flight', 'private jet',
                  'drone', 'glider', 'airliner', 'fighter jet', 'biplane', 'chopper', 'airbus', 'boeing'],
}


def categorize_transportation(response):
    tokens = word_tokenize(str(response).lower())
    found_categories = []

    # Match tokens to categories
    for token in tokens:
        for category, keywords in category_keywords.items():
            if token in keywords:
                found_categories.append(category)

    # Remove duplicates to ensure we get unique categories
    unique_categories = list(dict.fromkeys(found_categories))

    # Determine 'Keyword match' and 'Category match'
    if len(unique_categories) == 0:
        keyword_match = '0'
    elif len(unique_categories) == 1:
        keyword_match = '1'
    else:
        keyword_match = 'Multiple'

    # First unique category or 'N/A' if none found
    category_match = unique_categories[0] if unique_categories else 'N/A'

    return {'Keyword match': keyword_match, 'Category match': category_match}


def process_responses(file_path):
    # Read data from Excel
    df = pd.read_excel(file_path)

    tqdm.pandas(desc="Processing Responses")  # Enable tqdm for pandas apply
    df['aiout'] = df['Response'].progress_apply(lambda x: categorize_transportation(x))

    # Save the updated DataFrame to a new Excel file
    df.to_excel(file_path.replace('.xlsx', '_updated.xlsx'), index=False)


# Path to the Excel file
file_path = 'output/test_output.xlsx'
process_responses(file_path)
