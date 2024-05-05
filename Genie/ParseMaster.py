import pandas as pd
import json

def read_questions(file_path: str):
    df = pd.read_excel(file_path)
    filtered = df[['subkey', 'input', 'contextDict', 'expoutput']].head(10)
    filtered['contextDict'].update(filtered['contextDict'].apply(lambda x: json.loads(x.replace("'", "\""))))
    filtered['expoutput'].update(filtered['expoutput'].apply(lambda x: json.loads(x.replace("'", "\""))))
    # return df['input'].head(10).tolist()  # Assuming the Excel column is named 'Question'
    return filtered.head(10)
