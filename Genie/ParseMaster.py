import pandas as pd

def read_questions(file_path):
    df = pd.read_excel(file_path)
    return df['input'].head(10).tolist()  # Assuming the Excel column is named 'Question'
