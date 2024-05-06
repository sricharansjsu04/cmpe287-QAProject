import pandas as pd
import json

def read_questions(file_path: str):
    df = pd.read_excel(file_path)
    filtered = df[['subkey', 'input', 'contextDict', 'expoutput']]
    filtered['contextDict'] = filtered['contextDict'].apply(lambda x: json.loads(x.replace("'", "\"")))
    filtered['expoutput'] = filtered['expoutput'].apply(lambda x: json.loads(x.replace("'", "\"")))
    return filtered
